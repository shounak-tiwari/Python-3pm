basic_Salary = float(input("Enter the basic salary  : "))

house_rent =  (2.5 * basic_Salary)/100

dearness_allowance = (4.8*basic_Salary)/100

gross = house_rent + dearness_allowance +basic_Salary

print(gross)
