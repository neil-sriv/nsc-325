# Netscan
Netscan is an easy-to-use cli tool to scan for devices on your network.
## Features
- Scan network for currently connected devices
- Store list of devices from last scan
### Coming Soon
- Block selected devices from network
- Analyze network traffic of connected devices
- Automated threat detection
## Installation
```bash
$ git clone https://github.com/neil-sriv/nsc-325.git
$ cd nsc-325
$ pip install -r requirements.txt
$ pip install --editable .
$ netscan --help
```
## Usage
### Help
```bash
Usage: netscan [OPTIONS]

  Scan your wifi and list connected devices

Options:
  -d, --devices  Print the list of devices on the network
  -s, --scan     Scan for the list of devices on the network
  -v, --verbose  Print verbose
  --help         Show this message and exit.
  ```
### Device Discovery
List devices connected to network since last scan:
```bash
$ netscan --devices
IP: 127.0.0.1
Hostname: None
MAC: AB:CD:EF:GH:IJ:KL

IP: 127.0.0.2
Hostname: None
MAC: AB:CD:EF:GH:IJ:KL
```
Scan network for new devices connected to the network:
```bash
$ netscan --scan
Scanning 127.0.0.1...
New Devices:
IP: 127.0.0.2
Hostname: None
MAC: MN:OP:QR:ST:UV:WX
```
Add `--verbose` for more details:
```bash
IP: 127.0.0.1
Hostname: None
MAC: AB:CD:EG:GH:JK:LM

Vendor: Amazon Technologies
Possible OS:
	Name: Sony X75CH-series Android TV (Android 5.0)
	Accuracy: 98
	Type: media device

	Name: Android 4.1 - 6.0 (Linux 3.4 - 3.14)
	Accuracy: 96
	Type: phone

	Name: Android 5.1
	Accuracy: 96
	Type: phone

Open ports: ['8009']
```
