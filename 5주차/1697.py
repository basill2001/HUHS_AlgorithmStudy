# 틀렸습니다.

from collections import deque

N,K=map(int,input().split())

def split(lst):
    result=[]
    for i in range(len(lst)):
        result.append(lst[i]-1)
        result.append(lst[i]+1)
        result.append(lst[i]*2)
    return result

tree=deque([[N]])

def BFS(N):
    tree=deque([N])
    tovisit=deque([])

# print(BFS())