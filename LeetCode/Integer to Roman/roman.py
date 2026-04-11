class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        self.num = num

        valores = [ #lista de tuplas
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I")
    ]

        resultado = ""
        if 1 <= num <= 3999:
            for valor, simbolo in valores:
                while num >= valor:
                    resultado += simbolo
                    num -= valor

        return resultado
        

"""Sete símbolos diferentes representam numerais romanos com os seguintes valores:

Símbolo	Valor
I	1
V	5
X	10
L	50
C	100
D	500
M	1000
Os numerais romanos são formados pela conversão dos valores posicionais decimais, do maior para o menor. A conversão de um valor posicional decimal em um numeral romano segue as seguintes regras:

Se o valor não começar com 4 ou 9, selecione o símbolo do maior valor que pode ser subtraído da entrada, anexe esse símbolo ao resultado, subtraia o seu valor e converta o resto em um numeral romano.
Se o valor começar com 4 ou 9, use a  forma subtrativa  que representa um símbolo subtraído do símbolo seguinte, por exemplo, 4 é 1 ( I) menos que 5 ( V): IV e 9 é 1 ( I) menos que 10 ( X): IX. Somente as seguintes formas subtrativas são usadas: 4 ( IV), 9 ( IX), 40 ( XL), 90 ( XC), 400 ( CD) e 900 ( CM).
Apenas as potências de 10 ( I, X, C, M) podem ser concatenadas consecutivamente no máximo 3 vezes para representar múltiplos de 10. Você não pode concatenar 5 ( V), 50 ( L) ou 500 ( D) várias vezes. Se você precisar concatenar um símbolo 4 vezes, use a forma subtrativa .
Dado um número inteiro, converta-o para um numeral romano.

 

Exemplo 1:

Entrada: num = 3749

Saída: "MMMDCCXLIX"

Explicação:

3000 = MMM como 1000 (M) + 1000 (M) + 1000 (M)
 700 = DCC como 500 (D) + 100 (C) + 100 (C)
  40 = XL, pois é 10 (X) a menos que 50 (L)
   9 = IX como 1 (I) menos 10 (X)
Observação: 49 não é 1 (I) a menos que 50 (L) porque a conversão é baseada em casas decimais.
Exemplo 2:

Entrada: num = 58

Saída: "LVIII"

Explicação:

50 = L
 8 = VIII
Exemplo 3:

Entrada: num = 1994

Saída: "MCMXCIV"

Explicação:

1000 = M
 900 = CM
  90 = XC
   4 = IV
 

Restrições:

1 <= num <= 3999

Use dict quando precisa buscar valor(dicionario)
Use lista quando precisa controlar ordem (lista de tupla)"""