n,k=list(map(int,input().split()))
time=240-k
count=0
for i in range(1,n+1):
  c=5*i
  time=time-c
  if time<0:
    break
  count+=1
print(count)