from exercicio2 import Livro

livro1 = Livro('Uma nova Era', 'Ana Lucia', 1998)
livro2 = Livro('Dama da Corte', 'Bethoven', 2001)
livro3 = Livro('Força e Fé', 'Eliseu', 1996)
livro4 = Livro('Juiz da Vida', 'Carmen Lucia', 2013)
livro5 = Livro('Disciplinada', 'Carmen Lucia', 2010)

livro3.emprestar()

print(livro1)
print(livro2)
print(livro3)

# Verificar livros disponíveis de 1998
disponiveis = Livro.verificar_disponibilidade(1998)

for livro in disponiveis:
    print(livro._titulo)


livro5.emprestar()

print(livro4)
print(livro5)