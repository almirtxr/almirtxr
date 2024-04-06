"""Este programa ira ler o numero, e fazer
uma série de operações matematicas de para obter os milhares, as centas e dezenas"""
n = int(input()) #leitura do numero
print("%i:"%n)
mil = n / 1000 #divisão do numero por 1 mil
n = n % 1000 #a variavel "n" armazena o resto da divisão por 1 mil
c100 = n / 100 #a variavel "c100" pega a quantidade de centenas no numero
n = n%100 #é feita a operação para obter o resto da divisao
d10 = n/10 #operação para obter a quantidade de dezenas
uni = n%10 #operação para obter a quantidade de unidades no numero

print("%i milhar(es)" %mil) #exibir a quantidade de milhares
print("%i centena(s)" %c100) #exibir a quantidade de centenas
print("%i dezena(s)" %d10) #exibir a quantidade de dezenas
print("%i unidade(s)" %uni) #exibir a quantidade de unidades
