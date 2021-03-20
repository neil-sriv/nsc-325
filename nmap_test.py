# python3-nmap library needed
import nmap3
nmap = nmap3.Nmap()

# Put in your local network
results = nmap.scan_top_ports('192.168.1.1/24')

for i in results:

	# To see the raw data gathered by the scan, uncomment the next line
	#print(results[i])

	# i here will be the local ip address of each device, but the last two will be stats and runtime - we don't need them displayed
	if (i == 'stats') or (i == 'runtime'):
		continue

	print(i)

	# if statements here take care of errors - some devices do not have hostname or even macaddress
	if 'hostname' in results[i]:
		if results[i]['hostname'] == []:
			print('Hostname not found')

		else:
			print(results[i]['hostname'])

	if 'macaddress' in results[i]:
		if results[i]['macaddress'] == None:
			print('MAC address not found')
			print('Vendor information not found')

		else:
			print('MAC: ' + results[i]['macaddress']['addr'])
			
			if 'vendor' in results[i]['macaddress']:
				print('Vendor: ' + results[i]['macaddress']['vendor'])

			else:
				print('Vendor information not found')

	print()

print(str(len(results) - 2) + ' devices found')