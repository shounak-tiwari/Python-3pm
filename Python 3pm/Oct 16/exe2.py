
no1 = int(input("enter the value of number 1 : "))
no2 = int(input("enter the value of number 2 : "))

# print(no1//no2)
try:
    import prabhu # type: ignore
   
    print(no1//no2)

except ModuleNotFoundError as e :
    print(e)

except:
    print("Error found in somewhere in try block")