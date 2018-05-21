import discord
from discord.ext import commands

TOKEN = ''
command_prefix = '?'
description = '''Geoffrey is an inside joke none of you will understand, at 
least he knows where your bases are.'''

bot = commands.Bot(command_prefix=command_prefix , description=description)

class Location:
	name = ''
	x = 0;
	y = 0;
	z = 0;
	
	def __init__(self,args) :
		self.name = args[0]
		self.x = int(args[1])
		self.y = int(args[2])
		self.z = int(args[3])

	def  posToStr(self) :
		return '(x=' + str(self.x) + ', y=' + str(self.y) + ', z=' + str(self.z) + ')' 
			
#Bot Commands ******************************************************************		
@bot.event
async def on_ready():
	print('GeoffreyBot')
	print('Username: ' + bot.user.name)
	print('ID: ' + bot.user.id)

@bot.command()
async def Geoffrey():
	'''Check if the bot is alive'''
	await bot.say('I\'m here, ding dong')

@bot.command(pass_context=True)
async def addBase(ctx, * args):
	if (len(args) == 4) :
		try:
			base = Location(args)
			await bot.say('{}, your base named {} located at {} has been added'
				'to the database.'.format(ctx.message.author.mention, base.name, base.posToStr()))
		except ValueError:
			await bot.say('Invalid syntax, try again (?addbase [name] [x coord] [z coord])')
			
	else :
		await bot.say('Allows you to add your base location to the database. '
			'Syntax: ?addbase [Base Name] [X Coordinate] [Z Coordinate]')

#Bot Startup ******************************************************************	
try :
	file = open('token.dat','r')
	TOKEN = file.read()	
except FileNotFoundError:
	print('token.dat not found.')
except IOError:
	print('Error reading token.dat')

bot.run(TOKEN)

	
