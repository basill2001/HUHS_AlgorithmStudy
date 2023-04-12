from itertools import combinations

N=int(input())
lst=[]
# 9876543210 -> 10자리 수
for i in range(1,11):
    for num in combinations(range(0,10),i):
        num=sorted(list(num),reverse=True)
        num="".join(str(digit) for digit in num)
        lst.append(int(num))
        
lst.sort()

if N<len(lst):
    print(lst[N])
else:
    print(-1)