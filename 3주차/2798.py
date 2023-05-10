from itertools import combinations

# N장의 카드 중 M을 넘지 않으면서 최대한 가까운 3장의 카드 고르기
N,M=map(int,input().split())
# 주어진 카드 숫자들
card=list(map(int,input().split()))

# 최댓값 저장
maxi=0
# 가능한 카드 조합들
comb=list(combinations(card,3))
for card in comb:
    card_sum=sum(card)
    # 카드 합이 M이면 이론상 최대
    if card_sum==M:
        maxi=M
        break
    # M을 넘지 않으면서 지금껏 최대보다 크면 지금이 최대
    elif card_sum<M and maxi<card_sum:
        maxi=card_sum
            
print(maxi)