import socket
import threading
import sys

# Check if user entered required arguments
if len(sys.argv) != 4:
    print("Usage: python scanner.py <target> <start_port> <end_port>")
    sys.exit()

# Read user input from command line
target = sys.argv[1]
start_port = int(sys.argv[2])
end_port = int(sys.argv[3])

# Function to scan one port
def scan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    result = s.connect_ex((target, port))  # 0 = success
    if result == 0:
        print(f"[+] Port {port} is OPEN")
    s.close()

# Start threads for each port
for port in range(start_port, end_port + 1):
    t = threading.Thread(target=scan, args=(port,))
    t.start()
