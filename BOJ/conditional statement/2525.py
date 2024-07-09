## 2525

h, m = map(int, input().split())
m2 = int(input())

mh = m2//60
mm = m2%60

h += mh
if m + mm >= 60:
    h += 1
    m = m + mm -60
else:
    m += mm

if h >= 24:
    h -= 24

print(h, m)
