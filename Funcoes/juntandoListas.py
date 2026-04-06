#Clara está gerenciando o estoque de sua loja e recebeu duas listas separadas: uma contendo os nomes dos produtos e outras com seus respectivos preços. 
#Para facilitar a organização, ela precisa combinar essas listas de forma que cada produto seja associado ao seu preço.

#Crie um programa que junte as listas e exiba o resultado no formato produto: preço

def listasCompras():
    #O split() não está usando a vírgula, para isso O correto é:.split(",")
    produtos = input("Digite os produtos separados por vírgula: ").split(",") 
    valores = input("Digite os preços separados por vírgula: ").split(",") 
    #As listas podem ter espaços extras, Os itens ficarão:['Arroz', ' Feijão', ' Açúcar']
    #Para evitar, inclua .strip().
    produtos = [p.strip() for p in produtos]
    valores = [float(v.strip()) for v in valores]

    for produto, preco in zip(produtos, valores):
        print(f"{produto}: R$ {preco:.2f}")


#resolução 2:


produtos = input("Digite os produtos separados por vírgula: ").split(",") 
precos = input("Digite os preços separados por vírgula: ").split(",") 
 
for produto, preco in zip(produtos, precos): 
    print(f"{produto.strip()}: {preco.strip()}") 
