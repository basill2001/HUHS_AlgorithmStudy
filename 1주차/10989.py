import sys
N=int(input())

#길이가 10001인 배열 만들기
counts=[0]*10001

#같은 숫자 세기
for i in range(N):
    a=int(sys.stdin.readline())
    counts[a]+=1

#나온 수만큼 출력
for i in range(10001):
    if counts[i]!=0:
        for j in range(counts[i]):
            print(i)