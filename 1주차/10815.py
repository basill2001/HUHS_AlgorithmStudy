import sys

N=int(input())
card=set(map(int,sys.stdin.readline().split()))
# set이 O(1)으로 시간초과가 나지 않음

M=int(input())
integers=list(map(int,sys.stdin.readline().split()))

yn=[]
for i in range(M):
    if integers[i] in card:
        yn.append(1)
    else:
        yn.append(0)

for i in range(M):
    print(yn[i],end=" ")