# exercicio_35
r1 = float(input('primeiro lado do triangulo: '))
r2 = float(input('segundo lado do triangulo: '))
r3 = float(input('terceiro lado do triangulo: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('os lados PODEM formar um triangulo!')
else:
    print('os lados NÃO PODEM formar um triangulo!')
