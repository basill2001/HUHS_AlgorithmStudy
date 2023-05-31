from collections import deque

# 입력받기
M,N,H=map(int,input().split())
box=[]
for h in range(H):
    floor=[]
    for n in range(N):
        line=list(map(int,input().split()))
        floor.append(line)
    box.append(floor)

def displaybox(box):
    print("-----box-----")
    for h in range(H):
        for n in range(N):
            print("".join(list(map(str,box[h][n]))))

dx=[1,-1,0,0,0,0]
dy=[0,0,1,-1,0,0]
dz=[0,0,0,0,1,-1]
def getsix(spot,box):
    result=[]
    x=spot[0]
    y=spot[1]
    z=spot[2]
    for i in range(6):
        nx=x+dx[i]
        ny=y+dy[i]
        nz=z+dz[i]
        if 0<=nx<M and 0<=ny<N and 0<=nz<H:
            if box[nz][ny][nx]==0:
                result.append((nx,ny,nz))
    return result

def rippen(start,box):
    toripe=deque(start)
    ripped=[]
    cnt=0
    while len(toripe)!=0:
        child=deque([])
        while len(toripe)!=0:
            node=toripe.popleft()
            if node not in ripped:
                ripped.append(node)
                toripe_2=getsix(node,box)
                for tomato in toripe_2:
                    if tomato not in toripe or tomato not in ripped:
                        child.append(tomato)
                        box[tomato[2]][tomato[1]][tomato[0]]=1
        toripe=child
        cnt+=1
    return cnt-1

def getripped(box):
    ripped=[]
    for h in range(H):
        for n in range(N):
            for m in range(M):
                if box[h][n][m]==1:
                    ripped.append((m,n,h))
    return ripped

def isripped(box):
    for h in range(H):
        for n in range(N):
            for m in range(M):
                if box[h][n][m]==0:
                    return False
    return True

days=0
days=rippen(getripped(box),box)
if isripped(box)==False:
    print(-1)
else:
    print(days)