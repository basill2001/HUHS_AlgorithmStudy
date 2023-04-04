import sys
from collections import deque
input=sys.stdin.readline


N,K=map(int,input().split())
people=deque(list(i for i in range(1,N+1)))
order=[]

for i in range(N):
    people.rotate(-(K-1))
    deleted=people.popleft()
    order.append(deleted)

print(str(order).replace("[","<").replace("]",">"))