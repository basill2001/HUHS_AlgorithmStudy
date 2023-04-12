import sys
from collections import deque

input=sys.stdin.readline


N=int(input())
nums=list(map(int,input().split()))
balloons=deque(list(i for i in range(1,N+1)))
popped=[]

for i in range(len(nums)):
    popped_balloon=balloons[0]
    popped.append(popped_balloon)
    paper=-1*nums[popped[i]-1]
    balloons.rotate(paper)
    balloons.remove(popped_balloon)

for balloon in popped:
    print(balloon,end=" ")
    