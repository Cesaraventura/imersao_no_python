# exercicio 6 (dobro, triplo, raizquadrada)
n = int(input('digite um número: '))
d = n * 2
t = n * 3
r = n ** (1/2)
print('o dobro de {} vale {}.'.format(n, d))
print('o triplo de {} vale {}. \nA raiz quadrada de {} vale {:.2f}'.format(n, t, n, r))

# exercicio 7 (media aritimetica)
n1 = float(input('Primeira nota do aluno: '))
n2 = float(input('Segunda nota do aluno: '))
media = (n1 + n2)/2
print('A média entre {:.1f} e {:.1f} é igual a {:.1f}'.format(n1, n2, media))

# exercicio 8 (conversor de medidas)
medida = float(input('Uma distância em metros: '))
cm = medida * 100
mm = medida * 1000
print('A medida de {}m corresponde a {:.0f}cm e {:.0f}mm'.format(medida, cm, mm))

# exercicio 9 (tabuada)
num = int(input('Digite um número para ver sua tabuada: '))
print('-' * 15)
print('{} x {:2} = {}'.format(num, 1, num*1))
print('{} x {:2} = {}'.format(num, 2, num*2))
print('{} x {:2} = {}'.format(num, 3, num*3))
print('{} x {:2} = {}'.format(num, 4, num*4))
print('{} x {:2} = {}'.format(num, 5, num*5))
print('{} x {:2} = {}'.format(num, 6, num*6))
print('{} x {:2} = {}'.format(num, 7, num*7))
print('{} x {:2} = {}'.format(num, 8, num*8))
print('{} x {:2} = {}'.format(num, 9, num*9))
print('{} x {:2} = {}'.format(num, 10, num*10))
print('-' * 15)
