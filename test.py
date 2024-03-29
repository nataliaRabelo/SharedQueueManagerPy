from SharedMemoryQueue import enqueue_message, dequeue_message

# Enqueue messages into different queues
enqueue_message('Queue1', 'Message for Queue 1')
enqueue_message('Queue2', 'Message for Queue 2')

# Dequeue messages from the queues
message1 = dequeue_message('Queue1')
message2 = dequeue_message('Queue2')
print(f'Received from Queue1: {message1}')
print(f'Received from Queue2: {message2}')