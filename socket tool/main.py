import socket
import ipaddress
import re

print("Welcome this is a simple automation tool for penetration tests")
print("<================================================================>")
port_range_pattern = re.compile("([0-9]+)-([0-9]+)")

while True:

    ip_address = input("Enter the IP address to be scanned: ")
    port_range = input("Enter the ports range you want to scan !!")

    try:

        ip_address_is_valid = ipaddress.IPv4Address(ip_address)
        ports_range_is_valid = port_range_pattern.match(port_range.replace(" ", ""))
        if ip_address_is_valid and ports_range_is_valid:
            port_min = int(ports_range_is_valid.group(1))
            port_max = int(ports_range_is_valid.group(2))
            print("You entered a valid ip address and a valid ports range !!")
            break

    except:

        print("You entered an invalid ip address !!")


open_ports = []
for port in range(port_min, port_max):
    try:

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            s.connect((ip_address, port))
            open_ports.append(port)
    except:

        pass

for port in open_ports :
    print(f'port {port} is open on {ip_address}')
