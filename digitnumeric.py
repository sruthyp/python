def countd(a):
	c=0
	while(a!=0):
		a//=10
		c+=1
	print(c)
def main():
	try:
		a=int(input())
		countd(a)
	except:
		print('invalid')
main()
