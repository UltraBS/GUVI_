num=int(input())
n=num
a=0
while(n!=0):
    t=n%10;
    a=a+t**3
    n=n//10
if(num==a):
    print("yes")
else:
    print("no")