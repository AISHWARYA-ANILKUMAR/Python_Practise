
n1=int(input("Enter first number : "))
n2=int(input("Enter second number : "))


print("Before swap :"+str(n1)+", "+str(n2))
temp=n1
n1=n2
n2=temp
print("After swap :"+str(n1)+" ,"+str(n2))

print(type(n1))
print(type(n2))