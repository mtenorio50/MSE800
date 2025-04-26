def factorial(n):
    result = 1  # Initialize result to 1
    for i in range(1, n + 1):  # Loop from 1 to n (inclusive)
        result *= i  # Multiply result by i
    return result  # Return the final result


num = 5  # Get user input
print(f"Factorial of {num} is {factorial(num)}")
