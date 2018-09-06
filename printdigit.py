try:
	a=int(input())
	stri=''
	while(a!=0):
		stri+=str(a%10)
		a//=10
	for i in range(len(stri)-1,-1,-1):
		print(stri[i])
except:
    print('invalid')
