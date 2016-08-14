import string, random
def generate_room_name(active_rooms):
	has_name = False
	while not has_name:
		name = ''
		for i in range(4):
			name += string.ascii_uppercase[random.randrange(26)]
		if not name in active_rooms:
			has_name = True
			return name