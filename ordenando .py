numeros=[]
for i in range(4):
	numero=int(input('Digite um numero'))
	for chave, valor in enumerate(numeros):
		if numero <valor:
			numeros.insert(chave, numero)
			break
	else:
			numeros.append(numero)
print('--=='*10)
print("Lista atual: ",numeros)