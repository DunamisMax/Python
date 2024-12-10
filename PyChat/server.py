import socket
import threading
from typing import List, Dict
from pydantic import BaseModel
from fastapi import FastAPI
import time

# Global state (in-memory)
# Maps a username to its (conn, addr) tuple
clients: Dict[str, socket.socket] = {}
usernames: set = set()


class Message(BaseModel):
    sender: str
    content: str


app = FastAPI()

# Configuration
HOST = "0.0.0.0"  # Listen on all interfaces
PORT = 42069  # TCP port for chat server


def handle_client(conn: socket.socket, addr):
    """
    Handle an individual client connection.
    The client first sends a desired username.
    The server assigns it (or a variant if taken),
    notifies the client, and then relays messages.
    """
    try:
        # First message from client: desired username
        desired_username = conn.recv(1024).decode().strip()
        username = assign_username(desired_username)

        # Notify the client of their final assigned username
        conn.sendall(f"Your username is: {username}\n".encode())

        broadcast(
            Message(sender="SERVER", content=f"{username} has joined the chat."),
            exclude=username,
        )

        # Listen for messages from this client
        while True:
            data = conn.recv(1024)
            if not data:
                break
            msg_text = data.decode().strip()
            if msg_text.lower() == "/quit":
                break
            # Broadcast the message to others
            broadcast(Message(sender=username, content=msg_text), exclude=username)

    except Exception as e:
        # In production, add proper logging
        pass
    finally:
        disconnect_user(username)


def assign_username(desired_username: str) -> str:
    """
    Assign a unique username, appending numbers if needed.
    """
    base = desired_username
    counter = 1
    while desired_username in usernames:
        desired_username = f"{base}{counter}"
        counter += 1
    usernames.add(desired_username)
    return desired_username


def broadcast(msg: Message, exclude: str = None):
    """
    Send a message to all connected clients except the excluded one.
    """
    msg_str = f"[{msg.sender}]: {msg.content}\n"
    for user, conn in clients.items():
        if user != exclude:
            try:
                conn.sendall(msg_str.encode())
            except:
                # If sending fails, remove that user
                disconnect_user(user)


def disconnect_user(username: str):
    """
    Disconnect a user and clean up resources.
    """
    if username in usernames:
        usernames.remove(username)
    conn = clients.pop(username, None)
    if conn:
        try:
            conn.close()
        except:
            pass
    broadcast(Message(sender="SERVER", content=f"{username} has left the chat."))


def start_tcp_server():
    """
    Start the TCP server that handles raw socket connections.
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(5)
    print(f"Chat server listening on {HOST}:{PORT}...")
    while True:
        conn, addr = s.accept()
        # We must wait for the username assignment before adding to clients
        # We'll temporarily do it inside the handle_client
        # but to maintain state we need to store after username known
        # We'll store connection as None until username is decided
        # Actually, we can do username assignment in handle_client then store.
        # For that we do a small trick: assign and store inside handle_client.

        # We'll handle it directly inside handle_client, after determining username.
        def client_wrapper():
            # We'll handle username assignment inside the handler
            # After assign_username, add to clients dict.
            # Because we need the connection and username known.
            # We must do a small protocol: receive desired username first,
            # do that before adding to global dict.
            data = conn.recv(1024)
            desired = data.decode().strip()
            username = assign_username(desired)
            clients[username] = conn
            conn.sendall(f"Your username is: {username}\n".encode())
            broadcast(
                Message(sender="SERVER", content=f"{username} has joined the chat."),
                exclude=username,
            )

            # Now enter a loop to handle messages
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                msg_text = data.decode().strip()
                if msg_text.lower() == "/quit":
                    break
                broadcast(Message(sender=username, content=msg_text), exclude=username)

            disconnect_user(username)

        threading.Thread(target=client_wrapper, daemon=True).start()


# FastAPI lifecycle event to start the TCP server in a background thread
@app.on_event("startup")
def on_startup():
    threading.Thread(target=start_tcp_server, daemon=True).start()
    # Give the socket server a moment to start
    time.sleep(0.5)


# A trivial endpoint to confirm server running
@app.get("/")
def read_root():
    return {"status": "ok", "users_online": list(usernames)}
