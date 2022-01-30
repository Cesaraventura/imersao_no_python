# exercicio 28
from random import randint
computador = randint(0, 5)  #faz o computador pensar
print('-=-' * 20)
print('vou pensar em um numero entre 0 e 5. tente adivinhar...')
print('-=-' * 20)
jogador = int(input('em que numero eu pensei? '))   #jogador tenta adivinhar
if jogador == computador:
    print('PARABENS! Você conseguiu acertar')
else:
    print('GANHEI! eu pensei no número {} não no {}!'.format(computador, jogador))

# exercicio 29
velocidade = float(input('qual a velocidade atual do carro? '))
if velocidade > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80km/h')
    multa = (velocidade - 80) * 7
    print('Você deve pagar uma multa de R${:.2f}!'.format(multa))
print('tenha um bom dia! dirija com cuidado')

# exercicio 30
numero = int(input('digite um numero qualquer '))
resultado = numero % 2
if resultado == 0:
    print('o numero {} é PAR'.format(numero))
else:
    print('o numero {} é IMPAR'.format(numero))

# exercicio 31
distancia = float(input('qual a distancia da sua viagem? '))
print('você está prestes a começar uma viagem de {}km.'.format(distancia))
preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print('e o preço da passagem sera de R${:.2f}'.format(preco))
