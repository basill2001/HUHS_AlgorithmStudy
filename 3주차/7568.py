import sys
input=sys.stdin.readline

# 사람 입력받기
N=int(input())
lst=[]
for i in range(N):
    x,y=map(int,input().split())
    lst.append((x,y))

order=[]
# 각 사람마다
for i in range(N):
    # 덩치가 더 큰 사람 명수
    bigger=0
    for j in range(N):
        if lst[i][0]<lst[j][0] and lst[i][1]<lst[j][1]:
            bigger+=1
    order.append(bigger+1)

# 출력
for big in order:
    print(big,end=" ")
        