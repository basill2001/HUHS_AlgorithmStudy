import sys

K=int(input())
nums=[]
for i in range(K):
    num=int(sys.stdin.readline())
    if num==0:
        del nums[len(nums)-1]
    else:
        nums.append(num)

print(sum(nums))