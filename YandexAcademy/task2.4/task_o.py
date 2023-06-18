# -*- coding: cp1251 -*-

n: int = int(input())
m: int = int(input())

num: int = n * m
tmp: int = num

len_num: int = 0
while (tmp > 0):
    tmp //= 10
    len_num += 1

dx: int = (2 * n) - 1
dy: int = 1

for i in range(1, n + 1):
    position: int = 0
    for j in range(i, m + i):
        position += 1
        if position != 1:
            if position % 2 == 0:
                i += dx
            else:
                i += dy
        print(f"{str(i).rjust(len_num, ' ')} ", end="")

    dx -= 2
    dy += 2
    print()


