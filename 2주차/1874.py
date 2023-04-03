import sys
input=sys.stdin.readline

lst=[]
cnt=1
n=int(input())
for i in range(n):
    num=int(input())
    lst.append(num)

stack=[0]
j=0
process=[]
for i in range(len(lst)):
    while True and j<=n:
        if stack[-1]!=lst[i]:
            stack.append(j+1)
            j+=1
            process.append("+")
        elif stack[-1]==lst[i]:
            stack.pop()
            process.append("-")
            break

if stack==[0]:
    for i in range(len(process)):
        print(process[i])
else:
    print("NO")