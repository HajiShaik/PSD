import math

def sin(x):
    
    if not isinstance(x, (int, float)):
        raise TypeError("Input must be a number")
    return math.sin(math.radians(x))

def cos(x):
    
    if not isinstance(x, (int, float)):
        raise TypeError("Input must be a number")
    return math.cos(math.radians(x))

def tan(x):
   
    if not isinstance(x, (int, float)):
        raise TypeError("Input must be a number")
    if x % 180 == 90:
        raise ValueError("Tangent is undefined for this angle")
    return math.tan(math.radians(x))

def sqrt(x):
  
    if not isinstance(x, (int, float)):
        raise TypeError("Input must be a number")
    if x < 0:
        raise ValueError("Cannot compute square root of a negative number")
    return math.sqrt(x)

def log(x):
    
    if not isinstance(x, (int, float)):
        raise TypeError("Input must be a number")
    if x <= 0:
        raise ValueError("Logarithm undefined for non-positive values")
    return math.log10(x)

def exp(x):
    
    if not isinstance(x, (int, float)):
        raise TypeError("Input must be a number")
    return math.exp(x)
