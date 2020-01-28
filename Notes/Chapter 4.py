"""Linear Algebra:
   the branch of math that deals with vector spaces
"""
#
# Vectors - objects that can be added together to form new vectors,
#           and that can be multiplied by scalars; points in some
#           finite-dimensional space
from typing import List

Vector = List[float]

height_weight_age = [70,    # inches
                     170,   # pounds
                     40]    # years

grades = [95,   # exam 1
          80,   # exam 2
          75,   # exam 3
          62]   # exam 4

# Python lists *aren't* vectors, so we need to build our own tools
# Zip the vectors together and use list comprehension to perform
# arithmetic operations on them:

def add(v: Vector, w: Vector) -> Vector:
    """Adds corresponding elements"""
    
    assert len(v) == len(w), "vectors must be the same length"
    
    return [v_i + w_i for v_i, w_i in zip(v, w)]


assert add([1, 2, 3], [4, 5, 6]) == [5, 7, 9]

def subtract(v: Vector, w: Vector) -> Vector:
    """Subtracts corresponding elements"""
    
    assert len(v) == len(w), "vectors must be the same length"
    
    return [v_i - w_i for v_i, w_i in zip(v, w)]


assert subtract([5, 7, 9], [4, 5, 6]) == [1, 2, 3]

