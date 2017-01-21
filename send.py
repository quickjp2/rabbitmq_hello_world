import pika

# Establish a connection
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Check and/or create queue
channel.queue_declare(queue='hello')

# Send a message
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')
print(" [x] Sent 'Hello World!'")

# Close the connectoin
connection.close()
