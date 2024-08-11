text=" Hello, World! "

print("1.capitalize() =",text.capitalize())

print("2.center() =",text.center(20,'*'))

print("3.count() =",text.count(' '))

print("4.endswith() =",text.endswith('!'))

print("5.find()=",text.find('d'))


print("6.format()")

name ="Rohan Ridhar"
age = 20

text2="my name is {} amd i'm {} years old".format(name,age)
print(text2)

print("7.format_map()")

info={"name": "Riya Riddi", "age" : 20}
text3="my name is {name} and i'm {age} years old".format_map(info)
print(text3)

print("7.index()",text.index(" Hello"))

texts="hello"
print("8.isalpha()",texts.isalpha())

print("9.isalnum()")

text4="number12345"
print(text4.isalnum())

print("10.isnumeric() and isdigit()=")

text5="123456"
texts5="123"
print(text5.isnumeric())
print(texts5.isdigit())

print("11. isdecimal() =")

text6="125.12"
print(text6.isdecimal())

print("12. isspace()=")

text7="       "
print(text7.isspace())

print("13.islower() and isupper() , lower() and upper()=")

text8="hello"
text9="WORLD"
print(text8.islower())
print(text9.isupper())
print(text9.lower())
print(text8.upper())


print("14. translate() and maketrans()")

text10="Hello Aishwarya !"
trans_table=str.maketrans("aeioul","123456")
print(text10.translate(trans_table))


print("15.partition()=",text.partition("World"))

print("16.replace()=",text.replace("o","x"))

print("17.split()= ", text.split(","))

print("18.splitlines()=")

multiline="hello\nWorld"
print(multiline.splitlines())

print("19.strip() =", text.strip())

print("20.startswith()=",text.startswith(" H"))

print("21.swapcase()=")

text11="good"
print(text11.swapcase())

text12="fill"
print("22.zfill()=", text12.zfill(10)) #pad a string with zeros on the left side until it reaches a specified width.







