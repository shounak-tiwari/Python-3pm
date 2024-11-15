number = int(input("Enter the number : "))

def fact(number):
	fact = 1
	i =1
	while i<=number:
		fact = fact*i
		i+=1
	print("Factorial of number : ",fact)


fact(number)
