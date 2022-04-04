import sys
name=input("Enter ur name ")
code=int(input("Enter ur Id(code) ") )
grade=input("Enter ur grade ")
bsal=int(input("Enter ur basic salary "))
tax=0
if grade=='A':
	ma,ea=5000,4000
elif grade=='B':
	ma,ea=4000,3000
elif grade=='C':
	ma,ea=2500,1000
elif grade=='D':
	ma,ea=1500,800
else :
	print("Enter your correct grade")
	sys.exit(0)

peark=ma+ea

da=0.55*bsal
hr=0.35*bsal

gsal=bsal+peark+da+hr

if gsal<250000:
	print("U donot require to pay the tax")
elif gsal>=250000 and gsal<500000:
	tax=gsal*0.5
elif gsal>=500000 and gsal<700000:
	tax=gsal*0.10
elif gsal>=700000 and gsal<1000000:
	tax=gsal*0.15
else :
	tax=gsal*0.25

netsal=gsal+tax
print()
print("Epmloyees name: ",name)
print("Epmloyee Id(code): ",code)
print("Employees Gross Salary: ",gsal)
print("Tax to be payed by employee: ",tax)
print("Employees net salary: ",netsal)