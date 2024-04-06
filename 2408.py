"""
# -*- coding: utf-8 -*-
cont = 0
aux = 0
while cont != 2:
    nota = float(input())
    if nota >= 0 and nota<=10:
        cont = cont+1
        aux = aux+nota
    else:
        print("nota invalida")
media=aux/2.00
print("media = %0.2f"%media)
"""
idc = "ufms campo grande"
print(idc)
print(idc[6])