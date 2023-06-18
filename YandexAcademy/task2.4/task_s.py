# -*- coding: cp1251 -*-

n: int = 5#int(input())

#num: int = n * m
#tmp: int = num

#len_num: int = 0
#while (tmp > 0):
#    tmp //= 10
#    len_num += 1

# ----------------------------------
max_n: int = 0
if n % 2 == 0:
    max_n = n // 2
else:
    max_n = (n // 2) + 1

# ----------------------------------
for i in range(1, n + 1):
    out_n: int = 1
    for j in range(1, n + 1):





        if j > 2 and i > 2:
            out_n = 2
        
        
        print(f"{j}", end=" ")
    print()

