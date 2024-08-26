num = int(input("Enter the number: "))


if num < 0:
    print(f"{num} is not an Armstrong number (Armstrong numbers are non-negative).")
else:
    temp = num
    sum = 0

    while temp > 0:  
        rem = temp % 10  
        sum += rem ** 3
        temp = temp // 10  

   
    if num == sum:
        print(f"{num} is an Armstrong number.")
    else:
        print(f"{num} is not an Armstrong number.")
