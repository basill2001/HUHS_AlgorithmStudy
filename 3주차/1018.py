import sys
input=sys.stdin.readline

N,M=map(int,input().split())
# Board 만들기
board=[]
for i in range(N):
    row=input()
    board.append(row)

#칸마다 몇 개를 칠해야 하는지 저장
Cnt=[]
# 각 칸에서 시작
for i in range(N-7):
    for j in range(M-7):
        paint1=0 # 시작점이 B
        paint2=0 # 시작점이 W
        # 8x8 체스판 마다
        for k in range(i, i+8):
            for l in range(j,j+8):

                # 합이 짝수인 칸은 시작점과 색이 같고
                # 합이 홀수인 칸은 시작점과 색이 달라야 한다

                if (k+l)%2==0: # 합이 짝수인 칸
                    if board[k][l]=="W": # W이면
                        paint1+=1 # 시작점이 B일 경우 B로 칠하기
                    else: # B이면
                        paint2+=1 # 시작점이 W일 경우 B로 칠히기
                else: # 합이 홀수인 칸
                    if board[k][l]=="B": # B이면
                        paint1+=1 # 시작점이 B일 경우 W로 칠하기
                    else: # w이면
                        paint2+=1 # 시작점이 W일 경우 B로 칠하기
        Cnt.append(paint1) # 시작점이 B일 경우 총 칠한 개수
        Cnt.append(paint2) # 시작점이 W일 경우 총 칠한 개수

print(min(Cnt))
            