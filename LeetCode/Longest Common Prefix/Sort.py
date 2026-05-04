def longestCommonPrefix(strs):
    if not strs:
        return ""

    strs.sort()

    primeira = strs[0]
    ultima = strs[-1]

    i = 0
    while i < len(primeira) and i < len(ultima) and primeira[i] == ultima[i]:
        i += 1

    return primeira[:i]


print(longestCommonPrefix(["flower", "flow", "flight"]))

"""Você ordena e compara só duas palavras:

strs.sort()
primeira = strs[0]
ultima = strs[-1]

👉 Ideia:

A maior diferença vai estar entre a primeira e a última
Se elas combinam, todas do meio também combinam

✔️ Mais elegante
✔️ Menos comparações
❌ Precisa ordenar (custo extra)"""