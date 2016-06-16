from boto.sqs.message import Message
import boto
import boto.dynamodb
import os
import time
from boto.sqs.message import Message
conn = boto.dynamodb.connect_to_region(
        "us-west-2",
        aws_access_key_id  = '*****************',
        aws_secret_access_key = '**************************')
message_table_schema = conn.create_schema(
        hash_key_name='jobid',
        hash_key_proto_value=str,
    )
table = conn.create_table(
        name='f1111',
        schema=message_table_schema,
        read_units=100,
        write_units=100
    )
