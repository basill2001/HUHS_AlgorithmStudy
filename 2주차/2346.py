import sys
from collections import deque

input=sys.stdin.readline


N=int(input())
nums=list(map(int,input().split()))
balloons=deque(list(i for i in range(1,N+1)))
popped=[]

for i in range(len(nums)):
    print("balloons",balloons)
    popped_balloon=balloons[0]
    popped.append(popped_balloon)
    paper=-1*nums[popped[i]-1]
    print("paper",-paper)
    balloons.rotate(paper)
    print(balloons)
    balloons.remove(popped_balloon)
    print(balloons)

for balloon in popped:
    print(balloon,end=" ")
    