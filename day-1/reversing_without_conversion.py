a= int(input())
reverse=0
while a>0:
    k=a%10
    a=a//10
    reverse=(reverse*10)+k
print(reverse)



a=input()
c=0
for i in a:
    num=int(i)
    c=c+num
print(c)



a= int(input())
sum=0
while a>0:
    k=a%10
    sum=sum+k
    a=a//10
print(sum)
