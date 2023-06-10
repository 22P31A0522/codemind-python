a=int(input())
if a<=199:
    u=1.20
elif a>=200 and a<400:
    u=1.40
elif a>=400 and a<600:
    u=1.60
elif a>=600 and a<800:
    u=1.80
else:
    u=2.00
    
Bill=a*u
if Bill>400:
    s=0.15*Bill;
else:
    s=0
    
print("Units Consumed:",a)
print("Cost per Unit:",'%.2f'%u)
print("Bill:",'%.2f'%Bill)
print("Surcharge:",'%.2f'%s)
print("Total Amount:",'%.2f'%(Bill+s))