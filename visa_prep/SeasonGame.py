p=int(input())
if (p>=3 and p<6):
    print("Spring")
elif(p>=6 and p<9):
    print("Summer")
elif(p>=9 and p<12):
    print("Autumn")
elif((p>=1 and p<3) or p==12):
    print("Winter")
else:
    print("Invalid")
