#Age validation 

class InvalidAgeError(Exception):
    pass

try:
    age = 15 
    if age < 18:
        raise ValueError("You must be 18 years or older") #this error has been raised by us 
    print("eligible")

except ValueError as e:
    print("Error", e) #cannot accept string
    
else:
    print("Access granted")

finally:
    print("printing")


#no differece in output 