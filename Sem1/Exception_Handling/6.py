#Age validation 

age = 15

try:
    if age < 18:
        raise ValueError("You must be 18 years or older") #this error has been raised by us 
    print("eligible")


except ValueError as e:
    print("Error", e) #cannot accept string
    
else:
    print("Access granted")

