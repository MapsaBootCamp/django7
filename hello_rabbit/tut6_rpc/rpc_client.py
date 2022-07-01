#!/usr/bin/env python
import sys
import pika
import uuid


class FibonacciRpcClient(object):

    def __init__(self):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost'))

        self.channel = self.connection.channel()

        result = self.channel.queue_declare(queue='', exclusive=True)
        self.callback_queue = result.method.queue

        self.channel.basic_consume(
            queue=self.callback_queue,
            on_message_callback=self.on_response,
            auto_ack=True)

        self.response = None
        self.corr_id = None

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body

    def call(self, n):
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(
            exchange='',
            routing_key='rpc_queue',
            properties=pika.BasicProperties(
                reply_to=self.callback_queue,
                correlation_id=self.corr_id,
            ),
            body=str(n))
        self.connection.process_data_events(time_limit=10)
        return int(self.response)


fibonacci_rpc = FibonacciRpcClient()

fibo_indx = sys.argv[1] if len(sys.argv) > 1 else 30
print(f" [x] Requesting fib({fibo_indx})")
response = fibonacci_rpc.call(fibo_indx)
if response is None:
    print("kheili tool keshid hal nadasht vaise")
else:
    print(" [.] Got %r" % response)