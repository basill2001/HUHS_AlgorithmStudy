import sys
from collections import deque

input=sys.stdin.readline


N,M=map(int,input().split())
deq=deque(list(range(1,N+1)))
locations=list(map(int,input().split()))


## 2번 연산=rotate(negative)
## 3번 연산=rotate(positive)
def caldist(start,goal):
    dist=deq.index(goal)-deq.index(start)
    dist_mirr=len(deq)-abs(dist)
    if dist>0:
        dist_mirr*=-1
    if abs(dist)<=abs(dist_mirr):
        return -1*dist
    else:
        return -1*dist_mirr


cnt=0
for loca in locations:
    if deq[0]==loca:
        deq.popleft()
    else:
        cnt=cnt+abs(caldist(deq[0],loca))
        deq.rotate(caldist(deq[0],loca))
        if deq[0]==loca:
            deq.popleft()
print(cnt)