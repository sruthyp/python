try :
	s1=raw_input("enter the string1 : ")
	s2=raw_input("enter the string2 : ")
	ans=0
	a=s1.split(':')
	b=s2.split(':')
	c=int(a[0])*60+int(a[1])
	d=int(b[0])*60+int(b[1])
	if(c>d):
		ans=c-d
	else:
		ans=d-c
	print(ans)
except :
	print ("Invalid")
