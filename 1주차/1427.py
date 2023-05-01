# 입력받기
N=input()
digit=len(N)

# 자릿수 별로 분리
numbers=[]
for i in range(digit):
    numbers.append(int(N[i]))
# 정렬
numbers.sort(reverse=True)

# 출력
for n in numbers:
    print(n,end="")