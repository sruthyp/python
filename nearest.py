def main():
	try:
		a=int(input("enter the value:-"))
		if a%2!=0:
			a-=1
		print(a)
	except:
		print('invalid')
main()
