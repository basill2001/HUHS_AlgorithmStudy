import sys
N=int(input())
x=[]
for i in range(N):
    x.append(int(sys.stdin.readline()))

x.sort()
for i in range(N):
    print(str(x[i]))