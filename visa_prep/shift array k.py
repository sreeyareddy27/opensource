n=int(input())
arr=list(map(int,input().split()))
k=int(input())
k=k%n
a=arr[-k:]+arr[:-k]
print(*a)
