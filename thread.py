from multiprocessing import cpu_count
from multiprocessing import Process, Queue
import time
import requests

class MyProcess(Process):
    def __init__(self):
        Process.__init__()
print(cpu_count())

