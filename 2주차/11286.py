import sys
input=sys.stdin.readline
import heapq

N=int(input())
heap=[]

def calcul(x):
    if x==0:
        # 절댓값이 가장 작은 값 pop
        if len(heap)>0:
            print(heapq.heappop(heap)[1])
        else:
            print(0)
    else:
        # x 추가
        heapq.heappush(heap,(abs(x),x))

for i in range(N):
    x=int(input())
    calcul(x)