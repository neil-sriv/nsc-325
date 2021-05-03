class Device:
    def __init__(self, ip=None, hostname=None, mac=None, vendor=None, ports=None, os=None):
        self.__ip = ip
        self.__hostname = hostname
        self.__mac = mac
        self.__vendor = vendor
        self.__ports = ports
        self.__os = os

    def print_verbose(self):
        print(
            f'IP: {self.__ip}\nHostname: {self.__hostname}\nMAC: {self.__mac}\n')
        print(f'Vendor: {self.__vendor}')
        print('Possible OS:')
        if self.__os is None:
            return
        for guess in self.__os:
            name,acc,type = guess['name'], guess['accuracy'], guess['osclass']['type']
            print(f'\tName: {name}\n\tAccuracy: {acc}\n\tType: {type}\n')
        print(f'Open ports: {self.__ports}\n')

    def print_simple(self):
        print(
            f'IP: {self.__ip}\nHostname: {self.__hostname}\nMAC: {self.__mac}\n')

    def __str__(self):
        return str([self.__ip, self.__hostname, self.__mac,
                    self.__vendor, self.__ports, self.__os])
