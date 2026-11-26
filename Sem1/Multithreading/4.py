import threading
import time

def greet1():
    time.sleep(2)
    print("hello from thread1")


def greet2():
    print("hello from thread2")

def greet3():
    print("hello from thread3")

t1=threading.Thread(target=greet1)
t2=threading.Thread(target=greet2)
t3=threading.Thread(target=greet3)
t1.start()
t2.start()
t3.start()
