num=int(input("enter number="))

sum=0

for i in range(1,num):
    if num%i == 0:
        sum+=i

if num == sum :
    print(f"{num} is a perfect number")
else:
    print(f"{num} is not a perfect number")