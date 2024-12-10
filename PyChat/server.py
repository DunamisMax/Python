import socket
import threading
from typing import Dict
from pydantic import BaseModel
from fastapi import FastAPI
import time

# Global in-memory state
clients: Dict[str, socket.socket] = {}
usernames = set()

# Lock to ensure thread-safe operations on shared data structures
clients_lock = threading.Lock()
usernames_lock = threading.Lock()


class Message(BaseModel):
    sender: str
    content: str


app = FastAPI()

# Configuration
HOST = "0.0.0.0"  # Listen on all interfaces for the chat server
PORT = 42069  # TCP port for chat server connections


def assign_username(desired_username: str) -> str:
    """
    Assign a unique username by appending numbers if the desired one is taken.
    """
    base = desired_username
    counter = 1
    with usernames_lock:
        while desired_username in usernames:
            desired_username = f"{base}{counter}"
            counter += 1
        usernames.add(desired_username)
    return desired_username


def broadcast(msg: Message, exclude: str = None):
    """
    Send a message to all connected clients except the excluded one.
    If a client fails to receive, disconnect it.
    """
    msg_str = f"[{msg.sender}]: {msg.content}\n"
    to_disconnect = []
    with clients_lock:
        for user, conn in clients.items():
            if user != exclude:
                try:
                    conn.sendall(msg_str.encode())
                except:
                    # If sending fails, mark user for disconnection
                    to_disconnect.append(user)

    # Disconnect any clients that failed to receive
    for user in to_disconnect:
        print(f"[SERVER] Disconnecting {user} due to send failure.")
        disconnect_user(user)


def disconnect_user(username: str):
    """
    Disconnect a user and clean up resources.
    Remove them from clients and usernames, close their connection.
    Broadcast a leave message.
    """
    with clients_lock:
        conn = clients.pop(username, None)
    with usernames_lock:
        if username in usernames:
            usernames.remove(username)

    if conn:
        try:
            conn.close()
        except:
            pass

    # Notify others
    broadcast(Message(sender="SERVER", content=f"{username} has left the chat."))


def handle_client(conn: socket.socket, addr):
    """
    Handle an individual client connection.
    1. Receive the desired username from the client.
    2. Assign a unique username and notify the client.
    3. Add the client to the global clients list.
    4. Broadcast a join message.
    5. Continually read and broadcast messages until client quits or disconnects.
    """
    try:
        # Step 1: Get desired username
        data = conn.recv(1024)
        if not data:
            print("[SERVER] Connection closed before username received.")
            conn.close()
            return
        desired_username = data.decode().strip()
        username = assign_username(desired_username)

        # Step 2: Notify client of assigned username
        conn.sendall(f"Your username is: {username}\n".encode())

        # Step 3: Add client to global dictionary
        with clients_lock:
            clients[username] = conn

        # Step 4: Broadcast join message
        broadcast(
            Message(sender="SERVER", content=f"{username} has joined the chat."),
            exclude=username,
        )

        print(f"[SERVER] {username} connected from {addr}")

        # Step 5: Message loop
        while True:
            data = conn.recv(1024)
            if not data:
                print(f"[SERVER] {username} disconnected.")
                break
            msg_text = data.decode().strip()

            if msg_text.lower() == "/quit":
                print(f"[SERVER] {username} requested to quit.")
                break

            # Broadcast the user's message
            broadcast(Message(sender=username, content=msg_text), exclude=username)

    except Exception as e:
        # In production, you'd log this exception in detail.
        print(f"[SERVER] Error handling {addr}: {e}")
    finally:
        disconnect_user(username)


def start_tcp_server():
    """
    Start the TCP server that accepts new client connections.
    Spawns a new thread for each client.
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(
        socket.SOL_SOCKET, socket.SO_REUSEADDR, 1
    )  # Reuse address to avoid binding issues after restarts
    s.bind((HOST, PORT))
    s.listen(5)
    print(f"[SERVER] Chat server listening on {HOST}:{PORT}...")

    while True:
        conn, addr = s.accept()
        print(f"[SERVER] Incoming connection from {addr}")
        threading.Thread(target=handle_client, args=(conn, addr), daemon=True).start()


@app.on_event("startup")
def on_startup():
    """
    On FastAPI startup, launch the TCP chat server in a background thread.
    """
    threading.Thread(target=start_tcp_server, daemon=True).start()
    time.sleep(0.5)


@app.get("/")
def read_root():
    """
    A simple endpoint to confirm server health and list online users.
    """
    with usernames_lock:
        current_users = list(usernames)
    return {"status": "ok", "users_online": current_users}
