import boto.dynamodb
import os
import time
from boto.sqs.message import Message
#Accesing dynamoDB 
conn = boto.dynamodb.connect_to_region(
        "us-west-2",
        aws_access_key_id  = 'AKIAIVVL3QK5VFBA2DTQ',
        aws_secret_access_key = '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')
conn.list_tables()
message_table_schema = conn.create_schema(
        hash_key_name='jobid',
        hash_key_proto_value=str,
    )
#connecting to table
table = conn.get_table('f1111')
import os

import boto.sqs
conn = boto.sqs.connect_to_region(
        "us-west-2",
        aws_access_key_id  = 'AKIAIVVL3QK5VFBA2DTQ',
        aws_secret_access_key = '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')
)
#Creating the queue object
my_queue = conn.get_queue('test')
reverse = conn.get_queue('Reverse')
m =  my_queue.get_messages(1)
start = time.time()
f = open("url",'w')
count = 0
while (len(m) > 0):
	k = m[0].get_body()
	#print k
	l = k.split(':::')
	#print l[1]
	try:
#	   print l[0]
	   table.get_item(hash_key=l[0])
	except  boto.dynamodb.exceptions.DynamoDBKeyNotFoundError:
	#Pulling of SQS Messages
	   data={'value': l[1]}
	   m1=Message()
	   m1.set_body(k[0]+" "+"T")
	   reverse.write(m1)
	   item = table.new_item(hash_key = l[0],attrs=data)
	   item.put()
	   my_queue.delete_message(m[0])

	   f.write(l[1])
        m=my_queue.get_messages(1)
last = time.time()

f1 =  open("final_url",'r')
for i in f1:
	#Downloading the images
	wgeturl  = "wget" + " " + "-O" + " " + " " + "image" + str(count) + ".jpg" + " " + str(i) 
	print wgeturl
	count = count + 1
	os.system(wgeturl)

#Creating images
os.system("ffmpeg -framerate 1 -pattern_type glob -i '*.jpg' -c:v libx264 out.mp4")

print "Time of Execution"
print last - start