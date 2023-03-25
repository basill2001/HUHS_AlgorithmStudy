N=int(input())

#입력받기
dots=[]
for i in range(N):
    x,y=map(int,input().split())
    dots.append((y,x))

#정렬하기
dots.sort()

#출력하기
for dot in dots:
    print(dot[1],dot[0])