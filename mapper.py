class Mapper():

	def __init__(self, path):
		self.path = path

		# Use a+ to create the file if it does not exist; Seek(0) to reset to the beginning for reading
		f = open(path, 'a+')
		f.seek(0)

		self.map = {}

		for line in f:
			data = line.split(":")
			self.map[data[0]] = data[1].rstrip()
		f.close()

	def add(self, discord, UUID):

		UUID = Mapper.format_UUID(UUID)

		# If the user is already registered, abort
		if discord in self.map.keys():
			return False
		if UUID in self.map.values():
			return False

		# Else, add the user to the file
		f = open(self.path, 'a+')
		f.write(discord+":"+UUID+"\n")
		f.close()

		# Then add them to the active map
		self.map[discord] = UUID

		return True

	def get_UUID(self, discord):

		if discord in self.map.keys():
			return self.map[discord]
		else:
			return None

	def format_UUID(UUID):
		return UUID[0:8] + "-" + UUID[8:12] + '-' + UUID[12:16] + '-' + UUID[16:20] + '-' + UUID[20:32]

if __name__ == "__main__":
	mapper = Mapper("F:\\servers\\minecraft\\Regis Minecraft Server Modded\\Pixelmon EVIV\\map.txt")
	print(mapper.map)



