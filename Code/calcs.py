import math

a = 0.03
b = 0.84
c = 0.33
d = 3.23

pctspB = 0
pctspF = 1

x = 50* (pctspB) + 100 * (1 - pctspB)
y = 50*(pctspF) + 100 *(1- pctspF)

print(x,y)
num = a*(b*y + c*x)
denom = (d*y + c*x)
print(num)
print(denom)
mperm = a*(b*y + c*x) / (d*y + c*x)

print(mperm)
