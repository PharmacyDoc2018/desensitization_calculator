import math

from cyclophosphamide import Cyclophosphamide

def true_divide(x, y):
    i = 0
    while x%1 != 0:
        x *= 10
        y *= 10
        i += 1
    while y%1 != 0:
        x *= 10
        y *= 10
        i += 1
    result = (x / y) / (10**i)
    return result

def true_subtraction(x, y):
    i = 0
    while x%1 != 0:
        x *= 10
        y *= 10
        i += 1
    while y%1 != 0:
        x *= 10
        y *= 10
        i += 1
    result = (x - y) / (10**i)
    return result

def true_addition(x, y):
    i = 0
    while x%1 != 0:
        x *= 10
        y *= 10
        i += 1
    while y%1 != 0:
        x *= 10
        y *= 10
        i += 1
    result = (x + y) / (10**i)
    return result

def true_mod(x, y):
    i = 0
    while x%1 != 0:
        x *= 10
        y *= 10
        i += 1
    while y%1 != 0:
        x *= 10
        y *= 10
        i += 1
    result = (x % y) 
    return result

def get_increment(vol):
    increment = 0
    if vol <= 3:
        increment = 0.05
    elif vol <= 10:
        increment = 0.1
    else:
        increment = 0.5
    return increment

def is_increment(vol):
    increment = get_increment(vol)
    if true_mod(vol, increment) == 0:
        return True
    return False

def to_measurable(vol):
    increment = get_increment(vol)
    if true_mod(vol, increment) == 0:
        result = vol
    else:
        result = (vol//increment)*increment
    return result

def next_lower_measurable(vol):
    if not is_increment(vol):
        raise Exception("Error: volume must be a measurable increment")
    increment = get_increment(vol)
    result = true_subtraction(vol, increment)
    
    if not is_increment(result):
        increment = get_increment(result)
        result = true_subtraction(vol, increment)
    
    return result

def next_higher_measurable(vol):
    if not is_increment(vol):
        raise Exception("Error: volume must be a measurable increment")
    increment = get_increment(vol)
    result = true_addition(vol, increment)
    
    if not is_increment(result):
        increment = get_increment(result)
        result = true_addition(vol, increment)
    
    return result
    