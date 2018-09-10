num = int(input('Enter the values: '))
sum = 0
for n in range(num):
    numbers = float(input('Enter number : '))
    sum += numbers
avg = sum/num
print('Average of ', num, ' numbers is :', avg)
