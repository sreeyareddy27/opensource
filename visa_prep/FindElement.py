def bs(a,t):
    l,h=0,len(a)-1
    while l<=h:
        m=(l+h)//2
        if a[m]==t:
            return m
        elif a[m]<t:
            l=m+1
        else:
            h=m-1
    return -1
n=int(input())
a=list(map(int,input().split()))
t=int(input())
r=bs(a,t)
print(r)
