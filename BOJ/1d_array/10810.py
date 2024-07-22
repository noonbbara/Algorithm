## 10810

import sys

n, m = map(int, (input().split()))

bucket = [0] * n

#print(bucket)

for x in range(m):
    i, j, k = list(map(int, sys.stdin.readline().split()))
    for y in range(j-i+1):
        bucket[i-1+y] = k


print(" ".join(map(str, bucket)))
