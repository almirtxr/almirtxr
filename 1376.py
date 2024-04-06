"""O programa consiste em criar uma matriz de L linhas e C colunas e ler todos os números informados
pelo usuário, após é indexado cada número em uma posição da matriz com auxílio da funcção append(),

"""
linha, coluna = input().split()
L = int(linha)
C = int(coluna)
linha = int(linha)
coluna = int(coluna)
matriz = []
for i in range(L):
    L = input().split()
    lst = []
    for j in range(C):
        lst.append(int(L[j]))
    matriz.append(lst)
degraus = []
j = 0
degraus2 = []
for j in range(linha):
    lst1 = []
    lst1.append(int(matriz[j][j]))
    degraus.append(lst1)
# for k in range(linha):
#      lst2 = []
#      lst2 = append(int(matriz[k+1][k+1]))
#      degraus2.append(lst2)


for i in range(linha):
    print(*degraus[i], end=" ")


    
# for k in range(linha):
#     for l in range(coluna):
#         print(" " + str(matriz[k][l]), end="")
#     print()

