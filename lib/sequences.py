#!/usr/bin/env python3

def print_fibonacci(length):
    if length <= 0:
        print("value shoud be greater that 0.")
        return
    

    a, b = 0, 1
    while a <= length:
        print(a, end=" ")
        a, b = b, a + b



try:
    length_value = int(input("Enter an integer: "))
    print("Fibonacci sequence up to", length_value, ":")
    print_fibonacci(length_value)
except ValueError:
    print("Invalid input. Please enter a valid integer")