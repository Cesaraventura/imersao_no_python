# exercicio 10 (transformando real em dolar)
real = float(input('quanto dinheiro você tem na carteira? R$'))
dolar = real / 5.38
print('Com R${:.2f} você pode comprar US${:.2f}'.format(real, dolar))

# exercicio 11 (pintando parede, cada litro de tinta pinta 2 m²)
larg = float(input('largura da parede: '))
alt = float(input('altura da parede: '))
area = larg * alt
print('sua parede tem dimensão de {}x{} e sua área é de {}m²'.format(larg, alt, area))
tinta = area / 2
print('para pintar essa parede, você precisa de {} litros de tinta'.format(tinta))

# exercico 12 (calculando descontos)
preco = float(input('qual o preço do produto? R$'))
novo = preco - (preco * 5 / 100)
print('o produto que custava R${:.2f}, com desconto de 5% custará R${:.2f}'.format(preco, novo))

# exercicio 13 (salário do funcionário)
salario = float(input('qual o salario do funcionario? R$'))
novo = salario + (salario * 15 / 100)
print('um funcionario que ganhava R${:.2f}, com 15% de aumento, ganhará R${:.2f}'.format(salario, novo))

# exercicio 14 (conversor de temperaturas)
c = float(input('informe a temperatura em ºC: '))
f = 9 * c / 5 + 32
print('a temperatura em {}ºC corresponde a {}ºF'.format(c, f))

# exercicio 15 (aluguel de carros: aluguel 60 reais por dia e 0,15 por km rodado)
dias = int(input('quantos dias alugados? '))
km = float(input('quantos kms rodados? '))
pago = (dias * 60) + (km * 0.15)
print('o total a pagar é de R${:.2f}'.format(pago))
