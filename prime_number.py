def prime(num):
    if num <2:
        return False
    for i in range(2,num):
        if num%1==0:
            return False
    return True
num=int(input("enter a number: "))
if prime(num):
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")