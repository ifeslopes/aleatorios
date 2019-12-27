n=int(input('Entre com numero'))
c=n
f=1
while c>0:
	print('\033[35m{}X{}!\033[m'.format(c,n),end=' ')
	f*=c
	c-=1
print('=',f)