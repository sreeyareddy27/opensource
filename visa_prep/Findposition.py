n,k=map(int,input().split())
arr=list(map(int,input().split()))
arr.sort()
if k in arr:
    print(arr.index(k))
else:
    arr.append(k)
    arr.sort()
    print(arr.index(k))
