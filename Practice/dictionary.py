point = {"x": 1, "y": 2}
point = dict(x=1, y=2)
point["x"] = 10
point["z"] = 20

# access or search for a key
if "a" in point:
    print(point["a"])

print(point.get("a", 0))

# delete a key
del point["x"]
print(point)

# loop over dictionary
for key in point:
    print(key, point[key])

# iterate dictionary using items()
for key, value in point.items():
    print(key, value)

# dictionary comprehension
print(f"\n")
values = []
for x in range(5):
    values.append(x * 2)
    print(values)

# values = [x * 2 for x in range(5)]
print(f"\n")
print(values)

# comprehended version
values = [x * 2 for x in range(5)]
print(f"\n")
print(values)

# comprehended version with set, difference is the curly bracket
values = {x * 2 for x in range(5)}
print(f"\n")
print(values)

# dictionary comprehension
values = {x: x * 2 for x in range(5)}
print(f"\n")
print(values)
