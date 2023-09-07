a= '153'
cat=int(a)
c=0

for i in a:
    num= int(i)
    l=num**len(a)
    c=c+l
if c == cat:
    print("yes")
else:
    print("no")
    

