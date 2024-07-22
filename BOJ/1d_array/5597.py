## 5597

n_arr=[]

for _ in range(28):
    n = int(input())
    n_arr.append(n)

#print(len(n_arr))

#print(n_arr)



n_arr = sorted(n_arr)
#print(n_arr)

bad1 = bad2 = 0

for i in range(1, 29):
    if (n_arr[i-1] != i):
        bad1 = i
        break
print(bad1)


for i in range(bad1+1, 29):
    if (n_arr[i-2] != i):
        bad2 = i
        break
print(bad2)
