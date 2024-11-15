N = int(input())
for n in range(0,N):
    X,Y=map(int,input().split())
    if X<=Y:
        print("0")
    else:
        print(X-Y)
