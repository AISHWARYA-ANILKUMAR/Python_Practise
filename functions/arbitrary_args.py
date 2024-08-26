def fun( *values ):
    print(values)
    print("First :" +values[0]  + "\n " + "Second :" +values[1])
fun("ONE", "TWO")


def sumFunction(*args):
    res=sum(args)
    print("The sum :"+ str(res))   
sumFunction(1,2,5,6,4)
    


def sample(*data):
    print("The data's are :")
    for item in data :
        print(f"- {item}")
        
sample("one","two","three")
sample(1,2,3,4,5)
sample("a","b","c","d","e","f")
     