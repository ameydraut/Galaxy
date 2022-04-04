name=input("enter ur name ")
account_no=int(input("Enter ur account number "))
gender=input("Enter ur gender (male/female) ")
age=int(input("Enter ur age "))
balance=int(input("Enter the balance in ur account "))

if age>=60:
	interest_amount=balance*0.7
else:
	if gender=='male':
		interest_amount=balance*0.5
	elif gender=='female':
		interest_amount=balance*0.6
	else:
		print("Enter ur gender correctly")
total_balance=balance+interest_amount
print("Account Number ",account_no)
print("Account holder name ",name)
print("your gender ",gender)
print("your age ",age)
print("interest amount ",interest_amount)
print("Total balance ",total_balance)