import ctypes
from ctypes import c_char_p

# Carregar a DLL
shared_queue_dll = ctypes.CDLL('libs/SharedQueue.dll')

# Definir as assinaturas das funções
enqueue = shared_queue_dll.enqueue
enqueue.argtypes = [c_char_p, c_char_p]
enqueue.restype = None

dequeue = shared_queue_dll.dequeue
dequeue.argtypes = [c_char_p]
dequeue.restype = c_char_p

# Funções wrapper em Python
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