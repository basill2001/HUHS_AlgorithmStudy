N,M=map(int,input().split())
maze=[]
for i in range(N):
    maze.append(list(map(int,list(input()))))

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def BFS(graph):
    tovisit=[(0,0)]
    while tovisit:
        x,y=tovisit.pop(0)
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<N and 0<=ny<M and graph[nx][ny]==1:
                tovisit.append((nx,ny))
                graph[nx][ny]=graph[x][y]+1
    return graph[N-1][M-1]

print(BFS(maze))