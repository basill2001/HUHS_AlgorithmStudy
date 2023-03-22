N=int(input())
a=[]

for i in range(N):
    n=int(input())
    a.append(n)

a.sort()
for i in a:
    print(i)