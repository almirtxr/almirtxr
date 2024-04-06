"""Este programa lê um intervalo de inteiros e mostra
a quantidade de inteiros no intervalo, a quantidade de números pares,
a quantidade de numeros impares e a quantidade de numeros divisiveis por 5"""
x = 0
y = 1
while x >= 0 and x < y:
    x, y = input().split() #leitura dos numeros na mesma linha
    x = int(x) #conversão dos numeros para inteiro
    y = int(y) #conversão dos numeros para inteiro

    i = 0 #inicialização de variável
    contPar = 0 #inicialização de variável
    contImp = 0 #inicialização de variável
    contDivi = 0 #inicialização de variável
    inteiro = 0 #inicialização de variável
    while i < y: #condição para manter o programa rodando dentro do intervalo
        for i in range(x+1, y): #laço de repetição para verificar os numeros do intervalo
            inteiro += 1 #variável contadora de inteiros
            if i % 2 == 0: #verifica se o numero é par
                contPar += 1 #variavel contadora
            elif i % 2 != 0: #verifica se o numero é impar
                contImp += 1 #variavel contadora
            if i % 5 == 0: # verifica se o numero é divisivel por 5
                contDivi += 1 #variavel contadora
            i += 1 #variavel para icrementar o indice do laço For
    if contDivi %2 == 0:
        print("Intervalo (%i, %i):" %(x,y)) #este bloco mostra as informações
        print("Quantidade de inteiros: %d" %inteiro)
        print("Quantidade de pares: %d" %contPar)
        print("Quantidade de ímpares: %d" %contImp)
        print("Quantidade de divisíveis por 5: %d" %contDivi)
        break
    elif contDivi %2 != 0:
        print("Intervalo (%i, %i):" %(x,y)) #este bloco mostra as informações
        print("Quantidade de inteiros: %d" %inteiro)
        print("Quantidade de pares: %d" %contPar)
        print("Quantidade de ímpares: %d" %contImp)
        print("Quantidade de divisíveis por 5: %d" %contDivi)
        print()
    
