
a=" Hello, World "

print(a.upper()) #HELLO, WORLD
print(a.lower()) #hello, world
print(a.strip()) # remove space from start and end
print(a.split(",")) # split from , ['Hello', 'world']
print(a.replace("H", "J")) #Jello, World

print("----concatenate strings--------")

x = "hello"
y = "world"

print("concatenated =" + x + y)
print("concatenated with space = " + x + " " + y)

print("--escape characters---------")
txt = "We are the so-called \"Vikings\" from the north."
print(txt)
