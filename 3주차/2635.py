# 첫번째 수
N=int(input())

# 두번째 수가 주어지면 규칙에 따라 리스트 만들기
def test(x):
    lst=[N]
    lst.append(x)
    while lst[-1]>=0: # 마지막 수가 음수가 아닌 동안
        # 앞의 앞의 수에서 앞의 수를 빼서 수 만들기
        lst.append(lst[-2]-lst[-1])
    # 음의 정수가 나오면 버리기
    if lst[-1]<0:
        del lst[-1]
    return lst

# 최대 리스트 저장
maximum=0
max_list=[]

# 2 이상이면
if N>1:
    for i in range(1,N): # 두번째 수
        lst=test(i) # 첫번째 수와 두번째 수가 주어졌을 때의 리스트
        # 최대 리스트면 저장
        if len(lst)>maximum:
            maximum=len(lst)
            max_list=lst
# 1이면
elif N==1:
    maximum=len(test(1))
    max_list=test(1)
        
print(maximum)
for i in range(maximum):
    print(max_list[i],end=" ")