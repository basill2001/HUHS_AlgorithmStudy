import sys
N=int(input())

X=list(map(int,sys.stdin.readline().split()))

X_set=list(set(X))
X_set.sort()

dic={}
for i in range(len(X_set)):
    dic[X_set[i]]=i

for num in X:
    print(dic[num],end=" ")

# 시간초과를 dictionary로 해결