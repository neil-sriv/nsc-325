import nmap3
#nmap = nmap3.Nmap()
#nmap = nmap3.NmapScanTechniques()
nmap = nmap3.NmapHostDiscovery()

results = nmap.nmap_portscan_only('192.168.1.1/24', args='-O')

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
			print('Hostname: ' + results[i]['hostname'][0]['name'])

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

	ports_list = []
	for ports in results[i]['ports']:
		ports_list.append(ports['portid'])
	print('Ports: ' + str(ports_list))

	os = results[i]['osmatch']
	if os == []:
		print('OS information not found')
	
	else:
		print('OS guesses:')	
		if len(os) <= 3:
			pass
		else:
			os = os[:3]

		for guess in os:
			if guess == os[-1]:
				print('\tName of OS: ' + str(guess['name']))
				print('\tAccuracy: ' + str(guess['accuracy']))
				print('\tType: ' + str(guess['osclass']['type']))

			else:
				print('\tName of OS: ' + str(guess['name']))
				print('\tAccuracy: ' + str(guess['accuracy']))
				print('\tType: ' + str(guess['osclass']['type']))
				print()

	print()

print(results['runtime']['summary'])

#print(str(len(results) - 2) + ' devices found')