def longestCommonPrefix(strs):
    if not strs:
        return ""

    prefixo = strs[0]

    for palavra in strs[1:]:
        while not palavra.startswith(prefixo):
            prefixo = prefixo[:-1]

            if prefixo == "":
                return ""

    return prefixo


print(longestCommonPrefix(["flower", "flow", "flight"]))

"""🧠 Como funciona

Começa assumindo que a primeira palavra inteira é o prefixo:

prefixo = "flower"

Depois compara com "flow":

"flow".startswith("flower") → False
Então vai cortando:
flowe
flow

Agora:

"flow".startswith("flow")  # True

Segue para próxima palavra: "flight"

Testa:

flight.startswith("flow")  # False

Vai cortando:

flo
fl

Agora:

flight.startswith("fl")  # True

Retorna "fl"."""