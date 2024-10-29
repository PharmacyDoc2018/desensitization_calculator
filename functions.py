from cyclophosphamide import Cyclophosphamide

def to_measurable(vol):
    increment = 0
    if vol <= 3:
        increment = 0.05
    elif vol <= 10:
        increment = 0.1
    else:
        increment = 0.5
    return (vol//increment)*increment

