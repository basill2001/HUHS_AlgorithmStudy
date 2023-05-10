# N,M 크기의 직사각형 받기
N,M=map(int,input().split())
rectangle=[]

for i in range(N):
    rectangle.append(input())

# 정사각형의 최대 크기를 더 짧은 변의 길이로
sq=min(N,M) 

# 한 변이 size인 정사각형의 꼭짓점에 쓰여있는 수가 모두 같은지
def check(size):
    size=size-1
    for i in range(N-(size)):
        for j in range(M-(size)):
            if rectangle[i][j]==rectangle[i][j+size]==rectangle[i+size][j+size]==rectangle[i+size][j]:
                return True
            else:
                continue             

for size in range(sq,0,-1): # size를 역순으로
    if check(size)==True:
        print(size**2)
        break
