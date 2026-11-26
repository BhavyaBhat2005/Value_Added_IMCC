#Age validation 

age = 15

try:
    if age < 18:
        raise ValueError("You must be 18 years or older") #this error has been raised by us 


except ValueError:
    print("Please enter a valid number") #cannot accept string
    
else:
    print("Access granted")

#If age is 15 then the "except" gets printed
#If age is more than 20 then "else" gets printed