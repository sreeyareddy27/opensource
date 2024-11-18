a=int(input())
l=list(map(int,input().split()))
c=0
k=0
for i in l:
    if(i==0):
        c+=1
    else:
        k=max(k,c)
        c=0
k=max(k,c)
print(k)
