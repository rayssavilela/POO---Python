maçãs = 0
bananas = 0

maçãs = int(input('Digite a quantidade de maçãs vendidas: \n'))
bananas = int(input('Digite a quantidade de bananas vendidas: \n'))

if maçãs > bananas:
    print(f'As maçãs tiveram mais vendas, totalizando: {maçãs}')

elif bananas > maçãs:
    print(f'As Bananas tiveram mais vendas, totalizando: {bananas}')

else:
    print(f'As vendas foram iguais para ambas.')


