a,b=map(int,input().split())
l=list(map(int,input().split()))
d=0
nd=0
for k in l:
    if(k%b==0):
        d+=k
    else:
        nd+=k
print(d-nd)
