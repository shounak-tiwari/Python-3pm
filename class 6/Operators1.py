#conditional operators 

#enter the age of user and check it is eligible for vote or not 

age = float(input("Enter the age of user  : "))

result = (age >18)

# what is the type of object result ?? 
# boolean 

print(f"The type of object result is : {type(result)}")


print(f"User can vote in age of {age} :  {result}")