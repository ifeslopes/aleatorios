import os
import time
prod=[]
prec=[]
acm=[]
abm=[]
media=float()
cont=0
total=0
meno_p=0
maior_p=0
nome_m=''
nome_b=""

for i in range (0,3):
	
	prod.append(str(input("Entre com nome do produto: ")))
	prec.append(float(input('Entre com o valor do produto R$: ')))
	cont+=1
	total+=prec[i]

os.system('clear') or None
for i in range(0,4):
	#time.sleep(1)
	if i<1:
	 print("AGURADE UM MOMETO")
	else :
		print("\033[k",4-i,end="\r")
	
	
		
	time.sleep(1)
os.system('clear') or None
if i>=3:
		print("PRONTO!")
		time.sleep(2)
os.system('clear') or None
	
media=total/cont
print()
print("A MÉDIA DOS PREÇOS: %2.f"%media)
print("--"*20)

for i in range(0,3):
	if prec[i]>media:
		print("codigos dos produtos acima da media %d os nomes dos produto%s"%(
		i, prod[i]))
		acm.append(prod[i])
	if (maior_p<prec[i]):
		maior_p=prec[i]
		nome_m=prod[i]
	if (meno_p>prec[i]) or (i==0):
		meno_p=prec[i]
		nome_b=prod[i]
print('--'*20)		
print("O produto mais caro é:\033[31m %s \033[me o produto mais barato é: %s " %(nome_m, nome_b))
print("--"*20)
print("    Codigo    |   Produto   |  Preço ")
for i in range(0,3):
	print("\033[31m  ******   %d \033[m |  \033[31m*** %s  \033[m ** |  \033[31m  R$:%d\033[m "%(i,prod[i],prec[i]) if prec[i]>media else "   ******* %d  | *** %s   ** |R$:%d"%(i,prod[i],prec[i]))