
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        self.s = s
        chars = set()
        esquerda = 0
        maior = 0  

        for direita in range(len(s)): #direita → vai avançando pela string
                while s[direita] in chars:
                    chars.remove(s[esquerda])
                    esquerda += 1
            
                chars.add(s[direita])
                maior = max(maior, direita - esquerda + 1)
        return maior

"""Dada uma string s, encontre o comprimento do caractere mais longo. substringSem caracteres duplicados.

Exemplo 1:

Entrada: s = "abcabcbb"
 Saída: 3
 Explicação: A resposta é "abc", com comprimento 3. Observe que "bca"e "cab"também são respostas corretas.
Exemplo 2:

Entrada: s = "bbbbb"
 Saída: 1
 Explicação: A resposta é "b", com comprimento 1.
Exemplo 3:

Entrada: s = "pwwkew"
 Saída: 3
 Explicação: A resposta é "wke", com comprimento 3.
Note que a resposta deve ser uma substring; "pwke" é uma subsequência e não uma substring.
 

Restrições:

0 <= s.length <= 5 * 104
sConsiste em letras, dígitos, símbolos e espaços em inglês."""