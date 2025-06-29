#WAP a program find the sum of 3digits
num=int(input("enter the num:"))
a=num%10
num=num//10
c=num%10
d=num//10
sum=(a+c+d)
print("sum of three digit num:",sum)