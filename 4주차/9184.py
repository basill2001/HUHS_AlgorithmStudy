call={1:0,2:0,3:0,4:0}
W={}


def w(a,b,c):
    if (a,b,c) in list(W.keys()):
        return W[a,b,c]
    else:
        if a<=0 or b<=0 or c<=0:
            call[1]+=1
            return 1
        elif a>20 or b>20 or c>20:
            call[2]+=1
            return w(20,20,20)
        elif a<b and b<c:
            W[a,b,c]=w(a,b,c-1)+w(a,b-1,c-1)-w(a,b-1,c)
            call[3]+=1
            return W[a,b,c]
        else:
            W[a,b,c]=w(a-1,b,c)+w(a-1,b-1,c)+w(a-1,b,c-1)-w(a-1,b-1,c-1)
            call[4]+=1
            return W[a,b,c]


while True:
    a,b,c=map(int,input().split())
    if a==-1 and b==-1 and c==-1:
        break
    else:
        print("w(%d, %d, %d) =" %(a,b,c),w(a,b,c))