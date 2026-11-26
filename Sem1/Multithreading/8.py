import threading

def greet(name,age):
    print("Hello", name, "\nAge", age)

t1 = threading.Thread(target=greet, args=("Aarav", "21"))
t1.start()
t1.join()