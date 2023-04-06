N=int(input())

# number는 생성자, M은 분해합
def decompose(number):
    N=str(number)
    M=number
    for i in range(len(N)):
        M+=int(N[i])
    return M

i=0
while i<=N:
    if decompose(i)==N:
        print(i)
        break
    
for i in range(N):
    if decompose(i)==N:
        print(i)
        break