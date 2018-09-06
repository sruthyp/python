
def countd(m,n):
	(max,min)=(0,9999)
	for i in range(n):
		if max<m[i]:
			max=m[i]
		if min>m[i]:
			min=m[i]
	print(min,max)
def main():
	try:
		m=[]
		n=int(input())
		for i in range(n):
			m.append(int(input()))
		countd(m,n)
	except:
		print('invalid')
main()
