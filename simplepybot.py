import sys
import socket
import string
import ssl

def irc_parser():
	return dict()

#HOST="irc.mzima.net"
#PORT=6667
HOST="irc.ipv4.paraphysics.net"
PORT=6697
NICK="simplepybot"
IDENT="simplepybot"
REALNAME="simplepybot"
readbuffer=""

s=socket.socket( )

s=ssl.wrap_socket(s)

s.connect((HOST, PORT))
s.send("NICK %s\r\n" % NICK)
s.send("USER %s %s bla :%s\r\n" % (IDENT, HOST, REALNAME))

inloop = True
while inloop:
	readbuffer=readbuffer+s.recv(1024)
	temp=string.split(readbuffer, "\n")
	readbuffer=temp.pop( )

	for line in temp:
		line=string.rstrip(line)
		line=string.split(line)
		print line
		if(line[0]=="PING"):
			s.send("PONG %s\r\n" % line[1])
		elif(line[1]=="PRIVMSG"):
			if line[2] == NICK:
				s.send("PRIVMSG %s :sup doc\r\n" % line[0][1:].split('!',1)[0])
			if line[3] == ":join" and line[4]:
				s.send("JOIN %s\r\n" % line[4])
			elif line[3] == ":quit":
				s.send("QUIT :Gone to have lunch\r\n")
				s.close()
				inloop = False
