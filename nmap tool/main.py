import nmap
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
            print("You entered a valid ip address and a valid ports range !!")
            break

    except:

        print("You entered an invalid ip address !!")

scanner = nmap.PortScanner()
while True:
    scan = input("""\n Please enter the type of scan you want to run 
                       1)SYN ACK Scan 
                       2)UDP Scan 
                       3) Comprehensive Scan\n""")
    if scan <= "3":
        break

if (scan == "1"):
    print("Nmap version: ", scanner.nmap_version())
    scanner.scan(ip_address, port_range, "-v -sS")
    print(scanner.scaninfo())
    print("IP status:", scanner[ip_address].state())
    print(scanner[ip_address].all_protocols())
    print("Open Ports", scanner[ip_address]["tcp"].keys())
elif (scan == "2"):
    print("Nmap version: ", scanner.nmap_version())
    scanner.scan(ip_address, port_range, "-v -sU")
    print(scanner.scaninfo())
    print("IP status:", scanner[ip_address].state())
    print(scanner[ip_address].all_protocols())
    print("Open Ports", scanner[ip_address]["udp"].keys())
elif (scan == "3"):
    print("Nmap version: ", scanner.nmap_version())
    scanner.scan(ip_address, port_range, "-v -sS -sV -sC -A -O")
    print(scanner.scaninfo())
    print("IP status:", scanner[ip_address].state())
    print(scanner[ip_address].all_protocols())
    print("Open Ports", scanner[ip_address]["udp"].keys())
else:
    print("Please enter an appropriate option !!")
