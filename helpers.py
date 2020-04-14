def add_numbers(numbers):
    return sum(numbers)

def subtract_numbers(numbers):
    result = 0 - sum(numbers)
    return result
    
def multiply_numbers(numbers):
    result = 1
    for num in numbers:
        result = result * num
    return result

def divide_numbers(numbers):
    result = numbers[0]
    for num in numbers[1: len(numbers)]:
        result = result / num
    return int(result)