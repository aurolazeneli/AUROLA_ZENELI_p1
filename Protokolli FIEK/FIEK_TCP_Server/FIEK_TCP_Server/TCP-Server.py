import socket
import datetime
import random
from _thread import *

def IPADDRESS():
    return "Ip adresa juaj eshte %s" % addr[0]

def PORT():
    return "Porti juaj eshte %s" % addr[1]

def COUNT(req):
   numri=0
   zanore=['A','O','U','E','I']

   z = str(req[0:]).upper()
   for i in range (0, len(z)):
    if(z[i] in zanore):
       numri += 1
       bashketingellore=len(req)-numri
   return "Numri i zanoreve ne tekst eshte: ",numri ,"dhe numri i bashketingelloreve: ",bashketingellore 

def REVERSE(req):
 request=req.strip()
 stringlength=len(request) 
 requesting=request[stringlength::-1]
 return requesting


def PALINDROME(string):
	fromLeft = 0
	toRight = len(string) - 1
	
	while toRight >= fromLeft:
		if not string[fromLeft] == string[toRight]:
			return "False"
		fromLeft += 1
		toRight -= 1
	return "True"


