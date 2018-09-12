def rotate(n,k,l):
	a=[]
	for i in range(n-k,n):
		a.append(l[i])
	for i in range(n-k):
		a.append(l[i])
	print(a)
def main():
	try:
		n=int(input())
		k=int(input())
		l=[]
		for i in range(n):
			l.append(int(input()))
		rotate(n,k,l)
	except:
		print('invalid')
main()
