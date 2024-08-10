
txt = "The best things in life"

print("1. strings are arrays\n")

print(txt[2])

print("\n2. Looping through strings\n")

for item in txt :
    print(item)
    
print("\n3.Length of strings\n")

print(len(txt))

print("\n4.Check presence of words in string\n")

if "life" in txt :
    print("yes, present")
    
if "lie" not in txt :
    print("Not, present")
    