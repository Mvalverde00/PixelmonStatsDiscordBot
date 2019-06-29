# https://nbtparse.readthedocs.io/en/latest/nbtparse.semantics.html#module-nbtparse.semantics
# See the above for clarification on how to use the library

from nbtparse.semantics.filetype import NBTFile
from nbtparse.semantics.fields import ByteField
from nbtparse.semantics.fields import ShortField
from nbtparse.semantics.fields import UnicodeField

class Reader():

	def __init__(self, root):
		self.root = root


	def get_poke_stats(self, fname, num):
		player_data = self.read(fname)

		poke_data = Reader.read_poke(player_data, num)

		return [UnicodeField.to_python(poke_data['Name']), Reader.get_IVs(poke_data), Reader.get_EVs(poke_data)]


	def get_IVs(data):

		tags = ["IVHP", "IVAttack", "IVDefence", "IVSpeed", "IVSpAtt", "IVSpDef"]

		return [ByteField.to_python(data[tags[i]]) for i in range(len(tags))]

	def get_EVs(data):
		tags = ["EVHP", "EVAttack", "EVDefence", "EVSpeed", "EVSpecialAttack", "EVSpecialDefence"]

		return [ShortField.to_python(data[tags[i]]) for i in range(len(tags))]


	# Given a player's data dict, return a dict describing a specific pokemon in their party,
	# Where 1 is the first pokemon in their party and 6 is the last
	def read_poke(data, num):
		stub = "party"

		stub += str(num-1) # Pokemon are internally indexed 0-5, so we subtract by one

		return data[stub]


	def read(self, fname):
		path = self.root + fname

		f = open(path, 'rb')

		(rn, nbt) = NBTFile.load(f)

		f.close()

		data = nbt.__dict__['data']

		return data



if __name__ == "__main__":
	r = Reader("F:\\servers\\minecraft\\Regis Minecraft Server Modded\\world\\pokemon\\")


	stats = r.get_poke_stats("c66b094d-890a-4117-b00b-84ebe030b86c.pk", 1)

	print(stats)
