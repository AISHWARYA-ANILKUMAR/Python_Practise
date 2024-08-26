lim=int(input("enter limit = "))

f=0
s=1

print(f,end=' ')
print(s,end=' ')

for i in range(lim):
    
    t=f+s
    
    f=s
    s=t
    print(t,end=' ')
    
print()

print("The last print was to make the cursor on the next line , so the print statements coming after printing 't' will occur in the next line")

