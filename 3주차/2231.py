N=int(input())

# number는 생성자, M은 분해합
def decompose(number):
    N=str(number)
    M=number
    for i in range(len(N)):
        M+=int(N[i])
    return M

generator=0 # 생성자가 없는 경우엔 0을 출력 
for i in range(N):
    # 가장 작은 생성자 구하기
    if decompose(i)==N:
        generator=i 
        break
print(generator)