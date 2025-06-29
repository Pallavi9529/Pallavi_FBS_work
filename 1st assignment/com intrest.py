#WAP to enter P,T,R and calculate compound interst

p=int(input("enter princple:"))
t=int(input("enter no of time:"))
r=int(input("enter rate of rate:"))
n=int(input("enter the n:"))
a=(p*(1+r/n))**(n*t)
print("compound intrest:",a)