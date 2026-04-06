A = int(input('Informe o numero de dias para a atividade A: '))
B = int(input('Informe o numero de dias para a atividade B: '))
C = int(input('Informe o numero de dias para a atividade C: '))
Tempo_total = 0

if (A < 0) or (B < 0) or (C < 0):
    print('Erro: os dias não podem ser negativos')

else:
    print(f'Os dias para as atividades foram de:\n'
          f'A = {A}\n'
          f'B = {B}\n'
          f'C = {C}')
    Tempo_total = A + B + C
    print(f'Tempo total de: {Tempo_total}')

