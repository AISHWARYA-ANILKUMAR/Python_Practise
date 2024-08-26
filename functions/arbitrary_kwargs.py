def sample(**kwargs):
    print(kwargs)
    
sample(name="John", age=23,place="Kochi")
#O/p : {'name': 'John', 'age': 23, 'place': 'Kochi'}

def details(**kwargs):
    for key,value in kwargs.items(): #.items() method to get both keys and values from the dictionary.
        print(f"{key}: {value}")
        
details(name="Jerome",age=25,place="kozhikode",phone="8956471258",country="India")


# O/P:
# name: Jerome
# age: 25
# place: kozhikode
# phone: 8956471258
# country: India


def capitalize(**kwargs):
    # Create a new dictionary to store the capitalized values
    capitalized_kwargs = {}
    
    for key, value in kwargs.items():
        if isinstance(value, str):
            capitalized_kwargs[key] = value.capitalize() # if the value is string , capitalize it
        else:
            capitalized_kwargs[key] = value # else simply keep it like that
    
    print(capitalized_kwargs)

capitalize(name="aisHWArya", age=20, place="KoCHI")
capitalize(name="kRIshna", age=10,place="koZHIkoDE")

# O/P: {'name': 'Aishwarya', 'age': 20, 'place': 'Kochi'}
# {'name': 'Krishna', 'age': 10, 'place': 'Kozhikode'}