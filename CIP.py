#MODULE#
import urllib2,sys

if sys.platform in ["linux","linux2"]:
	W = ("\033[0m")
	G = ("\033[32;1m")
	R = ("\033[31;1m")
else:
	W = ("")
	G = ("")
	R = ("")

#FUNCTION#
def multi():
	try:
		req = "http://bot.whatismyipaddress.com"
		urllib2.Request(req)
		response = urllib2.urlopen(req)
		content = response.read()
		print ("\x1bc")
		print (R+"-----------------------------")
		print (G+"Check IPv4 & IPv6").center(35)
		print (R+"-----------------------------")
		print (G+"\nMy IPv4 & IPv6 : "+R),content
		print ("")
	except:
		print ("\x1bc")
		print (R+"-----------------------------")
		print (G+"Check IPv4 & IPv6").center(35)
		print (R+"-----------------------------")
		print (R+"\nMy IPv4 & IPv6 : not found\n")
def ipvFour():
	try:
		req = "http://ipv4bot.whatismyipaddress.com"
		urllib2.Request(req)
		response = urllib2.urlopen(req)
		content = response.read()
		print ("\x1bc")
		print (R+"-----------------------------")
		print (G+"Check IPv4 Only").center(35)
		print (R+"-----------------------------")
		print (G+"\nMy IPv4 : "+R),content
		print ("")
	except:
		print ("\x1bc")
		print (R+"-----------------------------")
		print (G+"Check IPv4 Only").center(35)
		print (R+"-----------------------------")
		print (R+"\nMy IPv4 : not found\n")
def ipvSix():
	try:
		req = "http://ipv6bot.whatismyipaddress.com"
		urllib2.Request(req)
		response = urllib2.urlopen(req)
		content = response.read()
		print ("\x1bc")
		print (R+"-----------------------------")
		print (G+"Check IPv6 Only").center(35)
		print (R+"-----------------------------")
		print (G+"\nMy IPv6 : "+R),content
		print ("")
	except:
		print ("\x1bc")
		print (R+"-----------------------------")
		print (G+"Check IPv6 Only").center(35)
		print (R+"-----------------------------")
		print (R+"\nMy IPv6 : not found\n")
def menu():
	try:
		print (R+"-----------------------------")
		print (G+"[1] IPv4 & IPv6 [2] IPv4 Only")
		print (G+"[3] IPv6 Only   [4] Exit")
		print (R+"-----------------------------")
		print (G+"Coded : GH057.ID | v1.0")
		print (R+"-----------------------------")
		print (R+"Find Me :")
		print (G+"http://fb.me/leemrtnzz\nhttp://t.me/leemrtnzz")
		print (R+"-----------------------------")
		menu = input(W+"Input menu : ")
		if menu > 4:
			print ("Menu not found")
		elif menu == 1:
			multi()
		elif menu == 2:
			ipvFour()
		elif menu == 3:
			ipvSix()
		elif menu == 4:
			print (R+"\n[!] Good Bye! [!]\n")
			exit()
		else:
			pass
	except NameError:
		pass
	except SyntaxError:
		pass
if __name__ == "__main__":
	while(True):
	 menu()