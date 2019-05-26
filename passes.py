# Simple password managing programme
# Takes site name, password, and the date this password was added
# Stores them in a csv spreadsheet

import csv, sys, pyperclip


if len(sys.argv) < 2:
	print("Please write the command as 'python passes.py add/get'")
	sys.exit()
	

if sys.argv[1] == 'get':
	#Getting site name
	site = input('Please enter the site: ')
	#Getting the password
	try:
		with open('passes.csv',newline='') as csvFile:
			csvReader = csv.reader(csvFile)
			for row in csvReader:
				if row:
					if row[0] == site:
						print('The password is: ' + row[1])
						pyperclip.copy(row[1])
						print('The password for '+ site + ' has been copied to clipboard')

	except FileNotFoundError:
		print("Error! File not found!")


elif sys.argv[1] == 'add':
	#Getting new data
	site = input('Please enter the site: ')
	pw = input('Please enter the password: ')
	date = input('Please enter the date this password was created: (write "forgot" if you don\'t remember) ')
	newEntry = [site, pw, date]
	
	#Appending new data to the password spreadsheet
	with open('passes.csv', 'a') as csvFile:
		csvWriter = csv.writer(csvFile, delimiter="," , quotechar='\"', quoting = csv.QUOTE_MINIMAL)
		csvWriter.writerow(newEntry)
			
	#Checking if new data have been added
	with open('passes.csv',newline = '') as csvFile:
		csvReader = csv.reader(csvFile)
		csvList = []
		for row in csvReader:
			csvList.append(row)
		if csvList[len(csvList) - 2] == newEntry:
			print('New data added successfully')
		else:
			print('Error!')
			

else:
	print('incorrect argument')
	sys.exit()
