N,M=map(int,input().split())
rectangle=[]

for i in range(N):
    rectangle.append(input())

sq=min(N,M)
horizon=False
if N==sq:
    horizon=True

def check(rec,size):
    size=size-1
    for i in range(N-(size)):
        for j in range(M-(size)):
            if rec[i][j]==rec[i][j+size]==rec[i+size][j+size]==rec[i+size][j]:
                return True
            else:
                continue             

for size in range(sq,0,-1):
    if check(rectangle,size)==True:
        print(size**2)
        break
