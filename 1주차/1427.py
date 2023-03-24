N=input()
digit=len(N)
numbers=[]
for i in range(digit):
    numbers.append(int(N[i]))
numbers.sort(reverse=True)

for n in numbers:
    print(n,end="")