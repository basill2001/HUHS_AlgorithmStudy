from collections import deque

# 입력받기
M,N=map(int,input().split())
box=[]
for i in range(N):
    box.append(list(map(int,input().split())))

tomato=deque([])
for i in range(N):
    for j in range(M):
        if box[i][j]==1:
            tomato.append((j,i))

def displaybox(box):
    print("------box------")
    for i in range(N):
        print(box[i])

dx=[1,-1,0,0]
dy=[0,0,1,-1]
def BFS():
    cnt=0
    while tomato:
        x,y=tomato.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<M and 0<=ny<N and box[ny][nx]==0:
                box[ny][nx]=box[y][x]+1
                tomato.append((nx,ny))
BFS()

maxi=0
for i in range(N):
    for j in range(M):
        if box[i][j]==0:
            print(-1)
            exit(0)
        if box[i][j]>maxi:
            maxi=box[i][j]
print(maxi-1)