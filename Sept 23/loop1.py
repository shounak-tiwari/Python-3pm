# while loops 
# Write a program that prompts the user for a positive integer and then calculates the sum of all integers from 1 to that number. Use a while loop.

number = int(input("Enter the positive integer : "))

add = 0 
 
i = 1

while i<=number:
    add+=i

    i+=1

print(f"The sum of {number} : {add}") 