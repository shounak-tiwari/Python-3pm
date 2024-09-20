age = float(input("Enter the age  : "))

if age>=18:
	if age<=24:
		highsec = input("Press y for yes and n for no : ")
		highsec.lower()
		if highsec=='y':
			highper = float(input("Enter the 12th calss percentage  : "))
			if highper >=55.00:
				print("Yes ! your eligible for jee exam ")
			else:
				print("12th percetange is not matched from cri ")
			
		else:
			print("Complete your 12th calss first ")
		
	else:
		print("Sorry!! your are age is greator from 24")
	
else:
	print("Beta ! pahle 18 ka to ho jaa ")
