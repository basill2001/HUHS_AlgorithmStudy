import sys

N=int(input())
costs=[]
for i in range(N):
    R,G,B=map(int,sys.stdin.readline().split())
    costs.append([R,G,B])

for i in range(1,N):
    costs[i][0]=costs[i][0]+min(costs[i-1][1],costs[i-1][2])
    costs[i][1]=costs[i][1]+min(costs[i-1][0],costs[i-1][2])
    costs[i][2]=costs[i][2]+min(costs[i-1][0],costs[i-1][1])
print(min(costs[N-1]))

# 원리 이해 못했음..