formula=input()

# -를 기준으로 입력받기
numbers=[]
num=str()
for i in formula:
    if i.isdigit() or i=="+":
        num+=i
    else:
        numbers.append(num)
        num=str()    
numbers.append(num)

# 항을 각자 더해서 출력하는 함수
def process(num):
    cut=[]
    i=0
    n=str()
    for i in range(len(num)):
        if num[i].isdigit():
            n+=num[i]
        else:
            cut.append(int(n))
            n=str()
    cut.append(int(n))
    return sum(cut)

for i in range(len(numbers)):
    numbers[i]=process(numbers[i])

result=numbers[0]
for i in range(1,len(numbers)):
    result-=numbers[i]
print(result)