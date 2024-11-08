def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def average(values):
    """Calculates the average of a list of values"""
    total_sum = 0
    for value in values:
        total_sum+= value
        
    return total_sum/len(values)

def convert_temperature(celsius):
    """Convert Celsius to Fahrenheit"""
    return (celsius * 9/5) + 32
    