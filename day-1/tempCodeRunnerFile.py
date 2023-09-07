a= int(input())
reverse=0
while a>0:
    k=a%10
    a=a//10
    reverse=(reverse*10)+k
print(reverse)