import sys
from collections import deque

d=[1,-1,0]
def geteight(spot,w,h):
    result=[]
    for x in d:
        for y in d:
            if [x,y]!=[0,0] and 0<=spot[0]+x<w and 0<=spot[1]+y<h:
                result.append((spot[0]+x,spot[1]+y))
    return result

def getisland(start,shape):
    tovisit=deque([start])
    visited=[]
    while len(tovisit)!=0:
        node=tovisit.popleft()
        if node not in visited:
            visited.append(node)
            consider=geteight(node,len(shape[0]),len(shape))
            for con in consider:
                if shape[con[1]][con[0]]==1 and con not in visited:
                    tovisit.append(con)
    for visit in visited:
        shape[visit[1]][visit[0]]=0

islands=[]
while True:
    w,h=map(int,input().split())
    if w==0 and h==0:
        break
    shape=[]
    for i in range(h):
        shape.append(list(map(int,sys.stdin.readline().split())))

    cnt=0
    for i in range(h):
        for j in range(w):
            if shape[i][j]==1:
                getisland((j,i),shape)
                cnt+=1
    islands.append(cnt)

for i in islands:
    print(i)