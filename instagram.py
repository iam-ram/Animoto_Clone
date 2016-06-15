import re
import os
import urllib

fo = open("bieber", "rw+")
f =  open("url", "rw+")
out=[]
url = " "
count = 0 
k = []
for i in fo:
	k =  re.findall("(?P<url>https?://[^\s]+)", i)
	print k
        for i in k:
		i = i[:-2]
		#url = str("wget") + " " + "-O" + " " + str(count) + " " +  i 
		url = str("wget") + " " + "-P" + " " + "fashion" + " " +  i
		print url
		count = count + 1
	for item in k:
		ite = item[:-2]		
		print ite
  		f.write(ite)
		f.write('\n')

