# unpacking operator "*"
numbers = [1, 2, 3, 4, 5]
print(*numbers)

# creating list without using unpacking operator
values = list(range(5))
print(values)

# creating list using unpacking operator
values = [*range(5)]
print(values)

# another sample
first = [1, 2, 3]
second = [4, 5, 6]
values = [*first, "a", *second, *"Hello"]
print(values)

# unpacking operator with dictionary
first = {"x": 1}
second = {"x": 10, "y": 3}
combined = {**first, **second, "z": 5}
print(combined)
