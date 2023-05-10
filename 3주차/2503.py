# 숫자 생성
# 가능한 전체 숫자의 리스트
pred=[]
for i in range(1,10):
    for j in range(1,10):
        for k in range(1,10):
            if i!=j and j!=k and k!=i:
                pred.append(str(100*i+j*10+k))

# 예측
def prediction(num,strike,ball,given):
    num=str(num)
    # given의 숫자들마다 해당하는 스트라이크와 볼 구하기
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
        # given에 숫자, 스트라이크, 볼 함께 저장
        given[i]=[number,cnt_s,cnt_b]

    result=[]
    # 주어진 스트라이크와 볼과 같은 숫자들만 result에 저장
    for number in given:
        if number[1]==strike and number[2]==ball:
            result.append(number[0])
    # result 반환
    return result

N=int(input())
goal=[]
for i in range(N):
    quest,strike,ball=input().split()
    # 초기 설정
    # 전체 pred 중 조건에 맞는 숫자들만 goal에 저장
    if i==0:
        goal=prediction(quest,int(strike),int(ball),pred)
    # 주어진 goal 중 조건에 맞는 숫자들만 goal에 저장
    else:
        goal=prediction(quest,int(strike),int(ball),goal)

print(len(goal))
