# Using class write a code for factorial
class factorial:  # Define a class named factorial
    def number(self, n):  # Method to calculate factorial
        result = 1  # Initialize result to 1
        for i in range(1, n + 1):  # Loop from 1 to n
            result *= i  # Multiply result by i
        return result  # Return the final result

    def prime(p):
        if num > 1:
            for i in range(2, p):  # Check for prime numbers
                if (num % i) == 0:  # If num is divisible by i, it is not prime
                    print(p, "is not a prime number")
                    break
            else:
                print(p, "is a prime number")
        else:
            print(p, "is not a prime number")


num = int(input("Enter a number: "))  # Get user input
# Call the prime method to check if the number is prime
print(factorial.prime(num))
obj = factorial()  # Create an instance of the factorial class
print(f"Factorial of {num} is {obj.number(num)}")
