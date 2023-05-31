import sys
from collections import deque
N,M=map(int,input().split())
graph={i:[] for i in range(1,N+1)}

for i in range(M):
    u,v=map(int,sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

def BFS(graph):
    cnt=0
    while len(graph)!=0:
        queue=deque([list(graph.keys())[0]])
        cnt+=1
        while len(queue)!=0:
            node=queue.popleft()
            for k in graph[node]:
                if k in graph and k not in queue:
                    queue.append(k)
            del graph[node]
    return cnt

print(BFS(graph))