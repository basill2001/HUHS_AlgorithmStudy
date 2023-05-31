from collections import deque

dx=[1,-1,0,0]
dy=[0,0,1,-1]

def BFS(gard,v):
    visited=[]
    tovisit=deque([v])
    while tovisit:
        node=tovisit.popleft()
        if node not in visited:
            visited.append(node)
            del gard[node]
            for i in range(4):
                nx=node[0]+dx[i]
                ny=node[1]+dy[i]
                if (nx,ny) in gard:
                    tovisit.append((nx,ny))

T=int(input())
worms=[]
for i in range(T):
    M,N,K=map(int,input().split())
    cabbage={}
    for k in range(K):
        x,y=map(int,input().split())
        cabbage[(x,y)]=1
    cnt=0
    while cabbage:
        srch=list(cabbage.keys())[0]
        BFS(cabbage,srch)
        cnt+=1
    worms.append(cnt)

for w in worms:
    print(w)