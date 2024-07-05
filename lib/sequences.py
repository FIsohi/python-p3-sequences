#!/usr/bin/env python3

def print_fibonacci(length):
    # Handle the cases where length is less than or equal to 0
    if length <= 0:
        print([])
        return
    
    # Initialize the Fibonacci sequence with the first two numbers
    fibonacci_sequence = [0, 1]

    # Generate the Fibonacci sequence up to the specified length
    while len(fibonacci_sequence) < length:
        next_value = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_value)
    
    # Print the Fibonacci sequence up to the specified length
    print(fibonacci_sequence[:length])

