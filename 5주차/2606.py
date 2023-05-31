com=int(input())
computer=[i for i in range(1,com)]
connections={i:[] for i in range(1,com+1)}
conn=int(input())
for i in range(conn):
    a,b=map(int,input().split())
    connections[a].append(b)
    connections[b].append(a)
for i in range(com):
    connections[i+1].sort()

def spread(graph):
    infected=[]
    soontobe=[1]
    while len(soontobe)!=0:
        node=soontobe.pop(0)
        if node not in infected:
            infected.append(node)
            child=list(set(graph[node])-set(infected))
            child.sort()
            soontobe.extend(child)
    return infected

print(len(spread(connections))-1)