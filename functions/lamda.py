lam = lambda x : x*x
print(lam(5)) #O/P  : 25

#multiple arguments
x = lambda a, b : a * b
print(x(5, 6))

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

myList=[1,2,3,4,5,6]
evenNum = filter(lambda x : x % 2 == 0 , myList)
print(list(evenNum)) #O/P : [2, 4, 6]

oddNum = filter(lambda x : x % 2 == 1 , myList)
print(list(oddNum)) #O/P :[1, 3, 5]

num = (1,2,3,4)
square = map(lambda x : x**2,num)
print(tuple(square)) #O/P : (1, 4, 9, 16)
 
