# -*- coding: cp1251 -*-

n: int = int(input())
nmax: int = 0
ipos: int = 0

for i in range(2, 11):

    tmp: int = n
    nsum: int = 0
    while (tmp >= i):
        nsum += (tmp % i)
        tmp //= i
    
    nsum += tmp

    if nsum > nmax:
        nmax = nsum
        ipos = i

print(f"{ipos}")
