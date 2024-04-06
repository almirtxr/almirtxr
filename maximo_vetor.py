# -*- coding: utf-8 -*-
"""
    Descobre o mínimo de n números, inteiros ou reais,
    ou de uma string de n caracteres, e o retorna.
    vet: qualquer sequência (lista, tupla ou string)
    Retorna o valor mínimo do vetor
"""
def max_function(vet):
    n = len(vet)
    maximo = vet[0] # Inicializa o maximo com o
                    # valor da primeira posição do vetor.
    for i in range(1, n): # Compara o segundo valor em diante
        if (vet[i] > maximo): # Se for menor que o maximo
            maximo = vet[i]   # passa a ser o novo maximo
    return maximo

print("Número de inteiros: ", end="")
n = int(input())
while (n <= 0): # Continua a ler até que n > 0
    print("Número de inteiros: ", end="")
    n = int(input())    

vet_int = [0]*n # Inicializa a lista com n zeros

for i in range(n):
    print(i+1, "º número inteiro: ", sep = "", end="")
    # Atribui cada número lido
    vet_int[i] = int (input()) 

# Escreve o maximo
print("O maximo é: ", max_function(vet_int))

print()

print("Número de reais: ", end="")
n = int(input())
while (n <= 0): # Continua a ler até que n > 0
    print("Número de reais: ", end="")
    n = int(input())    

vet_float = [0.0]*n # Inicializa a lista com n zeros

for i in range(n):
    print(i+1, "º número real: ", sep = "", end="")
    # Atribui cada número lido
    vet_float[i] = float(input()) 

# Escreve o mínimo
print("O máximo é: ", max_function(vet_float))


print()

st = input("Digite uma string: ")

# Obtém o maximo
car_max = max_function(st)
# Escreve o máximo
print("O caracter maximo é {0:s}, com código {1:d}".format(car_max, ord(car_max)))
