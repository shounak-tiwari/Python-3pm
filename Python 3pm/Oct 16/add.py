import py_compile

py_compile.compile('add.py')
num1 = input("Enter the value of number 1 : ")

num2 = input("Enter the value of number 2 : ")

Add = num1+num2

print(f"The sum of {num1} and {num2} is {Add}")


py_compile.compile('add.py', cfile='add.pyc')