import math
p,q=map(int,input().split())
c=p*100
d=math.ceil(q/100)
print(max(0,d-p))
