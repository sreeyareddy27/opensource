f=int(input())
if(f%4==0 and f%100!=0):
    print("YES")
elif(f%400==0 and f%100==0):
    print("YES")
else:
    print("NO")
