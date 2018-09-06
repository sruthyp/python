def countd(a):
	print(a+1)
def main():
	try:
		a=int(input())
		countd(a)
	except:
		print('invalid')
main()
