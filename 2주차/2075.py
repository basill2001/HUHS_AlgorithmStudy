import sys
input=sys.stdin.readline
import heapq

# 입력
N=int(input())
field=[]
column=[i for i in range(N)]
for i in range(N):
    x=list(map(int,input().split()))
    # 집어넣기
    for num in x:
        heapq.heappush(field,num)
        # N 초과하면 최소값 빼기
        if len(field)>N:
            heapq.heappop(field)

print(heapq.heappop(field))
        

## 메모리 초과 발생
# for i in range(2,N+1):
#     j=0
#     consider=False
#     for j in column:
#         if consider:
#             j-=1
#         track=table[N-i][j]
#         if track<floor[0]:
#             column.remove(j)
#             consider=True
#         else:
#             floor.append(track)
#             del floor[0]
#             floor.sort()

#         if len(column)==0:
#             break
#     if len(column)==0:
#         break

