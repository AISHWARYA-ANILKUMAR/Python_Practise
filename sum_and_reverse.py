num=int(input("enter number="))

sum=0
rev=0
temp=num # we use temp becuz after while num becomes zero

while(temp>0):
    rem=temp%10
    sum+=rem
    rev=rev*10+rem
    temp=temp//10
    
print(f"Reverse of {num} is {rev}")
print(f"sum of digits of {num} is {sum}")
    
    