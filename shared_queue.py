import ctypes
from ctypes import c_char_p
import os

# Construct the path to the DLL within the package
dll_path = os.path.join(os.path.dirname(__file__), 'libs', 'SharedQueue.dll')

# Carregar a DLL
shared_queue_dll = ctypes.CDLL(dll_path)

# Definir as assinaturas das fun��es
enqueue = shared_queue_dll.enqueue
enqueue.argtypes = [c_char_p, c_char_p]
enqueue.restype = None

dequeue = shared_queue_dll.dequeue
dequeue.argtypes = [c_char_p]
dequeue.restype = c_char_p

# Fun��es wrapper em Python
def enqueue_message(queue_name, message):
    if isinstance(queue_name, str):
        queue_name = queue_name.encode('utf-8')
    if isinstance(message, str):
        message = message.encode('utf-8')
    enqueue(queue_name, message)

def dequeue_message(queue_name):
    if isinstance(queue_name, str):
        queue_name = queue_name.encode('utf-8')
    result = dequeue(queue_name)
    if result is not None:
        return result.decode('utf-8')
    return None

# Enqueue messages into different queues
enqueue_message('Queue1', 'Message for Queue 1')
enqueue_message('Queue2', 'Message for Queue 2')

# Dequeue messages from the queues
message1 = dequeue_message('Queue1')
message2 = dequeue_message('Queue2')
print(f'Received from Queue1: {message1}')
print(f'Received from Queue2: {message2}')