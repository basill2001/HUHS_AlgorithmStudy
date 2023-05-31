from collections import deque
from itertools import combinations
import copy

# map 가져오기
N,M=map(int,input().split())
basic_shape=[]
for i in range(N):
    basic_shape.append(list(map(int,input().split())))

def getsafeplace(shape):
    cnt=0
    for i in range(N):
        for j in range(M):
            if shape[i][j]==0:
                cnt+=1
    return cnt

def getempty(shape):
    empty=[]
    for i in range(N):
        for j in range(M):
            if shape[i][j]==0:
                empty.append((j,i))
    comb=list(combinations(empty,3))
    return comb

def getvirus(shape):
    virus=[]
    for i in range(N):
        for j in range(M):
            if shape[i][j]==2:
                virus.append((j,i))
    return virus

dx=[1,-1,0,0]
dy=[0,0,1,-1]
def spread(shape,start):
    tovisit=deque([start])
    visited=[]
    while len(tovisit)!=0:
        node=tovisit.popleft()
        if node not in visited:
            visited.append(node)
        for i in range(4):
            nx=node[0]+dx[i]
            ny=node[1]+dy[i]
            if 0<=nx<M and 0<=ny<N:
                if shape[ny][nx]==0:
                    tovisit.append((nx,ny))
                    shape[ny][nx]=2

comb=getempty(basic_shape)
virus=getvirus(basic_shape)

safeplace=[]
for walls in comb:
    # walls=comb[j]
    shape=copy.deepcopy(basic_shape)
    for wall in walls:
        shape[wall[1]][wall[0]]=1
    for vir in virus:
        spread(shape,vir)
    safeplace.append(getsafeplace(shape))

print(max(safeplace))
    