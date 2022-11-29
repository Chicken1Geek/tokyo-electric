global db
db = []

def loadDatabase():
	global db
	db = []
	with open('users.txt','rt') as file:
		users = file.read().split('\n')
		for user in users:
			user = user.split(',')
			try:
				user[4] = int(user[4])
			except:
				pass
			db.append(user)

def writeDatabase():
	global db
	databaseDump = ''
	for user in db:
		userString = ''
		for i in user:
			if type(i) == int:
				userString += str(i) + ','
			else:
				userString += i + ','
		userString = userString.strip(',') + '\n'
		databaseDump += userString
	with open('users.txt','w') as file:
		file.write(databaseDump.strip('\n'))

def commit():
	writeDatabase()
	loadDatabase()

def createUser(id,name,contact,type,quota):
	global db
	db.append([id,name,contact,type,quota])
	commit()

def getUser(id):
	global db
	for user in db:
		if user[0] == id:
			return user

def updateUser(id,quota):
	global db
	user = getUser(id)
	userIndex = db.index(user)
	user[4] = quota
	db[userIndex] = user
	commit()
	
def deleteUser(id):
	global db
	db.remove(getUser(id))
	commit()
	
loadDatabase()