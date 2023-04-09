import sys
input=sys.stdin.readline

N=int(input())
lst=[]
for i in range(N):
    x,y=map(int,input().split())
    lst.append((x,y))

order=[]
for i in range(N):
    bigger=0
    for j in range(N):
        if lst[i][0]<lst[j][0] and lst[i][1]<lst[j][1]:
            bigger+=1
    order.append(bigger+1)

for big in order:
    print(big,end=" ")
        