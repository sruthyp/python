lis = []
num = int(input('How many numbers: '))
for n in range(num):
    numbers = int(input('Enter number '))
    lis.append(numbers)

print( "Minimum element in the list is :", min(lis))
