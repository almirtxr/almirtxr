"""Este programa irá ler 5 códigos e por meio de estrutura
condicionais vai verificar a quais unidades eles pertencem"""
cod1, cod2, cod3, cod4, cod5 = input().split()#leitura dos 5 codigos de curso

Cod1 = int(cod1) #passa a variavel do tipo str para int
Cod2 = int(cod2) #passa a variavel do tipo str para int
Cod3 = int(cod3) #passa a variavel do tipo str para int
Cod4 = int(cod4) #passa a variavel do tipo str para int
Cod5 = int(cod5) #passa a variavel do tipo str para int

facom = 0 #inicializa a variavel contadora
inma = 0 #inicializa a variavel contadora
outro = 0 #inicializa a variavel contadora

if Cod1 >= 1902 and Cod1 <= 1907: #compara o codigo do curso e ve se esta no intervalo entre 1902 e 1907
    facom += 1 # o contador soma + 1
elif Cod1 >= 2201 and Cod1<= 2291: #compara o codigo do curso e ve se esta no intervalo entre 2201 e 2291
    inma += 1 # o contador soma + 1
else: #se nao estiver dentro dos intervalos, o código é de outra unidade
    outro += 1 # o contador soma +1
    
if Cod2 >= 1902 and Cod2 <= 1907: #compara o codigo do curso e ve se esta no intervalo entre 1902 e 1907
    facom += 1 # o contador soma + 1
elif Cod2 >= 2201 and Cod2 <= 2291: #compara o codigo do curso e ve se esta no intervalo entre 2201 e 2291
    inma += 1 # o contador soma + 1
else:
    outro += 1 # o contador soma + 1
    
if Cod3 >= 1902 and Cod3 <= 1907: #compara o codigo do curso e ve se esta no intervalo entre 1902 e 1907
    facom += 1 # o contador soma + 1
elif Cod3 >= 2201 and Cod3 <= 2291: #compara o codigo do curso e ve se esta no intervalo entre 2201 e 2291
    inma += 1 # o contador soma + 1
else:
    outro += 1 # o contador soma + 1

if Cod4 >= 1902 and Cod4 <= 1907: #compara o codigo do curso e ve se esta no intervalo entre 1902 e 1907
    facom += 1 # o contador soma + 1
elif Cod4 >= 2201 and Cod4 <= 2291: #compara o codigo do curso e ve se esta no intervalo entre 2201 e 2291
    inma += 1 # o contador soma + 1
else:
    outro += 1 # o contador soma + 1

if Cod5 >= 1902 and Cod5 <= 1907: #compara o codigo do curso e ve se esta no intervalo entre 1902 e 1907
    facom += 1 # o contador soma + 1
elif Cod5 >= 2201 and Cod5 <= 2291: #compara o codigo do curso e ve se esta no intervalo entre 2201 e 2291
    inma += 1 # o contador soma + 1
else:
    outro += 1 # o contador soma + 1
print("Facom: %i" %facom) #exibe as quantidades
print("Inma: %i" %inma) #exibe as quantidades
print("Outras unidades: %i" %outro) #exibe as quantidades