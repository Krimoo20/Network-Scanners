import nmap

scanner = nmap.PortScanner()

print("Welcome this is a simple automation tool for penetration tests")
print("<================================================================>")
ip_adresse = input("Enter the IP address to be scanned: ")

scan = input("""\n Please enter the type of scan you want to run 
                   1)SYN ACK Scan 
                   2)UDP Scan 
                   3) Comprehensive Scan\n""")
if (scan == "1"):
    print("Nmap version: ",scanner.nmap_version())
    scanner.scan(ip_adresse,"1-1024","-v sS");
    print(scanner.scaninfo())
    print("IP status:",scanner[ip_adresse].state())
    print(scanner[ip_adresse].all_protocols())
    print("Open Ports", scanner[ip_adresse]["tcp"].keys())
