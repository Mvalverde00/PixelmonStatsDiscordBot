from discord.ext import commands
from mapper import Mapper
from reader import Reader

# To get UUID from minecraft username
import requests, time

bot = commands.Bot(command_prefix="!!")

mapper = Mapper("F:\\servers\\minecraft\\Regis Minecraft Server Modded\\Pixelmon EVIV\\map.txt")
reader = Reader("F:\\servers\\minecraft\\Regis Minecraft Server Modded\\world\\pokemon\\")

@bot.command()
async def check_poke(ctx, index):

	# Validate inpute
	try:
		index = int(index)
	except ValueError:
		await ctx.channel.send("Invalid index!  Not a Number!")
		return

	if index > 6 or index < 1:
		await ctx.channel.send("Invalid index!  Please enter a value 1-6 !")
		return


	#Check to make sure the user exists in map
	UUID = mapper.get_UUID(str(ctx.message.author))

	if UUID is None:
		await ctx.channel.send("You haven't registered your discord account to your minecraft account!  Please type !!register <minecraft username>")
		return

	stats = reader.get_poke_stats(UUID + ".pk", index)

	await ctx.channel.send("""Pokemon Name: {}\n
	============================
	Health, Speed IVs: {}, {}\n
	Attack, SpAtt IVs: {}, {}\n
	Defense, SpDef IVs: {}, {}\n
	============================
	Health, Speed EVs: {}, {}\n
	Attack, SpAtt EVs: {}, {}\n
	Defense, SpDef EVs: {}, {}\n
		""".format(stats[0], stats[1][0], stats[1][3], stats[1][1], stats[1][4], stats[1][2], stats[1][5],
							 stats[2][0], stats[2][3], stats[2][1], stats[2][4], stats[2][2], stats[2][5], ))

@bot.command()
async def register(ctx, mc_uname):
	server_check = requests.get("https://status.mojang.com/check")

	# Check that the server is online
	if server_check.status_code != 200:
		await ctx.channel.send("Sorry! The Mojang servers are down at the moment, so I could not register you.  Please try again later.")
		return

	# Check that api service is not offline	
	if server_check.json()[5]["api.mojang.com"] == "red":
		await ctx.channel.send("Sorry! The Mojang servers are down at the moment, so I could not register you.  Please try again later.")
		return

	# Get the response
	data = requests.get("https://api.mojang.com/users/profiles/minecraft/{}".format(mc_uname))

	# A blank byte string means no such username exists
	if data.content == b'':
		await ctx.channel.send("It seems you entered an invalid minecraft username.  Please check for typos and try again!")
		return

	# It exists!  Convert to json and get UUID
	data = data.json()
	UUID = data['id']

	# Try to add the info to the mapper
	if not mapper.add(str(ctx.message.author), UUID):
		await ctx.channel.send("Your discord account is already registered to a minecraft account, or vice versa!")
		return

	await ctx.channel.send("Successfully registered!")



bot.run("NTkzNjI4MjIzNTM1ODQxMzEx.XRQpjA.RU1A0kisdOxwJHIktOaf4NHKvzA")
