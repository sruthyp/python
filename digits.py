try:
	n=int(input("Enter the numbers:"))
	sum=0
	while(n!=0):
		rem=n%10
		sum+=rem
		n=n//10
	print(sum)
except:
    print('invalid')
