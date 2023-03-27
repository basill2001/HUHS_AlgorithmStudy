#온라인 저지 회원의 수
N=int(input())
member=[]

#각 회원의 나이와 이름
#가입한 순서대로 받기 위해 i 추가
for i in range(N):
    age,name=input().split()
    age=int(age)
    member.append((age,i,name))

#정렬하기
member.sort()

#출력
for i in range(N):
    print(member[i][0],member[i][2])