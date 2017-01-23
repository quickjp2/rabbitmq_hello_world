import pika, time

# Callback function
def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    time.sleep(body.count(b'.'))
    print(" [x] Done")
    ch.basic_ack(delivery_tag = method.delivery_tag)

# Establish a connection
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Check and/or create queue
channel.queue_declare(queue='task_queue', durable=True)

# Add for fair dispatch; count is how many un-ack-ed messages
channel.basic_qos(prefetch_count=1)

# Register as a listener
channel.basic_consume(callback, queue='task_queue')

# Wait for messages
print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
