import sys

T=int(input())

for i in range(T):
    PS=sys.stdin.readline().strip()
    rght=0
    VPS=True
    for j in range(1,len(PS)+1):
        letter=PS[len(PS)-j]
        if letter==")":
            rght+=1
        elif letter=="(" and rght!=0:
            rght-=1
        else:
            VPS=False
            break
    if rght==0 and VPS!=False:
        print("YES")
    else:
        print("NO")