num=int(input())
rnum=0
n=num
while(num!=0):
  t=num%10
  rnum=rnum*10+t
  num=int(num/10)
if(n==rnum):
  print("yes")
else:
  print("no")
