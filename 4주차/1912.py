import sys

n=int(input())
lst=list(map(int,sys.stdin.readline().rstrip().split()))

maxtill=lst[0]
summation=lst[0]

for i in range(1,n):
    if lst[i]>=summation+lst[i]:
        summation=lst[i]
    else:
        summation+=lst[i]
    if summation>maxtill:
        maxtill=summation

print(maxtill)
# 10 -4 3 1  5  6  -35 12 21 -1
# 10  6 9 10 15 21 -14 7  6
#       3
#                  -35 
#                      12 33 32

# 2 1 -4 3 4 -4 6 5  -5 1
# 2 3 -1 
#     0  3 7 3  9 14  9 
#            0
#                     0 1

# -1 -2 -3 -4 -5
# -1
#    -2 