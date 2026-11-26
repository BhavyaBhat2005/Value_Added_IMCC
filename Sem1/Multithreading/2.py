import threading

def greet1():
    print("hello from other thread")

t1=threading.Thread(target=greet1)

t1.start()
