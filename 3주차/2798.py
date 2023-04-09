#카드의 개수 N, M
#주어진 카드
N,M=map(int,input().split())
card=list(map(int,input().split()))

maxi=0
for c in range(2,N):
    for b in range(1,c):
        for a in range(b):
            card_sum=card[a]+card[b]+card[c]
            if card_sum==M:
                maxi=M
                break
            elif card_sum<M and maxi<card_sum:
                maxi=card_sum
            
print(maxi)