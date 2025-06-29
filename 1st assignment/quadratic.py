#WAP to find root of a quadratic equations

a=int(input("enter the a:"))
b=int(input("enter the b:"))
c=int(input("enter the c:"))
ans=(b*b)-(4*a*c)
ans=ans**0.5
root1=(-b+ans)/(2*a)
root2=(-b-ans)/(2*a)
print("root1:",root1)
print("root2:",root2)
