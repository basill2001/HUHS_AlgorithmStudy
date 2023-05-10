from itertools import combinations

N=int(input())
lst=[]
# 9876543210 -> 10자리 수

# 1자리 수 ~ 10자리 수
for i in range(1,11):
    # 0~9 중 i개를 뽑아서 만든 combination
    for num in combinations(range(0,10),i):
        num=sorted(list(num),reverse=True) # 역순으로 정렬
        num="".join(str(digit) for digit in num) # 리스트 합쳐서 숫자로
        lst.append(int(num))
        
lst.sort() # 오름차순으로 정렬

if N<len(lst): # lst 안에 있으면
    print(lst[N]) # N번째 감소하는 수 출력
else: # 안에 없으면
    print(-1) # -1 출력