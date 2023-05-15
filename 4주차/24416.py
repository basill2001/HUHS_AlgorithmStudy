call={1:0, 2:0}
fibo=[1,1]

# 동적계획법
def fibonacci(n):
    for i in range(3,n+1):
        fibo.append(fibo[-1]+fibo[-2])

n=int(input())
fibonacci(n)
call[1]=fibo[-1]
call[2]=n-2
print(call[1],call[2])