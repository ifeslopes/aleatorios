def fatorial(n):
	fat=1
	while (n>1):
		fat*=n
		n-=1
	return fat
def num_bi(n,k):
	return fatorial(n)/(fatorial(k)*fatorial(n-k))

#n=fatorial(int(input("entre")))
#print(n)