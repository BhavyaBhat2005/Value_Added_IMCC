#instead of using generic except, we specify the exception we want to handle 


print("This is a program to get result") #cannot divide by zero

try:
    num = int(input("Enter a number"))
    result = 100 / num
    print("Result", result)

finally:
    print("This is mandatory block") #will execute each time 
    


    #this inputs a number from user to divide by. string and 0 won't be accepted and will give error. else only executes when there is a valid number entered. Will get executed each time.
    #program will run even without except block with finally, but if there is an exception then it will not get handled 