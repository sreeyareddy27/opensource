a=int(input())
k=[list(map(int,input().split()))for i in range(a)]
for r in k:
    print(" ".join(map(str,r[::-1])))
