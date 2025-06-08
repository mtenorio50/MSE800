try:
    age = int(input("Enter your age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("Invalid input. Please enter a valid age.")
else:
    print("No exception were thrown")
