""" Python Crash Course """

# Strings:
# Use an f-string to substitute values into strings
first_name, last_name = ["Lillie", "Sauer"]
full_name = f"{first_name} {last_name}"
print(full_name)

# Exceptions:
# Handle exceptions to clean up your code
try:
    print(0/0)
except ZeroDivisionError:
    print("Cannot divide by zero")

# Lists
# Concatenate lists using 'extend'
x = [1, 2, 3]
x.extend([4, 5, 6])         # x becomes [1, 2, 3, 4, 5, 6]

        # When taking values from a list for new variables:
_, y = [1, 2]       # y == 2, the first element is disregarded

# Counters
# A Counter turns a sequence of value into a 'defaultdict(int)'-like object
# that maps keys to counts. Has a 'most_common' method.
from collections import Counter
doc = ["cat", "dog", "rat", "cat", "cat", "rat", "bird"]
word_counts = Counter(doc)
for word, count in word_counts.most_common():
    print(word, count)

# Sets
# To create a new set, "set = {2, 3, 4}" or "set()"
# Sets are contained within curly braces, but {} means an empty dict
s = set()
s.add(1)        # s becomes {1}
s.add(2)        # s becomes {1, 2}
s.add(2)        # s is still {1, 2}

        # the "in" operation is a lot faster on sets than on lists
        # make a list into a set -- new_set = set(old_list)
        # Sets are also useful for finding distinct items in a collection
        # e.g. list = [1, 2, 3, 1, 2, 3]; num_items = len(list) == 6
        #       set = set(list);    num_items = len(set)        == 3

# Control Flow
# if-elif-else; if-then-else; while; for-in; continue-break; etc.
for x in range(10):
    if x == 3:
        continue
    if x == 5:
        break
    print(x)            # prints "0, 1, 2, 4"

# Truthiness
# Pythonic way to check for nonexistant value:
assert x is None
    # Can also use the "all()" and "any()" functions to get True or False

# List Comprehensions
# Use list comprehensions to turn a list into a new list by choosing only
# certain elements, transforming elements, or both:
evens = [x for x in range(5) if x % 2 == 0]         # [0, 2, 4]
squares = [x * x for x in range(5)]                 # [0, 1, 4, 9, 16]
even_squares = [x * x for x in evens]               # [0, 4, 16]
# Turn lists into dictionaries or sets:
squares_dict = {x: x*x for x in range(5)}           # {..., 2: 4, 3: 9,...}
squares_set = {x * x for x in [1, -1]}              # {1}

# Automated Testing
# We will focus on "assert" statements, which raise an AssertionError if 
# the specified condition is not Truthy
assert 1 + 1 == 2, "1 + 1 should equal 2 but didn't"
        # you can add optional messages to print if the assertion fails
# Assert is very useful to test that functions are working as expected:
def smallest_item(xs):
    return min(xs)

assert smallest_item([10, 20, 5, 45]) == 5
assert smallest_item([1, 0, -1, 2]) == -1

