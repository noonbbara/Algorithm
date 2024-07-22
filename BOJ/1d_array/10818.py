## 10818

import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

print(min(arr), end=" ")
print(max(arr))
