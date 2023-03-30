import sys

queue=[]
N=int(sys.stdin.readline())

for i in range(N):
    command=sys.stdin.readline().strip()
    if command[:4]=="push":
        queue.append(int(command[5:]))
    elif command=="pop":
        if len(queue)!=0:
            print(queue[0])
            del queue[0]
        else:
            print(-1)
    elif command=="size":
        print(len(queue))
    elif command=="empty":
        if len(queue)==0:
            print(1)
        else:
            print(0)
    elif command=="front" or command=="back":
        if len(queue)==0:
            print(-1)
        elif command=="front" and len(queue)!=0:
            print(queue[0])
        elif command=="back" and len(queue)!=0:
            print(queue[len(queue)-1])