frase = input('Entre com uma frase: ')
frasenospace = frase.replace(' ', '') 
print(frasenospace)
quantiletra = (len(frasenospace)) 
print(quantiletra)

letraespec = input('qual letra vc deseja conferir:')
letraespecvss = frasenospace.count(letraespec)

porcenletra = (letraespecvss/quantiletra)*100 
print('A letra: {}, aparece {} vezes na frase: {}'.format(letraespec, letraespecvss, frase))
print('A porcentagem de repetição desse caracterer em relação ao tamanho da frase é {:.2f}%'.format(porcenletra))