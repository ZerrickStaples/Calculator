from helpers import *

print("Select an option: ")
print("1.) Addition: ")
print("2.) Subtraction: ")
print("3.) Multiplication: ")
print("4.) Division: ")
choice = input("What do you want to do?: ")

if choice == '1':
    input_string = input("Enter the numbers you want to add separated by a space: ")
    numbers = input_string.split()
    numbers = [int(num) for num in numbers]
    print(add_numbers(numbers))

if choice == '2':
    input_string = input("Enter the numbers you want to subtract: ")
    numbers = input_string.split()
    numbers = [int(num) for num in numbers]
    print(subtract_numbers(numbers))

if choice == '3':
    input_string = input("Enter the numbers you want to multiply: ")
    numbers = input_string.split()
    numbers = [int(num) for num in numbers]
    print(multiply_numbers(numbers))

if choice == '4':
    input_string = input("Enter the numbers you want to divide: ")
    numbers = input_string.split()
    numbers = [int(num) for num in numbers]
    print(divide_numbers(numbers))
