import pika

# Callback function
def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

# Establish a connection
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Check and/or create queue
channel.queue_declare(queue='hello')

# Register as a listener
channel.basic_consume(callback, queue='hello', no_ack=True)

# Wait for messages
print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
