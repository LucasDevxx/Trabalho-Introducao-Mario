G = []
R = []

print("Sistema de correção de provas iniciado")
print('Digite o gabarito da prova (10 respostas):')
cont = 0
while cont < 10:
    resposta = input(f'Questão {cont + 1}: ')
    G.append(resposta)
    cont = cont + 1

print('Digite as respostas do aluno (10 respostas):')
cont = 0
while cont < 10:
    resposta = input(f'Questão {cont + 1}: ')
    R.append(resposta)
    cont = cont + 1
acertos = 0
erros = []

cont = 0
while cont < 10:
    if R[cont] == G[cont]:
        acertos = acertos + 1
    else:
        erros.append(cont + 1)
    cont = cont + 1
