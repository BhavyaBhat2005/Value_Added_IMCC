#instead of using generic except, we specify the exception we want to handle 


print("This is a program to get result") #cannot divide by zero

try:
    num = int(input("Enter a number"))
    result = 100 / num
    print("Result", result)

except ValueError:
    print("Please enter a valid number") #cannot accept string
    
except ZeroDivisionError:
    print("You cannot divide by zero") #cannot divide by zero

else:
    print("Program executed successfully") 

    #this inputs a number from user to divide by. string and 0 won't be accepted and will give error. else only executes when there is a valid number entered.