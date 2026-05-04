class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
    
        if not strs:
            return ""

        prefixo = strs[0]

        for palavra in strs[1:]:
            i = 0
            while i < len(prefixo) and i < len(palavra) and prefixo[i] == palavra[i]:
                i += 1

            prefixo = prefixo[:i]

            if prefixo == "":
                break

        return prefixo
    
"""💡 Como isso funciona
Começa assumindo que o prefixo é a primeira palavra
Compara com as próximas
Vai "encurtando" o prefixo até sobrar apenas o comum
🧠 Exemplo

Entrada:

["flower", "flow", "flight"]

Processo:

prefixo = "flower"
compara com "flow" → "flow"
compara com "flight" → "fl"

Saída:

"fl"""