# 가지고 있는 동전 N 종류
# 가치의 합을 K개로
coins={}
N,K=map(int,input().split())
for i in range(N):
    worth=int(input())
    coins[worth]=0

# 동전 종류 리스트
keys=list(coins.keys())
keys.reverse()

# 구하기
left=K
for key in keys:
    a,b=divmod(left,key)
    if a>=1:
        left=b
        coins[key]=a
    if left==0:
        break

print(sum(coins.values()))