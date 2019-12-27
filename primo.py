num=int(input("entre com numerado"))
ton=int()
for c in range(1,num+1):
 if num%c==0:
 	print('\033[33m', end='')
 	ton+=1
 else:
 	print('\033[31m', end='')
 print('{} '.format(c), end=' ')
print("\n \033[m0 O numero {} foi divido por {}".format(num,ton))
if ton==2:
	print('O numero é PRIMO!')
else:
	print('O numero NÃO É PRIMO!!')