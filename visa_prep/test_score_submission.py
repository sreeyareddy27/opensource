a,b,c=map(int,input().split())
p=0
for i in range(1,a):
    if i*b==c:
        p=p+1
if p>=1:
    print("YES")
else:
    print("NO")
