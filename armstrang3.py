value = int(input("Enter a number: "))  
sum = 0  
temp = value 
  
while temp > 0:  
   digit = temp % 10  
   sum += digit ** 3  
   temp //= 10  
  
if value == sum:  
   print(value,"is an Armstrong number")  
else:  
   print(value,"is not an Armstrong number")  
