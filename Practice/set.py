numbers = [1, 1, 2, 3, 4]
first = set(numbers)
second = {1, 5}

print(first | second)  # union
print(first & second)  # intersection
print(first - second)  # difference
print(first ^ second)  # symmetric difference

if 1 in first:
    print("1 is in the first set")
