import threading
import queue
import time
import random

q = queue.Queue(maxsize=5)

def producer():
    for i in range(10):
        item = random.randint(1, 100)
        q.put(item)
        print(f"Produced {item}")
        time.sleep(0.5)

def consumer():
    while True:
        item = q.get()
        print(f"Consumed {item}")
        q.task_done()
        time.sleep(1)

t1 = threading.Thread(target=producer)
t2 = threading.Thread(target=consumer, daemon=True)

t1.start()
t2.start()
t1.join()