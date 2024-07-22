## 9086

import sys

n = int(input())

string =[]

for _ in range(n):
    string.append(sys.stdin.readline().strip())

#print(string)

for _ in range(n):
    print(string[_][0], end="")
    print(string[_][-1])

