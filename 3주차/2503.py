#숫자 생성
pred=[]
for i in range(1,10):
    for j in range(1,10):
        for k in range(1,10):
            if i!=j and j!=k and k!=i:
                pred.append(str(100*i+j*10+k))

# 예측
def prediction(num,strike,ball,given):
    num=str(num)
    lst=[[number] for number in given]
    for i in range(len(given)):
        number=given[i]
        cnt_s=0
        cnt_b=0
        for j in range(3):
            # 스트라이크
            if number[j]==num[j]:
                cnt_s+=1
            # 볼
            elif number[j] in num:
                cnt_b+=1
        lst[i].append(cnt_s)
        lst[i].append(cnt_b)

    result=[]
    for number in lst:
        if number[1]==strike and number[2]==ball:
            result.append(number[0])
    
    return result

N=int(input())
goal=[]
for i in range(N):
    quest,strike,ball=input().split()
    if i==0:
        goal=prediction(quest,int(strike),int(ball),pred)
    else:
        goal=prediction(quest,int(strike),int(ball),goal)

print(len(goal))
