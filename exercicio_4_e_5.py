#exercício 4
a = input('digite algo: ')
print('O tipo primitivo desse valor é ', type(a))
print('Só tem espaços? ', a.isspace())
print('É um número? ', a.isnumeric())
print('É alfabético? ', a.isalpha())
print('É alfanumérico? ', a.isalnum())
print('Está em maíusculas? ', a.isupper())
print('Está em minúsculas? ', a.islower())
print('Está capitalizada? ', a.istitle())

#exercício 5 (eu fiz)
n = int(input('digite um número: '))
a = n - 1
s = n + 1
print('analizando o valor {}, seu antecessor é {} e seu sucessor é {}'.format(n, a, s))

#exercício 5 (guanabara)
#assistindo ao vídeo ele não utilizou a linha 14 e 15 e na linha 16 ele utiliza .format(n, (n-1), (n+1))
