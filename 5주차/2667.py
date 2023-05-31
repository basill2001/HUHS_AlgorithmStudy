from collections import deque

def buildconnection(graph,a,b,c,d):
    try:
        graph[(a,b)].append((c,d))
    except KeyError:
        graph[(a,b)]=[(c,d)]

def buildgraph(given,N):
    graph={}
    for i in range(N):
        for j in range(N):
            if given[i][j]==1 and (j,i) not in graph:
                graph[(j,i)]=[]
            if given[i][j]==1:
                if (i+1<N and j<N) and given[i+1][j]==1:
                    buildconnection(graph,j,i,j,i+1)
                    buildconnection(graph,j,i+1,j,i)
                if (j+1<N and i<N) and given[i][j+1]==1:
                    buildconnection(graph,j,i,j+1,i)
                    buildconnection(graph,j+1,i,j,i)
    return graph
            
def BFS(gard,v):
    tovisit=deque([v])
    visited=[]
    while tovisit:
        node=tovisit.popleft()
        if node not in visited:
            visited.append(node)
            child=list(set(gard[node])-set(visited))
            del gard[node]
            child.sort()
            tovisit.extend(child)
    return len(visited)

N=int(input())
gard=[]
for i in range(N):
    line=list(map(int,list(input())))
    gard.append(line)
gard=(buildgraph(gard,N))

cnt=[]
while gard:
    search=list(gard.keys())[0]
    num=BFS(gard,search)
    cnt.append(num)

cnt.sort()
print(len(cnt))
for j in cnt:
    print(j)