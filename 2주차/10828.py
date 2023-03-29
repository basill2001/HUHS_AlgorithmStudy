import sys

stack=[]
N=int(sys.stdin.readline())

for i in range(N):
    command=sys.stdin.readline().strip()
    if command[:4]=="push":
        stack.append(int(command[5:]))
    elif command=="pop":
        if len(stack)!=0:
            print(stack.pop())
        else:
            print(-1)
    elif command=="size":
        print(len(stack))
    elif command=="empty":
        if len(stack)==0:
            print(1)
        else:
            print(0)
    elif command=="top":
        if len(stack)==0:
            print(-1)
        else:
            print(stack[len(stack)-1])