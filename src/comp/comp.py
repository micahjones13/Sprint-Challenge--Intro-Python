# The following list comprehension exercises will make use of the
# defined Human class.
import math


class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"<Human: {self.name}, {self.age}>"


humans = [
    Human("Alice", 29),
    Human("Bob", 32),
    Human("Charlie", 37),
    Human("Daphne", 30),
    Human("Eve", 26),
    Human("Frank", 18),
    Human("Glenn", 42),
    Human("Harrison", 12),
    Human("Igon", 41),
    Human("David", 31),
]

# Write a list comprehension that creates a list of names of everyone
# whose name starts with 'D':
print("Starts with D:")
#   return the name that passed|for person in humans,|check if the first letter is D
a = [person.name for person in humans if person.name[0] == 'D']
print(a)

# Write a list comprehension that creates a list of names of everyone
# whose name ends in "e".
print("Ends with e:")
# return the names that pass|for person in humans|check if the last ltter is 'e'
b = [person.name for person in humans if person.name[-1] == 'e']
print(b)

# Write a list comprehension that creates a list of names of everyone
# whose name starts with any letter between 'C' and 'G' inclusive.
print("Starts between C and G, inclusive:")
# return the names taht pass|for person in humans| check if name starts with letters C-G
c = [person.name for person in humans if person.name[0]
     in ['C', 'D', 'E', 'F', 'G']]
print(c)

# Write a list comprehension that creates a list of all the ages plus 10.
print("Ages plus 10:")
# return age + 10|for person in humans
d = [person.age + 10 for person in humans]
print(d)

# Write a list comprehension that creates a list of strings which are the name
# joined to the age with a hyphen, for example "David-31", for all humans.
print("Name hyphen age:")
# return string name-age|for person in humans
e = [f'{person.name}-{person.age}' for person in humans]
print(e)

# Write a list comprehension that creates a list of tuples containing name and
# age, for example ("David", 31), for everyone between the ages of 27 and 32,
# inclusive.
print("Names and ages between 27 and 32:")
# return tuple of name and age|for person in humans|if age is between 27 & 32
f = [(person.name, person.age)
     for person in humans if person.age in [27, 28, 29, 30, 31, 32]]
print(f)

# Write a list comprehension that creates a list of new Humans like the old
# list, except with all the names uppercase and the ages with 5 added to them.
# The "humans" list should be unmodified.
print("All names uppercase:")
# return list of humans with uppercase and +5|for person in humans
# needed new human objs
g = [Human(person.name.upper(), person.age+5) for person in humans]
print(g)

# Write a list comprehension that contains the square root of all the ages.
print("Square root of ages:")
# return square root of ages|for person in humans
h = [math.sqrt(person.age) for person in humans]
print(h)
