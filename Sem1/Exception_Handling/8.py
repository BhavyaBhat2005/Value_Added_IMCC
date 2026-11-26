#Age validation 

class InvalidAgeError(Exception):
    pass

try:
    age = 15 
    if age < 18:
        raise ValueError("You must be 18 years or older") #this error has been raised by us 
    print("eligible")

finally:
    print("printing")


#checking the program without else and the exception 