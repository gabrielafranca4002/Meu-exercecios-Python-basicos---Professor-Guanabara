d = int(input('Por quantos dias o carro foi alugado? '))
k = float(input('Quantos km foram rodados? '))
p = (d * 60) + (k * 0.15)
print('O total a pagar é de {:.2f}'.format(p))
