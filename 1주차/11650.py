N=int(input())

#입력받기
dots=[]
for i in range(N):
    x,y=map(int,input().split())
    dots.append((x,y))

#정렬하기
dots.sort()

#출력하기
for dot in dots:
    print(dot[0],dot[1])