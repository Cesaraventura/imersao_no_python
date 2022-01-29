# exercicio 22
nome = str(input('digite seu nome completo: '))
print('seu nome completo com letras maíusculas é: {} '.format(nome.upper()))
print('seu nome completo com letras minusculas é: {} '.format(nome.lower()))
print('seu nome tem {} letras'.format(len(nome) - nome.count(' ')))
# print('seu primeiro nome tem {} letras'.format(nome.find(' ')))
# jeito do guanabara a partir da linha 6 para contar as letras do primeiro nome
separa = nome.split()
print('seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))

# exercicio 23
num = int(input('digite um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('analisando o número {}'.format(num))
print('unidade: {}'.format(u))
print('dezena: {}'.format(d))
print('centena: {}'.format(c))
print('milhar: {}'.format(m))

# exercicio 24
cid = str(input('em que cidade você nasceu? ')).strip()
print(cid[:5].upper() == 'SANTO')

# exercicio 25
nome = str(input('qual seu nome completo? ')).strip()
print('seu nome tem costa? {}'.format('costa' in nome.lower()))

# exercicio 26
frase = str(input('digite uma frase: ')).upper().strip()
print('a letra A aparece {} vezes'.format(frase.count('A')))
print('a primeira letra A apareceu na posição {}'.format(frase.find('A')+1))
print('a ultima letra A apareceu na posição {}'.format(frase.rfind('A')+1))

# exercicio 27
n = str(input('digite seu nome completo: ')).strip()
nome = n.split()
print('muito prazer em te conhecer!')
print('seu primeiro nome é {}'.format(nome[0]))
print('seu ultimo nome é {}'.format(nome[len(nome)-1]))
