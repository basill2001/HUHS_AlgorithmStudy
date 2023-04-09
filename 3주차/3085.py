N=int(input())
candies=[]
for i in range(N):
    candies.append(list(input()))

def continuity(board):
    maximum1=1
    maximum2=1
    for i in range(N):
        #행별로
        row=1
        for j in range(1,N):
            if board[i][j-1]==board[i][j]:
                row+=1
                if maximum1<row:
                    maximum1=row
            else:
                row=1
            
        #열별로
        column=1
        for j in range(1,N): 
            if board[j-1][i]==board[j][i]:
                column+=1
                if maximum2<column:
                    maximum2=column
            else:
                column=1
    return max(maximum1,maximum2)

    
maximum=0
for i in range(N):
    for j in range(N-1):
        # 행에서 교환
        candies[i][j],candies[i][j+1]=candies[i][j+1],candies[i][j]
        cnt1=continuity(candies)
        if cnt1>maximum:
            maximum=cnt1
        candies[i][j],candies[i][j+1]=candies[i][j+1],candies[i][j]

        # 열에서 교환
        candies[j][i],candies[j+1][i]=candies[j+1][i],candies[j][i]
        cnt2=continuity(candies)
        if cnt2>maximum:
            maximum=cnt2
        candies[j][i],candies[j+1][i]=candies[j+1][i],candies[j][i]

print(maximum)