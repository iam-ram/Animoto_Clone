import os
import re
import sys

import boto.sqs
conn = boto.sqs.connect_to_region(
        "us-west-2",
        aws_access_key_id  = 'AKIAIVVL3QK5DFGJJKLNNGGH',
        aws_secret_access_key = 'Ea+F7rQ0OeGUKJ3f4VvMCmGGHJJKKLLL'
)


q = conn.create_queue('test')
reverse = conn.create_queue('Reverse')
print conn.get_all_queues()

#from boto.sqs.message import RawMessage
from boto.sqs.message import Message
m = Message()
fp = open('url','r')
count  = 1
for i in fp:
	print i
	str1 = str(count) + ":::" + str(i)
	m = Message()
	count =  count + 1
	m.set_body(str1)
	retval = q.write(m)
	print 'added message, got retval: %s' % retval
fp.close()

