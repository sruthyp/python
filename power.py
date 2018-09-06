def main():
	try:
		s=0
		a=int(input())
		while(a!=0):
			a=a/2
			if a==1:
				s=1
				break
		if s!=1:
			print('no')
		else :
			print('yes')
	except:
		print('invalid')
main()
