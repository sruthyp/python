val = int(input("Enter a number: "))

factorial = 1

if val < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif val == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,val + 1):
       factorial = factorial*i
   print("The factorial of",val,"is",factorial)
