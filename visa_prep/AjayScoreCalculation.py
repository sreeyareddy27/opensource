s=int(input())
for i in range(s):
    a,b=map(int,input().split())
    q=a//10
    r=q*b
    print(r)
