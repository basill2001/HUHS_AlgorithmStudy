
N=int(input())

maximum=0
max_list=[]

def test(x):
    lst=[N]
    cnt=1
    lst.append(x)
    while lst[-1]>=0:
        lst.append(lst[-2]-lst[-1])
        cnt+=1
    if lst[-1]<0:
        del lst[-1]
    return lst

if N>1:
    for i in range(1,N):
        lst=test(i)
        if len(lst)>maximum:
            maximum=len(lst)
            max_list=lst
elif N==1:
    if len(test(1))>maximum:
            maximum=len(test(1))
            max_list=test(1)
        
print(maximum)
for i in range(maximum):
    print(max_list[i],end=" ")
