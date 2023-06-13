import math
a,b,c=map(int,input().split())
s=(a+b+c)/2
area=s*(s-a)*(s-b)*(s-c)
print('%.2f'%math.sqrt(area))