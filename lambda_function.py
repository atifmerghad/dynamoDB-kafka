from __future__ import print_function

import json
import boto3
from kafka import KafkaProducer
import urllib
import ssl
import logging

root = logging.getLogger()
if root.handlers:
    for handler in root.handlers:
        root.removeHandler(handler)
logging.basicConfig(format='%(asctime)s %(message)s',level=logging.DEBUG)

print('Loading function')


context = ssl.create_default_context()
context.options &= ssl.OP_NO_TLSv1
context.options &= ssl.OP_NO_TLSv1_1

producer = KafkaProducer(
   bootstrap_servers=['botstrap-server-address:9092'],
   value_serializer=lambda m: json.dumps(m).encode('ascii'),
   retry_backoff_ms=500,
   request_timeout_ms=20000,
   security_protocol='SASL_SSL',
   sasl_mechanism='PLAIN',
   ssl_context=context,
   sasl_plain_username='user',
   sasl_plain_password='password')


def lambda_handler(event, context):
        
    print("Received event: " + json.dumps(event, indent=2))

    # Get the object from the event and show its content type
    record = event['Records'][0]
    eventName = record['eventName']
    newImage = record['dynamodb']['NewImage']
    
    try:
        print("We have new object. In DynamoDB {}, with eventName {}".format(newImage, eventName))
        future = producer.send("dynamoDB","We have new object. In DynamoDB {}, with eventName {}".format(newImage, eventName))
        record_metadata = future.get(timeout=10)
        print("sent event to Kafka! topic {} partition {} offset {}".format(record_metadata.topic, record_metadata.partition, record_metadata.offset))

    except Exception as e:
        print(e)
        print('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(eventName, newImage))
        raise e

