b,c=map(int,input().split())
if(b==0 and c%2==0):
    print("YES")
elif(b==0 and c%2!=0):
    print("NO")
elif((b+2*c)%2==0):
    print("YES")
else:
    print("NO")