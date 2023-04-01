from collections import deque

N=int(input())
pile=deque()

pile.append(N)
for i in range(N-1,0,-1):
    pile.appendleft(i)
    for j in range(i):
        pile.rotate(1)

for card in pile:
    print(card,end=" ")


## in first pile of cards
# 1st card-> last
# 2nd card=1
# 3rd card-> last
# 4th card-> last
# 5th card=2
# 6th card-> last
# 7th card-> last
# 8th card-> last
# 9th card=3

# 1개
# [1]->[1]
# [1]!

# 2개
# [2 1]->[1 2]
# [2]

# 3개
# [3 1 2]->[1 2 3]
# [2 3]->[3 2]->[2 3]
# [3]

# 4개
# [2 1 4 3]->[1 4 3 2]
# [4 3 2]->[3 2 4]->[2 4 3]
# [4 3]->[3 4]->[4 3]->[3 4]
# [4]
