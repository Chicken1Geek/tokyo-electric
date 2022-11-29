import database as db

tariff = {'a':10,'b':20}

def ask(question):
	return input(question)

def updateUsage(id,quota):
	user = db.getUser(id)
	newQuota = user[4] + quota
	print('newquota',newQuota)
	db.updateUser(id,newQuota)
	
def calculateBill(id):
	user = db.getUser(id)
	usedQuota = user[4]
	userType = user[3]
	price = tariff[userType]
	bill = usedQuota * price
	return bill

def payBill(id):
	db.updateUser(id,0)

def newUserMenu():
	print('\nCreate New User Menu:')
	id = ask('Enter user Id: ')
	name = ask('Enter user name: ')
	contact = ask('Enter user contact: ')
	type = ask('Enter user type: ')
	try:
		db.createUser(id,name,contact,type,0)
		print('\nUser created.')
	except:
		print('There was an error trying to create the user. Please try again.')

def viewUserMenu():
	
	print('\nView User Menu:')
	id = ask('Enter a valid user id: ')
	try:
		user = db.getUser(id)
		print(f'\nUser Id: {user[0]}\nName: {user[1]}\nContact: {user[2]}\nType: {user[3]}\nCurrent quota used: {user[4]} kv/h \n')
	except:
		print('No user found with given id.')
		
def deleteUserMenu():
	print('\nDelete User Menu:')
	id = ask('Enter a valid User id: ')
	try:
		db.deleteUser(id)
		print('User Deleted')
	except:
		print('No user found with the id')

def updateUsageMenu():
	print('\nUpdate Usage Menu:')
	id = ask('Enter valid user Id: ')
	try:
		user = db.getUser(id)
		user[0]
	except:
		print('No user found with id')
	try:
		addQuota = int(ask('Enter usage: '))
	except:
		print('Enter a valid quota. Use only integers')
	try:
		updateUsage(id,addQuota)
	except Exception as e:
		print('Error adding quota')
		print(e)
	
def billingMenu():
	print('\nBilling menu:')
	id = ask('Enter a user Id: ')
	try:
		user = db.getUser(id)
		userName = user[1]
		userType = user[3]
		userQuota = user[4]
		print('\n\n')
		print(f'Billing for {userName}')
		print(f'User type: {userType}')
		print(f'Tariff : {tariff[userType]} ₹/Hour')
		print(f'Quota Used : {userQuota} kv/h')
		print(f'Total : ₹{calculateBill(id)}')
		print('\n')
		
		confirm = input('Do you want to mark this user paid? [y/n]: ').lower()
		if confirm == 'y':
			payBill(id)
		elif confirm == 'n':
			print('Payment cancelled.')
		else:
			print('Not a valid option try again.')
	except:
		print('No user found with id')

def menu():
	queries = ['b - Billing','u - Update usage','c - Create User','v - View User','d - Delete User']
	for query in queries:
		print(query)

def main():
	print('\nTokyo Electricity Board')
	menu()
	query = ask('Enter a option:  ').lower()
	if query == 'b':
		billingMenu()
	elif query == 'u':
		updateUsageMenu()
	elif query == 'c':
		newUserMenu()
	elif query == 'v':
		viewUserMenu()
	elif query == 'd':
		deleteUserMenu()
	else:
		print('Invalid query Try Again')
	
while True:
	main()