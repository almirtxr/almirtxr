def copia_lista(vet):
    n = len(vet)
    copia = [None]*n
    for i in range(n):
        copia[i] = vet[i]
    return copia
    
lista = input()
print(copia_lista(lista))