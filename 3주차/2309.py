from itertools import combinations

# 난쟁이들의 키 받기
heights=[]
for i in range(9):
    heights.append(int(input()))

# heights에서 7개 조합
for comb in combinations(heights,7):
    comb=list(comb)
    # 합이 100이면 정답
    if sum(comb)==100:
        comb.sort()
        for dwarf in comb:
            print(dwarf)
        break