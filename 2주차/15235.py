import sys
input=sys.stdin.readline
from collections import deque

N=int(input())
slices=list(map(int,input().split()))
cur=[[i+1,0] for i in range(N)]

for i in range(len(slices)):
    cur[i].append(slices[i])
cur=deque(cur)

time=[0 for i in range(N)]
tottime=0
while len(cur)!=0:
    cur[0][1]+=1
    tottime+=1
    if cur[0][1]==cur[0][2]:
        time[cur[0][0]-1]=tottime
        cur.popleft()
    else:
        cur.rotate(-1)

for tick in time:
    print(tick,end=" ")