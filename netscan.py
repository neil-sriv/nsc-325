import click
import json
from nmap import scan
from data_models import Device
import socket
import nmap3


@click.command()
@click.option('-d', '--devices', help='Print the list of devices on the network', is_flag=True)
@click.option('-s', '--scan', help='Scan for the list of devices on the network', is_flag=True)
@click.option('-v', '--verbose', help='Print verbose', is_flag=True)
def cli(devices, scan, verbose):
    """Scan your wifi and list connected devices"""
    if devices or scan:
        try:
            current_devices(scan=scan, verbose=verbose)
        except nmap3.exceptions.NmapExecutionError:
            print('If on Linux or OSX please run with "sudo", if on Windows please run as admin!')


def nmap_scan(ip):
    return scan(ip)


def get_ip():
    ips = socket.gethostbyname_ex(socket.gethostname())[-1]
    ip = ips[-1]
    ip = ip.split('.')[:-1]
    ip = '.'.join(ip)+'.1'
    return ip


def current_devices(scan=False, verbose=False):
    curr_devices = scan_devices()
    if scan:
        all_devices = nmap_scan(get_ip())
        store_devices(all_devices)
        new_devices = scan_devices()
        if len(new_devices)==0:
            print('No new devices connected to the network.')
        else:
            print_devices('New Devices', compare_devices(
                curr_devices, new_devices), verbose)
    else:
        print_devices('Current Devices', curr_devices, verbose)

def store_devices(devices):
    with open('devices.json', 'w') as f:
        json.dump(devices, f)


def compare_devices(old, new):
    old_ip = set(old.keys())
    new_ip = set(new.keys())

    diff = list(new_ip.difference(old_ip))
    print((diff))
    new_devices = {ip: new[ip] for ip in diff}
    return new_devices


def scan_devices():
    with open('devices.json') as f:
        data = json.load(f)
    return data


def print_devices(title, devices, verbose):
    print(f'{title}')
    for ip, dev in devices.items():
        if 'os' in dev:
            d = Device(ip=ip, hostname=dev['hostname'], mac=dev['mac'],
                    vendor=dev['vendor'], ports=dev['ports'], os=dev['os'])
        else:
            d = Device(ip=ip, hostname=dev['hostname'], mac=dev['mac'],
                    vendor=dev['vendor'], ports=dev['ports'])
        if verbose:
            d.print_verbose()
        else:
            d.print_simple()


if __name__ == '__main__':
    cli()
