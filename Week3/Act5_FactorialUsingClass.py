# Using class write a code for factorial
class factorial:  # Define a class named factorial
    def number(n):  # Define a static method named number calculate factorial
        result = 1  # Initialize result to 1
        for i in range(1, n + 1):  # Loop from 1 to n
            result *= i  # Multiply result by i
        return result  # Return the final result


num = int(input("Enter a number: "))  # Get user input
# Call the factorial class method to calculate factorial
ans = factorial.number(num)
print(f"Factorial of {num} is {ans}")
