import socket
import threading
import sys


def receive_messages(conn):
    while True:
        try:
            data = conn.recv(1024)
            if not data:
                print("Connection closed by the server.")
                break
            print(data.decode(), end="")
        except:
            # If there's any error receiving, we assume connection closed.
            break


def main():
    server_ip = input("Enter the server IP address: ").strip()
    desired_username = input("Enter your desired username: ").strip()

    # Connect to the TCP server
    server_port = 42069  # Must match server.py PORT
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn.connect((server_ip, server_port))

    # Send the desired username
    conn.sendall(f"{desired_username}\n".encode())

    # Receive the assigned username (the server responds with a line)
    assigned_line = conn.recv(1024).decode().strip()
    print(assigned_line)
    assigned_username = assigned_line.replace("Your username is: ", "")

    # Start a thread to listen for incoming messages
    receiver = threading.Thread(target=receive_messages, args=(conn,), daemon=True)
    receiver.start()

    print("Type /quit to exit.")
    # Main loop to send messages
    while True:
        msg = input()
        if msg.strip().lower() == "/quit":
            conn.sendall(msg.encode())
            break
        conn.sendall((msg + "\n").encode())

    conn.close()
    sys.exit(0)


if __name__ == "__main__":
    main()
