
n=int(input("enter the range to find prime no"))
for i in range(1,n+1):
    count=0
    for j in range(1,i+1):
        if (i%j==0):
            count=count+1
    if (count==2):
        print(i)