"""Este código ira ler 3 notas de prova e uma nota de trabalho
, depois irá calcular a media e comparar com a suficiente para ser aprovado
(>= 6.0), caso nao seja aprovado direto, será solicitado a nota da OPT e ira recalcular
a media substituindo a menor nota das provas"""
P1, P2, P3, Tp = input().split() #leitura das notas
p1 = float(P1) #conversão para float
p2 = float(P2) #conversão para float
p3 = float(P3) #conversão para float
tp = float(Tp) #conversão para float
mediaPs = (p1 + p2 + p3) / 3  #calculo da media aritmética
porcentMP = 80 / 100 #calculo da porcentagen
porcentTP = 20 / 100 #calculo da porcentagem
ma = (mediaPs*porcentMP) + (porcentTP*tp) #soma da medias das provas e trabalho
menor = 0 #inicializa a variavel menor nota
if ma >= 6: #faz a comparação e exibe o resultado da aprovação
    print("MA: %.1f"%ma) #exibe a media
    print("Estudante aprovado(a)") 
elif ma < 6: #compara a media
    print("O(A) estudante precisa fazer a prova optativa!")
    opt = float(input()) #le a nota da optativa
    if p1 < p2 and p1 < p3: #este bloco faz a comparação para descobrir a menor nota
        menor = p1
        mediaPs = (opt + p2 + p3) / 3 #recalcula a media
    if p2 < p1 and p2 < p3:
        menor = p2
        mediaPs = (p1 + opt + p3) / 3 #recalcula a media
    if p3 < p1 and p3 < p2:
        menor = p3
        mediaPs = (p1 + p2 + opt) / 3 #recalcula a media
    porcentMP = 80 / 100 #recalcula a porcentagem
    porcentTP = 20 / 100 #recalcula a porcentagem
    ma = (mediaPs*porcentMP) + (porcentTP*tp) #recalcula a media
    if ma > 6: #se a nota for maior que 6, o aluno é aprovado
        print("MA: %.1f" %ma)
        print("Estudante aprovado(a)")
    else: #se a nota for menor que 6, o aluno é reprovado
        print("MA: %.1f" %ma)
        print("Estudante reprovado(a)")

