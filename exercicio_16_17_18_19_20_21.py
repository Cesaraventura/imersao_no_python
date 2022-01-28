# exercicio 16 (ler um numero real e mostre sua porção inteira)
import math
num = float(input('digite um valor: '))
print('o valor digitado foi {} e a sua porção inteira é {}'.format(num, math.trunc(num)))

# exercicio 17  (programa que le os catetos e encontra a hipotenusa)
co = float(input('comprimento do cateto oposto: '))
ca = float(input('comprimento do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1 / 2)
print('A hipotenusa vale {:.2f}'.format(hi))

# outra maneira ex 17
import math
co = float(input('comprimento do cateto oposto: '))
ca = float(input('comprimento do cateto adjacente: '))
hi = math.hypot(co, ca)
print('A hipotenusa vale {:.2f}'.format(hi))

# exercicio 18 (digite um angulo e descubra o sen, cos e tg)
import math
angulo = float(input('digite um ângulo: '))
sen = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tg = math.tan(math.radians(angulo))
print('o ângulo de {} tem o seno de {:.2f}'.format(angulo, sen))
print('o ângulo de {} tem o cosseno de {:.2f}'.format(angulo, cos))
print('o ângulo de {} tem a tangente de {:.2f}'.format(angulo, tg))

# exercicio 19 (sortear alunos e escolher 1)
import random
n1 = (str(input('primeiro aluno: ')))
n2 = (str(input('segundo aluno: ')))
n3 = (str(input('terceiro aluno: ')))
n4 = (str(input('quarto aluno: ')))
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print('O aluno escolhido foi: {}'.format(escolhido))

# exercicio 20 (sortear a ordem de uma lista)
import random
n1 = (str(input('primeiro aluno: ')))
n2 = (str(input('segundo aluno: ')))
n3 = (str(input('terceiro aluno: ')))
n4 = (str(input('quarto aluno: ')))
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print('a ordem da apresentação será: ')
print(lista)

# exercicio 21 (tocando música) (esse exercicio eu copiei exatamente igual do video)
import pygame
pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
pygame.event.wait()
