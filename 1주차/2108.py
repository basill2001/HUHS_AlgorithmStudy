import sys
from collections import Counter

N=int(input())

#수 배열 받기
nums=[]
sum
for i in range(N):
    nums.append(int(sys.stdin.readline()))

#산술평균
aver=sum(nums)/N
print(round(aver))

#중앙값
nums.sort()
mid=int(N/2-0.5)
print(nums[mid])

#최빈값
mode=Counter(nums).most_common()
if len(mode)>1 and mode[0][1]==mode[1][1]:
    print(mode[1][0])
else:
    print(mode[0][0])

#범위
print(nums[N-1]-nums[0])

##probs : 시간 초과, Counter import해서 해결