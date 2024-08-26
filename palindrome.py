num=int(input("enter number="))


rev=0
temp=num
rem=0

while(num > 0):
    
    rem=int(num%10)
    rev=rev*10+rem
    num=num//10
   
if(rev == temp):
    print(f"{temp} is Palindrome")
else:
    print(f"{temp} is not palindrome")
    
    