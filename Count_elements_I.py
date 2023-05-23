n,m=map(int,input().split())
l=set(map(int,input().split()))
k=set(map(int,input().split()))
c=0
for i in l:
    if i in k:
        c+=1
print(c)