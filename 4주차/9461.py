import copy

shape=[[0,1,0,1,0,1],[0,1,1,0,1,1],[0,2,0,1,1,1]]
lengths=[1,1,1]

def P(N):
    if N<=len(shape):
        return lengths[N-1]
    else:
        while len(shape)<N:
            zero_index=shape[-1].index(0)
            length=shape[-1][(zero_index+1)%6]
            lengths.append(length)
            newtri=copy.deepcopy(shape[-1])
            newtri[(zero_index)%6]+=length
            newtri[(zero_index+1)%6]-=length
            newtri[(zero_index+2)%6]+=length
            shape.append(newtri)
    return length

T=int(input())
for i in range(T):
    N=int(input())
    print(P(N))