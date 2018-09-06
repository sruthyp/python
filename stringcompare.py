def compare(st1,sr2):
	if st1==st2:
		print(st2)
	elif st1>st2:
		print(st1)
	else :
		print(st2)
def main():
	try:
		s1=input()
		s2=input()
		compare(s1,s2)
	except:
		print('invalid')
main()
