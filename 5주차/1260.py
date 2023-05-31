from collections import deque

def DFS(graph_DFS,start):
    tovisit=[start]
    visited=[]
    while len(tovisit)!=0:
        node=tovisit.pop()
        if node not in visited:
            visited.append(node)
            if node in graph_DFS:
                temp=list(set(graph_DFS[node])-set(visited))
                temp.sort(reverse=True)
                tovisit+=temp
    return visited

def BFS(graph_BFS,start):
    tovisit=deque([start])
    visited=[]
    while len(tovisit)!=0:
        node=tovisit.popleft()
        if node not in visited:
            visited.append(node)
            child=[]
            for j in graph_BFS[node]:
                if j not in visited:
                    child.append(j)
            tovisit.extend(child)
    return visited

def buildgraph(n,edges):
    graph={}
    for i in range(n):
        graph[i+1]=[]
    for e in edges:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])
    for i in range(n):
        graph[i+1].sort()
    return graph

N,M,V=map(int,input().split())
edge=[]
for m in range(M):
    edge.append(list(map(int,input().split())))
grph=buildgraph(N,edge)
dfs=DFS(grph,V)
grph=buildgraph(N,edge)
bfs=BFS(grph,V)

for d in dfs:
    print(d,end=" ")
print()
for b in bfs:
    print(b,end=" ")