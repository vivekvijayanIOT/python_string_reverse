a=raw_input("Enter the number")
b=int(a)
n=1
i=b-1
while(i>1):
	b=b*i
	i=i-1	
print "Factorial of %s is %d"%(a,b)
