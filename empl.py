n=int(input("Gross salary of how many people do u want to count"))
for i in range(1,n+1):
	emp_id=int(input("Enter the employee id"))
	emp_level=input("Enter the employee level ")
	emp_name=input("Enter the enployee name")
	emp_bsal=int(input("Enter the basic sal of an employee"))

	ta=0
	ca=0

	if emp_level=='A':
		ta,ca=4000,6500
	elif emp_level=='B':
		ta,ca=3000,5500
	elif emp_level=='C':
		ta,ca=2000,4000
	elif emp_level=='D':
		ta,ca=1000,2000
	else:
		print("Enter the correct Grade")

	peark=ta+ca
	da=0.76*emp_bsal
	hr=0.35*emp_bsal

	emp_gsal=peark+da+hr+emp_bsal
	print("Employee name",emp_name)
	print("Employee Id",emp_id)
	print("Employee level",emp_level)
	print("Gross Salary of Employee",emp_gsal)