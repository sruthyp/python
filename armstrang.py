low = int(input("Enter low range: "))
high = int(input("Enter high range: "))
 
for num in range(low,high + 1):
   
   sum = 0
 
   
   temp = num
   while temp > 0:
       digit = temp % 10
       sum += digit ** 3
       temp //= 10
 
   if num == sum:
       print(num)
