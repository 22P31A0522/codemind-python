n=int(input())
s=0
a=0
for i in range(1,n+1):
    s+=i*i
    a+=i
b=a*a
d=s-b
print(abs(d))