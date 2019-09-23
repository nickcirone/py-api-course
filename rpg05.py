#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

def showInstructions():
	# print a main menu and the commands 
	print('''
RPG Game
========
Commands:
	go [direction]
	get [item]
	quit
	''')

def showStatus():
	# print the player's current status
	print('----------------------')
	print('You are in the ' + currentRoom + '.')
	if rooms[currentRoom].get('north'):
		print(rooms[currentRoom].get('north') + ' is to the north.')
	
	if rooms[currentRoom].get('south'):
		print(rooms[currentRoom].get('south') + ' is to the south.')
	
	if rooms[currentRoom].get('east'):
		print(rooms[currentRoom].get('east') + ' is to the east.')

	if rooms[currentRoom].get('west'):
		print(rooms[currentRoom].get('west') + ' is to the west.')

	print('Inventory: ' + str(inventory))
	if "item" in rooms[currentRoom]:
		print('You see a ' + rooms[currentRoom]['item'] + '.')
	print('----------------------')

inventory = []

rooms = {
			'Hall': {
				'south': 'Kitchen',
				'east': 'Dining Room'
			},
			'Kitchen': {
				'north': 'Hall',
				'item': 'carrot'
			},
			'Dining Room': {
				'west': 'Hall',
				'item': 'fork'
			}
		}

currentRoom = 'Hall'

showInstructions()

while True:
	showStatus()

	move = ''
	while move == '':
		move = input('> ')

	move = move.lower().split()

	if move[0] == 'quit':
		print('Goodbye, thanks for playing!')
		break

	if move[0] == 'go':
		if move[1] in rooms[currentRoom]:
			currentRoom = rooms[currentRoom][move[1]]
		else:
			print("You cannot go that way!")

	if move[0] == 'get':
		if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item'].lower():
			inventory += [move[1]]
			print('Got ' + move[1] + '!')
			del rooms[currentRoom]['item']
		else:
			print('Cannot get ' + move[1] + '!')
