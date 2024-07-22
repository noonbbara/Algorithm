## 10871

import sys

n, x = map(int, (input().split()))

a = list(map(int, sys.stdin.readline().split()))

#lower_arr = []

for i in range(len(a)):
    if a[i] < x:
        #lower_arr.append(a[i])
        print(a[i], end=" ")
        

#print(lower_arr)
