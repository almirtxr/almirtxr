cpf = input()
sep = ".-"
for i in range(len(sep)):
    CPf = cpf.replace(sep[i],"")
aux = CPf.split(".")
temp = ""
aux2 = temp.join(aux)
CPF = aux2
soma = 0
for i in range(0, len(CPF)-2):
    dig = int(CPF[i])
    soma = soma + (dig * (i+1))
b1 = soma % 11 % 10
soma2 = 0
cont = ['9', '8', '7', '6', '5', '4', '3', '2', '1']
mult = 0
for j in range(0, len(CPF)-2):
    dig2 = int(CPF[j])
    mult = int(cont[j])
    soma2 = soma2 + (dig2 * mult)
b2 = soma2 % 11 % 10


CPFValido =  ["","","","","","","","","",b1,b2]
# if b1Int == b1 and b2Int == b2:
#     print("Valido")
# else:
#     print("inválido")