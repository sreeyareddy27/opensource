X,Y,Z = list(map(int, input().split()))
if X + Y <= Z:
    print(2)
elif X<=Z:
    print(1)
else:
    print(0)
