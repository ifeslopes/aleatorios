import os
import time
import random
s=''
e=''
l=''
mater=['ARROZ','MACARRAO','CARNE','FEIJAO','MANTEGA','FARINHA','FUBA','TRIGO','SABAO','BOLO']
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
while s !='s':
	os.system('clear') or None
	e=input("Digite (R) P/ valores automaticos \n É (M)P/ Add valores manual: ")
	if e=="R" or e=="r":
		for i in range (0,3):
		 prod.append(random.choice(mater))
		 prec.append(random.randint(2,90))
		 cont+=1
		 total+=prec[i]
	elif (e=="m") or (e=="M"):
	 for i in range (0,3):
	 	prod.append(str(input("Entre com nome do produto: ")))
	 	prec.append(float(input('Entre com o valor do produto R$: ')))
	 	cont+=1
	 	total+=prec[i]
	else:
	 	 
	 	print('ERRO! Valor digitado diferente de (R) ou (M)')
	 	break
	os.system('clear') or None
	for i in range(0,5):
	#time.sleep(1)
	
	 	print("AGUARDE UM MOMETO",end="")
	 	#l=("."*i)
	 	#print(l)
	 	print("",end="")
	 	l=("."*i)
	 	print(l,end="\r")
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
			print("Codigo do produtos acima da media:\033[31m%d\033[m o nome do produto:\033[31m%s\033[m"%(
		i, prod[i]))
		acm.append(prod[i])
		if (maior_p<prec[i]):
			maior_p=prec[i]
			nome_m=prod[i]
		if (meno_p>prec[i]) or (i==0):
			meno_p=prec[i]
			nome_b=prod[i]
	print('--'*20)		
	print("Produto mais caro é:\033[35m%s \033[me produto mais barato é: \033[36m%s\033[m" %(nome_m, nome_b))
	print("--"*20)
	print("    Codigo    |   Produto   |  Preço ")
	for i in range(0,3):
	 print("\033[31m  ******: %d \033[m |  \033[31m***: %s  \033[m ** |\033[31m  R$:%d\033[m "%(i,prod[i],prec[i]) if
	prec[i]>media else "   ******: %d  |***: %s   ** |R$:%d"%(i,prod[i],prec[i]))
	print('--'*20)
	s=input("Desejar sair? Digite(s) P/continuar aperte(Enter): ")
	prod.clear()
	prec.clear()
	maior_p=0