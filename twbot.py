import socket

class twbot:
	def __init__(self, name, passwd, channel):
		self.name = name
		self.passwd = passwd
		self.channel = channel
		self.port = 6667
		self.host = 'irc.twitch.tv'
		self.socket = ''

	def Send_message(self, message):
		self.socket.send(("PRIVMSG "+ self.channel +" :" + message + "\r\n").encode())

	def Banplayer(self, username, time=None):
		if time is None:
			self.Send_message(".timeout " + username)
			self.Send_message("User : "+username+" foi banido do canal.")
		else:
			self.Send_message(".timeout " + username + " " + str(time))
			self.Send_message("User : "+username+" foi banido do canal por "+str(time)+" segundos.")	
	
	def Alo(self, username):
			self.Send_message(username + ", VAI TUMA NO CU")


	def Listen(self):
		s = socket
		readbuffer = readbuffer + s.recv(1024).decode()
		temp = readbuffer.split("\n")
		readbuffer = temp.pop()
		for line in temp:
			if (line.split()[0] == "PING"):
				print (line)
				s.send(("PONG "+ line.split()[1] + "\r\n").encode())
			else:
				parts = line.split(":")
				if "QUIT" not in parts[1] and "JOIN" not in parts[1] and "PART" not in parts[1]:
					try:
						message = parts[2][:len(parts[2]) - 1]
					except:
						message = ""
					usernamesplit = parts[1].split("!")
					username = usernamesplit[0]
					if MODT:
						print (username + ": " + message)
						if message.lower() == "alo":
							self.Alo(username)
						if username == "macotv":
							if message.split()[0] == "!ban123":
								if len(message.split()) == 3:
									self.Banplayer(message.split()[-2],message.split()[-1])
								if len(message.split()) == 2:
									self.Banplayer(message.split()[-2])
					for l in parts:
						if "End of /NAMES list" in l:
							MODT = True



	def Connect(self):
		s = socket.socket()
		s.connect((self.host, self.port))
		s.send(("PASS " + self.passwd  + "\r\n").encode())
		s.send(("NICK " + self.name    + "\r\n").encode())
		s.send(("JOIN " + self.channel + "\r\n").encode())
		self.socket = s

#testing
bot = twbot("trecuu","oauth:SEGREDINHO","#macotv")
bot.name = "alo"
print(bot.host)


#testing
