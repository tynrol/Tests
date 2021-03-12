t=int(input())
def f(n,k):
    inT=n//k
    overT=n%k
    sum=0
    for i in range(overT):
        n-=inT+1
        sum+=n*(inT+1)
    for i in range(k-overT):
        n-=inT
        sum+=n*inT
    return sum

for i in range(t):
    n,k=map(int,input().split())
    print(f(n,k))
    

