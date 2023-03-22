lst=[]
sum=0
for i in range(5):
    num=int(input())
    lst.append(num)
    sum+=num

print(int(sum/5))
lst.sort()
print(lst[2])