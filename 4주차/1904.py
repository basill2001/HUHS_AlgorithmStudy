lst=[1,2]
N=int(input())
while len(lst)<N:
    lst.append((lst[-1]+lst[-2])%15746)

print(lst[N-1]%15746)