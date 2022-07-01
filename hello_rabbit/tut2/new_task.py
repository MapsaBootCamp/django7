#!/usr/bin/env python
import json
import pika
import sys

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)

message = ' '.join(sys.argv[1:])

if message:
    channel.basic_publish(
        exchange='',
        routing_key='task_queue',
        body=message,
        properties=pika.BasicProperties(
            delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE,
        ))
    print(" [x] Sent %r" % message)
else:
    data = {
        "payam": "salam",
        "sleep_time": 12
    }
    channel.basic_publish(
        exchange='',
        routing_key='task_queue',
        body=json.dumps(data),
        properties=pika.BasicProperties(
            delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE,
            content_type='application/json', 
        ))
    print(f" [x] Sent json data: {data}")

connection.close()