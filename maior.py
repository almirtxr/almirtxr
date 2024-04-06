x, y, z = input().split()
x = int(x)
y = int(y)
z = int(z)
maior = (x+y+abs(x-y)) / 2
if maior > z:
    print("%.0f eh o maior"%maior)
else:
    print("%d eh o maior" %z)
