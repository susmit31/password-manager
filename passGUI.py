from tkinter import *
import sys, csv, pyperclip

fonty = ('georgia', 16)

# this is the callback function for button "Add"
def addToDB():
	site = str(add_siteEntry.get())
	user = str(add_userEntry.get())
	password = str(add_passEntry.get())
	date = str(add_dateEntry.get())
	newData = [site, user, password, date]
	
	with open('passes.csv','a') as csvFile:
		csvWriter = csv.writer(csvFile, delimiter=",",quotechar='\"', quoting = csv.QUOTE_MINIMAL)
		csvWriter.writerow(newData)
		
	# checking if new data have been added
	with open('passes.csv',newline='') as csvFile:
		csvReader = csv.reader(csvFile)
		csvList = []
		for row in csvReader:
			csvList.append(row)
		if newData in csvList:
			add_statLabel.configure(text="Data added successfully", bg ='mediumseagreen')
		 
# this is the callback function of the Get button
def getFromDB():
	site = str(get_siteEntry.get())
	
	for i in range(3):
		get_statLabel[i].configure(text='')
		
	try:
		with open('passes.csv',newline='') as csvFile:
			siteData = []
			csvReader = csv.reader(csvFile)
			
			for row in csvReader:
				if row:
					if row[0] == site:
						siteData.append(row)
			
			if len(siteData)<4:
				j = 0
				for i in range(len(siteData)):
					get_statLabel[j].configure(text='Username: {};\nPassword: {}; \nDate added: {}'.format(siteData[i][1], siteData[i][2], siteData[i][3], font=fonty))
					j+=1
			else:
				j = 0
				for i in range(len(siteData)-2, len(siteData)):
					get_statLabel[j].configure(text='Username: {}; Password: {}; Date added: {}'.format(siteData[i][1], siteData[i][2], siteData[i][3], font=fonty))
					j+=1
				
	except FileNotFoundError:
		get_statLabel.configure(text = 'The password file can not be found!')
		
# creating the screen		
root = Tk()	
root.title('Password manager v1.0')

# creating frames
addFrame = Frame()
addFrame.grid(row = 0, column = 0)
getFrame = Frame()
getFrame.grid(row = 0, column = 1)

# creating add labels
add_title = Label(addFrame, text='Add new data', font=('georgia',24,'bold'), bg = 'aqua')
add_siteLabel = Label(addFrame, text = 'Site name: ', font = fonty, height = 4)
add_userLabel = Label(addFrame, text='Username: ' , font = fonty, height = 4)
add_passLabel = Label(addFrame, text = 'Password: ', font = fonty, height = 4)
add_dateLabel = Label(addFrame, text='Date added: ', font = fonty, height = 4)
add_statLabel = Label(addFrame, font = fonty, height = 4)

# creating add entries
add_siteEntry = Entry(addFrame,  font = fonty, width = 25)
add_userEntry = Entry(addFrame, font = fonty, width = 25)
add_passEntry = Entry(addFrame, font = fonty, width = 25)
add_dateEntry = Entry(addFrame, font = fonty, width = 25)

# creating add button
addButton = Button(addFrame, text='Add to database', font = fonty, command = addToDB)

# gridding the add labels
add_title.grid(row = 0, column = 0, columnspan = 40)
add_siteLabel.grid(row = 1, column = 0)
add_userLabel.grid(row = 2, column = 0)
add_passLabel.grid(row = 3, column = 0)
add_dateLabel.grid(row = 4, column = 0)
add_statLabel.grid(row = 6, column = 0, columnspan = 40)

# gridding the add entries
add_siteEntry.grid(row = 1, column = 1)
add_userEntry.grid(row = 2, column = 1)
add_passEntry.grid(row = 3, column = 1)
add_dateEntry.grid(row = 4, column = 1)

# gridding the add button
addButton.grid(row = 5, column = 0, columnspan = 40)

# creating get labels
get_title = Label(getFrame, text='Retrieve password', font = ('georgia',24, 'bold'), bg='aqua')
get_siteLabel = Label(getFrame, text='Enter the name of the site:', font = fonty, height = 4)
get_statLabel = [0]*3
for i in range(3):
	get_statLabel[i]= Label(getFrame, font = fonty)

# creating get entries
get_siteEntry = Entry(getFrame, font = fonty, width = 25)

# creating get button
getButton = Button(text='Get data for this site', font = fonty, command = getFromDB)

# gridding get labels
get_title.grid(row=0, column = 1, columnspan = 40)
get_siteLabel.grid(row = 1, column = 1)
for i in range(3):
	get_statLabel[i].grid(row = 3+i, column = 1, columnspan = 40)

# gridding get entries
get_siteEntry.grid(row = 1, column = 2)

# gridding get button
getButton.grid(row = 7, column = 1, columnspan = 40)

root.mainloop()