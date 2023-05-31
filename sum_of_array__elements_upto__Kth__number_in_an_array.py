n=int(input())
l=map(int,input().split())
k=int(input())
c=0
for i in l:
    c+=i
    if i==k:
        break
print(c)