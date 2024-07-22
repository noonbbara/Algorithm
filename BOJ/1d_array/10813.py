## 10813

import sys

n, m = map(int, (input().split()))

bucket = []
for _ in range(n):
    bucket.append(_+1)

#print(bucket)

for x in range(m):
    i, j= list(map(int, sys.stdin.readline().split()))
    temp = bucket[i-1]
    bucket[i-1] = bucket[j-1]
    bucket[j-1] = temp


print(" ".join(map(str, bucket)))
