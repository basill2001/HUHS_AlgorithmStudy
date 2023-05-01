import sys
input=sys.stdin.readline

N,M=map(int,input().split())
board=[]
for i in range(N):
    row=input()
    board.append(row)

Cnt=[]
for i in range(N-7):
    for j in range(M-7):
        paint1=0
        paint2=0
        for k in range(i, i+8):
            for l in range(j,j+8):
                if (k+l)%2==0:
                    if board[k][l]=="W":
                        paint1+=1
                    else:
                        paint2+=1
                else:
                    if board[k][l]=="B":
                        paint1+=1
                    else:
                        paint2+=1

        Cnt.append(paint1)
        Cnt.append(paint2)

print(min(Cnt))
            