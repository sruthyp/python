a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
print("before swapping\na=", a, " b=", b)
 
a = a ^ b;
b = a ^ b;
a = a ^ b;
print("\nafter swapping\na=", a, " b=", b)
