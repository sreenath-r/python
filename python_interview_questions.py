#Basic Python Questions:

#1. what are Variables and how to declare them in Python?
'''Variables are used to store data values. In Python, you can declare a variable by simply assigning 
a value to it using the equals sign (=).'''
#Example:
x = 5
y = "Hello"

#2.What are python's built-in data types?
'''Python has several built-in data types, including:
- Numeric (int, float, complex)
- Sequence (list, tuple, range)
- Text (str)
- Mapping (dict)
- Set (set, frozenset)
- Boolean (bool)
- Binary (bytes, bytearray, memoryview)'''

#3.how do you write a function in python?
'''You can define a function in Python using the def keyword, followed by the function name and parentheses.'''
#Example:
def greet(name):
    return "Hello, " + name + "!"

'''Running greet(name) returns the greeting string "Hello, <name>!" 
(it does not print anything by itself).'''

#4.what is a list and how it is different from tuple?
'''A list is a mutable, ordered collection of items, 
while a tuple is an immutable, ordered collection of items.'''
#Example:
my_list = [1, 2, 3] # list
my_tuple = (1, 2, 3) # tuple        

#5.How do you handle exceptions in Python?
'''You can handle exceptions in Python using try and except blocks.'''              
#Example:
try:
    x = 1 / 0
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")       


#6.what is a dictionary and how do you use it?
'''A dictionary is a mutable, unordered collection of key-value pairs.'''
#you can use it store data values like this
#Example:
my_dict = {
    "name": "Alice",
    "age": 30, 
    "city": "New York"
    }          

#you can access values using their keys:
# Example:
name = my_dict["name"]  # "Alice"        
age = my_dict["age"]    # 30
city = my_dict["city"]  # "New York"

#7.how do you import and use libraries in Python?
'''You can import libraries in Python using the import statement.'''    
#Example:
import math 
result = math.sqrt(16)  # 4.0
print(result)           # prints: 4.0
#You can also import specific functions or classes from a library:
from math import sqrt
result = sqrt(25)      # 5.0
print(result)          # prints: 5.0

#8.what is a loop and how do you write for/while loops in Python?
'''A loop is a control structure that allows you to repeat a block of code multiple times.'''
#You can write a for loop using the for keyword, and a while loop using the while keyword.
#Example of a for loop:
for i in range(5):
    print(i)

#Example of a while loop:
count = 0
while count < 5:
    print(count)
    count += 1

#9.How do you read and write files in Python?
'''You can read and write files in Python using the built-in open() function.'''    
#Example of writing to a file:
with open("example.txt", "w") as file:
    file.write("Hello, World!")

#Example of reading from a file:
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
#prints: Hello, World!

#10. what is the difference between python 2 and python 3?
'''Python 3 is the latest version of Python and includes several improvements and new features over Python 2.
Some key differences include:       
- Print statement: In Python 2, print is a statement, while in Python 3, print() is a function.
- Integer division: In Python 2, dividing two integers performs floor division, while in Python
    3, it performs true division.
- Unicode: In Python 3, strings are Unicode by default, while in Python 2, they are ASCII by default.
- Libraries: Some libraries are only available for Python 3, while others are only available for
    Python 2.'''