import socket
import pyfiglet

banner = pyfiglet.figlet_format("PScan", font="small_poison")
print(banner)

target = input("Enter the target IP address or domain: ")
start_port =int(input("Enter the starting port number: "))
end_port = int(input("Enter the ending port number: "))

print(f"Scanning {target} from port {start_port} to {end_port}...")

for port in range(start_port, end_port + 1):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)  # Set a timeout for the connection attempt
    result = sock.connect_ex((target, port))

    if result == 0:
        print(f"Port {port} is open")
    else:
        print(f"Port {port} is closed")
    sock.close()

print("Port scanning completed.")

# simple port scanner I made using socket
# https://docs.python.org/3/library/socket.html

#added a little banner there :)