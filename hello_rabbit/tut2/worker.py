#!/usr/bin/env python
import json
import pika
import time

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)
print(' [*] Waiting for messages. To exit press CTRL+C')


def callback(ch, method, properties, body):
    # print("ch: \n", ch.__dict__)
    # print("++++++++++++++++++++++++++++++")
    # print("method: \n", method.__dict__)
    # print("++++++++++++++++++++++++++++++")
    # print("properties: \n", properties.__dict__)
    # print("++++++++++++++++++++++++++++++")
    # print("body: \n", body)
    if properties.content_type == 'application/json':
        data = json.loads(body)
        print(" [x] Received %r" % data.get("payam"))
        time.sleep(data.get("sleep_time", 5))
    else:
        print(" [x] Received %r" % body.decode())
        time.sleep(body.count(b'.'))
    print(" [x] Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='task_queue', on_message_callback=callback)

channel.start_consuming()