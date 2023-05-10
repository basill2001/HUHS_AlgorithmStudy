N=int(input())

num=0 # marker
count=0 # 찾은 종말의 수의 개수

# num을 1씩 증가해가며 종말의 수이면 count를 증가시키기
# count==N이면 num은 N번째 종말의 수
while count<N:
    num+=1
    if "666" in str(num):
        count+=1
print(num)
