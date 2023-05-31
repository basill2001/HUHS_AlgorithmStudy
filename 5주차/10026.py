from collections import deque
import copy

# def displayshape(shape):
#     for s in shape:
#         print("".join(list(map(str,s))))

dx=[1,-1,0,0]
dy=[0,0,1,-1]
def norm(start,shape):
    norm_queue=deque([start])
    visited=[]
    while len(norm_queue)!=0:
        node=norm_queue.popleft()
        if node not in visited:
            visited.append(node)
            for i in range(4):
                nx=node[0]+dx[i]
                ny=node[1]+dy[i]
                if 0<=nx<len(shape) and 0<=ny<len(shape):
                    if shape[ny][nx]==shape[node[1]][node[0]] and (nx,ny) not in visited:
                        norm_queue.append((nx,ny))
    for visit in visited:
        shape[visit[1]][visit[0]]=0

def weak(start,shape):
    color=[shape[start[1]][start[0]]]
    if color==["R"]:
        color.append("G")
    elif color==["G"]:
        color.append("R")
    queue=deque([start])
    visited=[]
    while len(queue)!=0:
        node=queue.popleft()
        if node not in visited:
            visited.append(node)
            for i in range(4):
                nx=node[0]+dx[i]
                ny=node[1]+dy[i]
                if 0<=nx<len(shape[0]) and 0<=ny<len(shape):
                    if shape[ny][nx] in color and (nx,ny) not in visited:
                        queue.append((nx,ny))
    for visit in visited:
        shape[visit[1]][visit[0]]=0

N=int(input())
basic_shape=[]
for i in range(N):
    line=list(input())
    basic_shape.append(line)

normal=0
norm_shape=copy.deepcopy(basic_shape)
for i in range(N):
    for j in range(N):
        if norm_shape[j][i]!=0:
            norm((i,j),norm_shape)
            normal+=1

weakend=0
weak_shape=copy.deepcopy(basic_shape)
for i in range(N):
    for j in range(N):
        if weak_shape[j][i]!=0:
            weak((i,j),weak_shape)
            weakend+=1

print(normal,weakend)