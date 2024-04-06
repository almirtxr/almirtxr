# def montaMatriz(n):
#     mat = []
#     for i in range(n):
#         linha = input().split()
#         lin_int = [0]*n
#         for j in range(n):
#             lin_int[j] = float(linha[j])
#         mat.append(lin_int)
#     return mat
# -*- coding: utf-8 -*-

# Cria uma lista vazia para a matriz
lst_matriz = []

# lin = Ler a linha em que aplicaremos a operação
tam, lc = input().split()
tam = int(tam)
lc = int(lc)

# Criar variável que armazenará a soma
# soma = 0.0
soma = 0.0

# para i de 0 até 11
for i in range(tam):
    # lst_linha = lista vazia que irá armazenar os
    # valores da linha i
    lst_linha = []
    
    # para j de 0 até 11
    for i in range(tam):
         linha = input().split()
         lin_int = [0]*tam
         for j in range(tam):
             lin_int[j] = float(linha[j])
         mat.append(lin_int)
    
    # Colocar lst_linha na matriz lst_matriz
    lst_matriz.append(lst_linha)

# Fazer a soma dos elementos da linha lin
# para j de 0 a 11
for j in range(tam):
    # soma += lst_matriz[lin][j]
    soma += lst_matriz[lc][j]
    