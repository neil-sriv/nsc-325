import nmap3
import json



def scan(ip):
    nmap = nmap3.NmapHostDiscovery()
    devices = dict()
    print(f'Scanning {ip}...')
    results = nmap.nmap_portscan_only(f'{ip}/24', args='-O')

    for i in results:
        # i here will be the local ip address of each device, but the last two will be stats and runtime - we don't need them displayed
        if (i == 'stats') or (i == 'runtime'):
            continue
        device = dict()

        # if statements here take care of errors - some devices do not have hostname or even macaddress
        if 'hostname' in results[i]:
            if results[i]['hostname'] == []:
                device['hostname'] = None

            else:
                device['hostname'] = results[i]['hostname'][0]['name']

        if 'macaddress' in results[i]:
            if results[i]['macaddress'] == None:
                device['mac'] = None
                device['vendor'] = None

            else:
                device['mac'] = results[i]['macaddress']['addr']

                if 'vendor' in results[i]['macaddress']:
                    device['vendor'] = results[i]['macaddress']['vendor']

                else:
                    device['vendor'] = None

        ports_list = []
        for ports in results[i]['ports']:
            ports_list.append(ports['portid'])
        device['ports'] = ports_list

        os = results[i]['osmatch']
        if len(os) <= 3:
            pass
        else:
            os = os[:3]

        for guess in os:
            device['os'] = os
        devices[i] = device
    return devices


if __name__ == "__main__":
    scan(ip)
