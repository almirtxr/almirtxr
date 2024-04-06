'''
raio = float(input())
area = raio ** 2 * 3.14159
print("A=%.4f"%area)
'''
'''
n1 = float(input())
n2 = float(input())
media = n1 * 3.5 + n2 * 7.5
media = media / 11
print("MEDIA = %.5f"%media)
'''
'''
tempo = int(input())
horas = int(tempo / 3600)
minutos = int(tempo / 60)
tempo -= minutos*60
minutos %= 60
print("%d:%d:%d"%(horas, minutos, tempo))
'''
'''
a = int(input())
b = int(input())
c = int(input())
d = int(input())
prod = a*b
prod2 = c*d
dif = prod - prod2
print("DIFERENCA = %d"%(dif))
'''
'''
a, b, c, d = input().split()
a = int(a)
b = int(b)
c = int(c)
d = int(d)
v1 = False
v2 = False
v3 = False
v4 = False
if b > c and d > a:
    v1 = True
somaab = a + b
somacd = c + d
if somacd > somaab:
    v2 = True
if c > 0 and d > 0:
    v3 = True
if a % 2 == 0:
    v4 = True
#print("%s" %v4)
if v1 == True and v2 == True and v3 == True and v4 == True:
    print("Valores aceitos")
else:
    print("Valores nao aceitos")

'''
'''
n = int(input())
if n == 0:
    print("E")
if n >= 1 and  n <= 35:
    print("D")
if n >= 36 and n <= 60:
    print("C")
if n >= 61 and n <= 85:
    print("B")
if n >= 86 and n <= 100:
    print("A")
'''
'''
import math
x1 , y1 = input().split()
x2, y2 = input().split()
x1 = float(x1)
x2 = float(x2)
y1 = float(y1)
y2 = float(y2)
e1 = (x2 - x1)*(x2 - x1)
e2 = (y2 - y1)*(y2 - y1)
soma = e1 + e2
res = math.sqrt(soma)
print("%.4f" %res)
'''
'''
hr = int(input())
vel = int(input())
d = hr * vel
res = d / 12
print("%.3f" % res)
'''
'''
tp = int(input())
p1, p2, p3, p4, p5 = input().split()
p1 = int(p1)
p2 = int(p2)
p3 = int(p3)
p4 = int(p4)
p5 = int(p5)
ac = 0
if p1 == tp:
    ac += 1
if p2 == tp:
    ac += 1
if p3 == tp:
    ac += 1
if p4 == tp:
    ac += 1
if p5 == tp:
    ac += 1
print(ac)
'''