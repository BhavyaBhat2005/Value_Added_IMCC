import threading

lock = threading.Lock()

def task():
    lock.acquire()
    try:
        print("Inside locked section")
    finally:
        lock.release()