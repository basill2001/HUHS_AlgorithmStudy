import sys
import heapq

N=int(input())
hp=[]
for i in range(N):
    x=-1*int(sys.stdin.readline())
    if x!=0:
        heapq.heappush(hp,x)
    else:
        if len(hp)>0:
            print(-1*(heapq.heappop(hp)))
        else:
            print(0)