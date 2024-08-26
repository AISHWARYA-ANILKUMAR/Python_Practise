num = int(input("Enter a number: "))

if num < 0 :
    print("negative numbers are not prime")
elif num <=1 :
    print("1 or less is not prime")
    
else:
    lim=int(num**0.5)+1
    for i in range(2,lim):
        rem=num%i
        if rem == 0:
            print(f"{num} is not prime")
            break
    else:
            print(f"{num} is prime")
    
