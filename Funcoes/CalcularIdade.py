def calcular_idade(ano_nascimento, ano_atual):

    return ano_atual - ano_nascimento 

ano_nascimento = int(input("Digite o Ano de Nascimento: "))

ano_atual = int(input("Digite o Ano atual: "))

idade = calcular_idade(ano_nascimento, ano_atual) 

print(f"A Idade é {idade} anos.")