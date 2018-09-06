def main():
	try:
		c=0
		k=0
		a=input()
		for i in a:
			if i.isalpha():
				c=c+1
			elif i.isnumeric():
				k=k+1
		if c+k==len(a) and c>0 and k>0:
			print('yes')
		else :
			print('no')
	except:
		print('invalid')
main()
