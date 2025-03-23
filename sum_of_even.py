n=int(input("enter last number"))
sum=0
for i in range(1,n+1):
    if i%2==0:
        print(i)
        sum=sum+i
print("sum of even numbers of range ", + n ,"is", +sum)