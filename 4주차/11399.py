# 사람 : 1번 ~ N번
# 각 Pi분 인출 시간
N=int(input())
P=list(map(int,input().split()))
P.sort(reverse=True)

tot_time=0
for i in range(N):
    tot_time+=sum(P)
    del P[0]

print(tot_time)