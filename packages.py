import math
print(math.sqrt(16))

#import only specific function
from math import sqrt,pi 
a=sqrt(16)
print(a)

import random 
number = random.randint(1,10)#here 1 and 10 included
print(number)

# Import entire module
import random

# Use module functions
number = random.randint(1, 10)
choice = random.choice(["apple", "banana", "orange"])

import json
data = {"name": "Alice", "age": 30}
json_string = json.dumps(data)
print(json_string)


