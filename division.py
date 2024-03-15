#module for division

def div(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    
    return x / y
