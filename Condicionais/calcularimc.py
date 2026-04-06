
peso = float(input('Informe seu Peso Corporal: kg '))
altura = float(input('Informe sua altura: m '))
imc = peso / (altura ** 2)

if imc < 18.5:
    print('Você está abaixo do peso normal')

elif 18.5 <= imc or imc < 25:

    print('Você está no seu peso ideal')

else:
    print('Você está acima do peso')