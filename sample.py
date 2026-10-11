
import requests

# Download a web page
response = requests.get("https://api.github.com")
print(response.status_code) 
# Should print 200

name = "chaman"

"""
 these are the multiline comments
""" 
power = 10**2
print(power)

string = "chaman tej"

long_string = """
my name is Chukka Chaman Tej
s/o Chukka Appala Naidu
"""
print(long_string)

first_name = "chaman"
last_name = "tej"

full_name = first_name + last_name
print(full_name)

long_dash = "_ " * 20
print(long_dash)

len(long_dash) #builtin functions


age=21
eligibile = age > 18
print(eligibile)

age=23
has_license = False
drunk = True

is_elgible = age>21 and has_license and not drunk


name = "chaman"
string = f"hi my name is {name}"
print(string)


message = "I love Python programming with Python"

print(message.tolower())

print("Python" in message)        # True
print(message.startswith("I"))   # True
print(message.endswith("Python")) # True

# Find position
print(message.find("Python"))     # 7 (first occurrence)
print(message.count("Python"))    # 2 (number of times)

# Replace
new_message = message.replace("Python", "JavaScript")
print(new_message)  # "I love JavaScript programming with JavaScript"
# or and not

name= "chaman tej"

for ch in name:
    print(ch)

for ch in name:
    print(ch,end="-")

for i in range(3,7,2):
    print(i,end=" ")


colors = ["red", "blue", "green"]
for color in colors:
    print(f"I like {color}")


numbers=[1,2,4,4,5,6]
print(numbers.index(4))#first occurence

numbers.sort()
numbers.reverse()

newlist = numbers.copy()
#if copy is not there then same list will be referenced and modified
# mainly only applicable for the lists,sets,dictionaries but not for normal strings,int,bool

person = {
    "name":"chaman Tej",
    "age":30,
    "city":"vizag"
}

print(person["name"])
print(person.get("job"))#default is none
print(person.get("job","unknown"))

person = {"name": "Alice", "age": 30, "city": "New York"}

# Get all keys, values, or items
print(person.keys())    # dict_keys(['name', 'age', 'city'])
print(person.values())  # dict_values(['Alice', 30, 'New York'])
print(person.items())   # dict_items([('name', 'Alice'), ...])

# Check if key exists
if "name" in person:
    print("Name found!")

# Update multiple values
person.update({"age": 31, "job": "Engineer"})
# by using update we can modify values and also add new keys, all this with keeping the old keys 


#list cant be used as keys string and tuples are ok 

#tuples are immutable
points = (3,4)
temp=list(points)
temp[0]=5
points=tuple(temp)


empty=set()