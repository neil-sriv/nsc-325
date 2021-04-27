import click
import json
from nmap import scan
from data_models import Device
import socket


@click.command()
@click.option('-d','--devices', help='Print the list of devices on the network', is_flag=True)
@click.option('-s','--scan', help='Scan for the list of devices on the network', is_flag=True)
@click.option('-v', '--verbose', help='Print verbose', is_flag=True)
# @click.option('--scan', prompt='Your name',
#               help='The person to greet.')
def cli(devices, scan, verbose):
    """Scan your wifi and list connected devices"""
    if devices or scan:
        current_devices(scan=scan, verbose=verbose)


def nmap_scan(ip):
    return scan(ip)

def get_ip():
    ips = socket.gethostbyname_ex(socket.gethostname())[-1]
    ip = ips[-1]
    return ip




def current_devices(scan=False, verbose=False):
    with open('devices.json') as f:
        data = json.load(f)
    curr_devices = data['devices']
    if scan:
        nmap_scan(get_ip())
        new_devices = scan_devices()
        print_devices('New Devices', compare_devices(
            curr_devices, new_devices), verbose)
    else:
        print_devices('Current Devices', curr_devices, verbose)


def compare_devices(old, new):
    old_ip = set(old.keys())
    new_ip = set(new.keys())

    difference = new_ip.difference(old_ip)
    new_devices = {ip: new_ip[ip] for ip in difference}
    return new_devices


def scan_devices():
    with open('devices.json') as f:
        data = json.load(f)
    new_devices = data['devices']
    return new_devices


def print_devices(title, devices, verbose):
    print(f'{title}')
    for ip, dev in devices.items():
        d = Device(ip=ip, hostname=dev['hostname'], mac=dev['mac'],
                   vendor=dev['vendor'], ports=dev['ports'], os=dev['os'])
        if verbose:
            d.print_verbose()
        else:
            d.print_simple()


if __name__ == '__main__':
    cli()
