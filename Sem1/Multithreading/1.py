import time

def task1():
    print("Task1 has started")
    time.sleep(2) 
    print("T1 completed")

def task2():
    print("Task1 has started")
    time.sleep(2)
    print("T2 completed")

task1()
task2()

#approx 2 seconds each program is taking for each, so total approx 4 seconds 
#currently it is waiting till the first executes and wasting time 
