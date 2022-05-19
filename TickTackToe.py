import discord
from discord.ext import commands
import os #protects the seceret tokens used to connect to discord
from dotenv import load_dotenv

class TickTackToe:
	def __init__(self):
		load_dotenv() #in order to pull from seceret tokens
		TOKEN = os.getenv('DISCORD_TOKEN') #in "Secrets" set DISCORD_TOKEN to bot token
		GUILD = os.environ['DISCORD_GUILD'] #in "Sevrets" set DISCORD_GUILD to guild name
		
		client = discord.Client() #this is what interacts with discord
		client = commands.Bot(command_prefix = '!') #Sets command key
		self.count = 0
		@client.event 
		async def on_ready(): 
			for guild in client.guilds:
				if guild.name == GUILD:
					print(f'{client.user} is connected to the following Guild:\n'f'{guild.name} (id:{guild.id})')
				try:
					client.run
				except Exception:
					client.login(TOKEN)
					client.run(TOKEN)
					
		@client.command()
		async def hello(txt):
			await txt.send('Hello!')

		@client.command()
		async def rules(txt):
			await txt.send('Rules of the game:`\n`1. Users should take turns (x plays then o plays).`\n`2. Play row (up and down) then collum (left and right).`\n`3. Only one game can be played at a time, but multiple people can play.`\n`4. Try to win. good luck :D')
			
		@client.command()
		async def newGame(txt):
			self.board = [["_", "_", "_"],["_", "_", "_"],["_", "_", "_"]]
			str = self.__str__()
			await txt.send(str)

		self._playX(client)
		self._playO(client)
	
		client.run(TOKEN)
		
	## working print function (returns a string of the proper output statement)
	def __str__(self):
		string = "`   1  2  3  `\n`"
		count = 0
		for r in range (len(self.board)):
			count += 1
			for c in range( len(self.board[r]) ):
				if(c == 0):
					string += str(count) + " "
				if (self.board[r][c] == "_"):
					string += " _ "
				else:
					string += " " + self.board[r][c] + " "
			# print(r)
			if(r < 2):
				string += " `\n`"
			else:
				string += " `"
		return (string)
	
	## MORE DISCORD + PYTHON API and COMMANDS
##https://www.codegrepper.com/code-	examples/python/discord.py+new+line+in+message
##player X place a marker
	
	def _playX(self, c): # c = client
		@c.command()
		async def xPlay(txt, row, col):
			if(self._isValid(row, col)):  ## +
				self.board[int(row)-1][int(col)-1] = "X"
				self.count = self.count + 1
				str = self.__str__() # automaticaly uses self.board
				if (self._checkWin()):
					await txt.send("X wins!")
					self.board = [["_", "_", "_"],["_", "_", "_"],["_", "_", "_"]]
					self.count = 0
				elif(self.count > 8):
					await txt.send("Scratch Game! ")
					self.board = [["_", "_", "_"],["_", "_", "_"],["_", "_", "_"]]
					self.count = 0
				await txt.send(str)
			else:
				await txt.send("Please put in valid values.")
			

	def _playO(self, c): # c = client
		@c.command()
		async def oPlay(txt, row, col):
			if(self._isValid(row, col)):  ## +
				self.board[int(row)-1][int(col)-1] = "O"
				self.count = self.count + 1
				str = self.__str__() # automaticaly uses self.board
				if (self._checkWin()):
					await txt.send("O Wins!")
					self.board = [["_", "_", "_"],["_", "_", "_"],["_", "_", "_"]]
					self.count = 0
				elif(self.count > 8):
					await txt.send("Scratch Game! ")
					self.board = [["_", "_", "_"],["_", "_", "_"],["_", "_", "_"]]
					self.count = 0
				await txt.send(str)
			else:
				await txt.send("Please put in valid values.")
			#
			

	def _isValid(self, r, c):
		if(int(r)-1 < 3 and int(r)-1 >= 0 and int(c)-1 < 3 and int(c)-1 >= 0 and self.board[int(r)-1][int(c)-1]  == "_"):
			return True
		return False

			
	def _checkWin(self):
        #check rows
			table = self.board
			for row in self.board:
				if (row[0] == row[1] and row[0] == row[2] and not row[0] == "_"):
					return True 
				#check cols
			for c in range(3):
				if(table[0][c] == table[1][c] and table[0][c] == table[2][c] and not table[0][c] == "_"):
					return True
				# check diagnols
			if ((table[0][0] == table[1][1] and table[0][0] == table[2][2] and not table[1][1] == "_") or (table[0][2] == table[1][1] and table[0][2] == table[2][0] and not table[1][1] == "_")):
				return True
			return False
	# client.run(TOKEN)