import sys
from collections import deque

N=int(input())
dq=deque()

for i in range(N):
    command=sys.stdin.readline().strip()

    ## push
    if command[:10]=="push_front":
        dq.appendleft(int(command[11:]))
    elif command[:9]=="push_back":
        dq.append(int(command[10:]))
    ## pop
    elif command[:3]=="pop":
        if len(dq)==0:
            print(-1)
        elif command=="pop_front":
            print(dq.popleft())
        elif command=="pop_back":
            print(dq.pop())
    ## size, empty
    elif command=="size":
        print(len(dq))
    elif command=="empty":
        if len(dq)==0:
            print(1)
        else:
            print(0)
    ## front, back
    elif command=="front" or command=="back":
        if len(dq)==0:
            print(-1)
        elif command=="front":
            print(dq[0])
        elif command=="back":
            print(dq[len(dq)-1])