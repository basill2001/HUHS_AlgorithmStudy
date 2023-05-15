N=int(input())
dist=list(map(int,input().split()))
oil_cost=list(map(int,input().split()))

# 지금까지 중 제일 oil cost가 작은 동네에서 기름 넣기
cur_min=oil_cost[0]
mins=[0]
for i in range(1,len(oil_cost)-1):
    if oil_cost[i]<cur_min:
        cur_min=oil_cost[i]
        mins.append(i)

# 그 다음 min까지 묶기
dist_bind=[]
for i in range(len(mins)):
    village=mins[i]
    if i<len(mins)-1:
        next_village=mins[i+1]
        bind=sum(dist[village:next_village])
    else:
        bind=sum(dist[village:])
    dist_bind.append(bind)

tot_cost=0
for i in range(len(dist_bind)):
    tot_cost+=dist_bind[i]*oil_cost[mins[i]]
print(tot_cost)