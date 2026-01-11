# Port Scanner

A simple Python-based port scanner that identifies open ports and performs banner grabbing to detect running services on target systems.

## Features

- Scans ports 1-1024 on target systems
- Banner grabbing to identify service versions
- Clean output displaying open ports and detected services
- Timeout handling for faster scanning
- Domain name resolution support

## Requirements

- Python 3.x
- No external libraries required (uses standard `socket` library)

## Installation

1. Clone the repository:
```
git clone https://github.com/dhruvimoliya/port-scanner.git
cd port-scanner
```

2. Ensure Python 3 is installed:
```
python3 --version
```

## Usage

Run the scanner:
```
python3 port-scanner.py
```

When prompted, enter the target IP address or domain name:
```
Enter targetIP/Domain (e.g.,scanme.nmap.org): scanme.nmap.org
```

The scanner will display open ports and attempt to identify running services.

## Example Output

```
Scanning ports 1-1024 on 45.33.32.156 ...
[+] Port 22 is OPEN | Service: SSH-2.0-OpenSSH_6.6.1p1 Ubuntu-2ubuntu2.13
[+] Port 80 is OPEN | Service: HTTP/1.1 200 OK
[+] Port 443 is OPEN | Service: Open (No Banner)
```

## How It Works

1. **Port Scanning**: Uses TCP socket connections to check if ports are open
2. **Banner Grabbing**: Sends HTTP HEAD request and captures service responses
3. **Timeout**: Set to 0.4 seconds to balance speed and accuracy
4. **Error Handling**: Gracefully handles unreachable hosts and connection failures

## Legal Disclaimer

**Important**: This tool is for educational purposes only.

- Only scan systems you own or have explicit permission to test
- Unauthorized port scanning may be illegal in your jurisdiction
- Always obtain proper authorization before testing any network or system
- The author is not responsible for misuse of this tool

## Limitations

- Scans only ports 1-1024 (common ports)
- Single-threaded scanning (slower for large port ranges)
- Basic banner grabbing (may not work for all services)
- No UDP port scanning support

## Contributing

Suggestions and improvements are welcome! Feel free to open an issue or submit a pull request.

## License

This project is open source and available for educational purposes.

---

**Note**: Always practice responsible disclosure and ethical hacking principles.
