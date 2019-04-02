import socket
import sys

class twbot:
	def __init__(self, name, passwd, channel):
		self.name = name
		self.passwd = passwd
		self.channel = channel
		self.port = 6667
		self.host = 'irc.twitch.tv'
		self.socket = None
		self.MODT = False

	def Send_message(self, message):
		self.socket.send(("PRIVMSG #"+ self.channel +" :" + message + "\r\n").encode())

	def Banplayer(self, username, time=None):
		if time is None:
			self.Send_message(".timeout " + username)
			self.Send_message("User : "+username+" foi banido do canal.")
		else:
			self.Send_message(".timeout " + username + " " + str(time))
			self.Send_message("User : "+username+" foi banido do canal por "+str(time)+" segundos.")
	
	def Alo(self, username):
			self.Send_message(username + ", ALOOOOOOOOO")

	def Listen(self):
		readbuffer = ''
		if self.socket != None:
			s = self.socket
			readbuffer = readbuffer + s.recv(1024).decode()
			temp = readbuffer.split("\n")
			readbuffer = temp.pop()
			for line in temp:
				print(line)
				if (line.split()[0] == "PING"):
					s.send(("PONG "+ line.split()[1] + "\r\n").encode())
				else:
					parts = line.split(":")
					if "QUIT" not in parts[1] and "JOIN" not in parts[1] and "PART" not in parts[1]:
						try:
							message = parts[2][:len(parts[2]) - 1]
						except:
							message = ""
						username = parts[1].split("!")[0]
						if self.MODT:
							print (username + ": " + message)
							if message.lower() == "alo":
								self.Alo(username)
							
							if (username == "mistertag") or (username == "trecuu"):
								if message.split()[0] == "!ban123":
									if len(message.split()) == 3:
										self.Banplayer(message.split()[-2],message.split()[-1])
									if len(message.split()) == 2:
										self.Banplayer(message.split()[-2])
								elif message.split()[0] == "!botquit":
									self.Send_message(" Bot vazando! Flw vlw!")
									self.socket.close()
									print("Bot Disconected!!!")
									sys.exit()

						for l in parts:
							if "End of /NAMES list" in l:
								self.MODT = True
		else:
			print("Bot not CONNECTED! (try Connect())")	

	def Connect(self):
		s = socket.socket()
		s.connect((self.host, self.port))
		s.send(("PASS " + self.passwd  + "\r\n").encode())
		s.send(("NICK " + self.name    + "\r\n").encode())
		s.send(("JOIN #" + self.channel + "\r\n").encode())
		self.socket = s



#testing
oauth = open("oauth.txt","r")
oauth = oauth.read()

bot = twbot("trecuu",oauth,"trecuu")

bot.Connect()

while True:
	bot.Listen()

#testing
