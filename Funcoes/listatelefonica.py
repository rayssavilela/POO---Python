

def converter(lista):

    return [int(telefone) for telefone in lista] 



def verifica_conversao(lista):

    for num in lista:  

       if not isinstance(num, int):  

           return "Erro na conversão."  

    return "Todos os números foram convertidos corretamente!" 

telefones = ["11987654321", "21912345678", "31987654321", "11911223344"] 

telefones_convertidos = converter(telefones) 

print(verifica_conversao(telefones_convertidos)) 

