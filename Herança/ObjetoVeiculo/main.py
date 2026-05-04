# 7- Crie um Arquivo Main (main.py): Crie um arquivo chamado main.py no mesmo diretório que suas classes.

# 8- Importe e Instancie Objetos: No arquivo main.py, 
# importe as classes Carro e Moto. Em seguida, crie três instâncias de Carro e Moto com diferentes marcas, modelos, quantidade de portas e tipos.
from carro import Carro
from moto import Moto

carro1 = Carro("Chevrolet", "Onix", 4)
carro2 = Carro("Hyundai", "HB20", 4)
carro3 = Carro("BMW", "320i", 4)

moto1 = Moto("Ducati", "Shiron", "Esportiva")
moto2 = Moto("Yamaha", "MT-03", "Esportiva")
moto3 = Moto("Honda", "PCX-150", "Casual")


# 9- Exiba as Informações: Para cada instância, imprima no console as informações utilizando o método __str__.
print(carro1)
print(carro2)
print(carro3)

print(moto1)
print(moto2)
print(moto3)