import socket

def scan_port(target, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.4)

        result = sock.connect_ex((target, port))

        if result == 0 : 
            try:
                sock.send(b'HEAD / HTTP/1.1\r\n\r\n')

                banner = sock.recv(1024).decode().strip()
                clean_banner = banner.split('\n')[0]
                sock.close()
                return clean_banner
            except:
                sock.close()
                return "Open (No Banner)"
            
        sock.close()
        return False
    except:
        return False
    
def main():
    target_input = input("Enter targetIP/Domain (e.g.,scanme.nmap,org): ")
    target = socket.gethostbyname(target_input)

    print(f"\nScanning ports 1-1024 on {target} ...")

    for port in range(1,1025):
        response = scan_port(target, port)

        if response:
            print(f"[+] Port {port} is OPEN | Service: {response}")
        
if __name__ == "__main__":
    main()