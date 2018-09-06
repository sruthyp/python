def compare(str1,str2):
	for i in range(len(str2)):
		str1+=str2[i]
	print(str1)
def main():
	try:
		a1=input()
		a2=input()
		compare(a1,a2)
	except:
		print('invalid')
main()
