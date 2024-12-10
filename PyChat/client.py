import socket
import threading
import sys


def receive_messages(conn, assigned_username, stop_event):
    """
    Continuously receive and display messages from the server.
    If the connection is lost or closed, print a notification and set stop_event.
    """
    while not stop_event.is_set():
        try:
            data = conn.recv(1024)
            if not data:
                # Connection closed by server or network error
                print("\n[SYSTEM] Connection closed by the server.")
                stop_event.set()
                break
            message = data.decode().rstrip("\n")
            # Print the received message
            # We print a newline first to ensure we are not breaking into the user's input line
            print(f"\n{message}")
            # Reprint the prompt so the user can continue typing
            print(f"You> ", end="", flush=True)
        except:
            # Any receive error means we consider connection lost
            print("\n[SYSTEM] Connection lost.")
            stop_event.set()
            break


def main():
    print("Welcome to PyChat Client!")
    print("You will be prompted for the server IP and a desired username.\n")

    server_ip = input("Enter the server IP address: ").strip()
    desired_username = input("Enter your desired username: ").strip()

    # Connect to the TCP server
    server_port = 42069  # Make sure it matches server.py's PORT
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        conn.connect((server_ip, server_port))
    except Exception as e:
        print(f"[SYSTEM] Failed to connect to {server_ip}:{server_port}. Error: {e}")
        sys.exit(1)

    # Send the desired username
    conn.sendall(f"{desired_username}\n".encode())

    # Receive the assigned username (the server responds with a line)
    assigned_line = conn.recv(1024).decode().strip()
    if not assigned_line:
        print("[SYSTEM] No response from server for username assignment.")
        sys.exit(1)

    # Extract the assigned username
    assigned_username = assigned_line.replace("Your username is: ", "")

    # Display welcome info
    print("\n" + "=" * 50)
    print(f"Welcome, {assigned_username}!")
    print("You are now connected to the chat.")
    print("Type your message and press Enter to send.")
    print("Type /quit to leave the chat.")
    print("=" * 50 + "\n")

    # A threading event to signal when the connection should stop
    stop_event = threading.Event()

    # Start a thread to listen for incoming messages
    receiver = threading.Thread(
        target=receive_messages, args=(conn, assigned_username, stop_event), daemon=True
    )
    receiver.start()

    # Print initial prompt
    print("You> ", end="", flush=True)

    # Main loop to send messages
    while not stop_event.is_set():
        try:
            msg = input()
        except EOFError:
            # If user hits Ctrl+D or similar
            msg = "/quit"

        if stop_event.is_set():
            break

        if msg.strip().lower() == "/quit":
            conn.sendall(msg.encode())
            break

        # Send message
        conn.sendall((msg + "\n").encode())
        # After sending message, reprint prompt
        print("You> ", end="", flush=True)

    # Cleanup
    stop_event.set()
    try:
        conn.close()
    except:
        pass
    print("\n[SYSTEM] Disconnected. Bye!")
    sys.exit(0)


if __name__ == "__main__":
    main()
