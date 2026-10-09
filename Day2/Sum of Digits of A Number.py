n=int(input())
digit=0
sum=0
while n>0:
    digit=n%10
    sum+=digit
    n=n//10
print(sum)