# Magic methods in python

"""There are two similar special methods that describe the object using a string representation. 
These methods are .__repr__() and .__str__(). 
The .__repr__() method returns a detailed description for a programmer who needs to maintain and debug the code. 
The .__str__() method returns a simpler description with information for the user of the program.
reference : https://realpython.com/python-repr-vs-str/d
"""
class person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
      return f"{self.name}({self.age})"

    def __repr__(self):
        return f"person('{self.name}',{self.age})"

    def __call__(self):
        print("Hey I am good")


p = person("Harry", 30)
print(p)

print(p.__str__)


