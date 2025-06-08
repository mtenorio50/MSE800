# SWAP VARIABLES long version

x = 10
y = 20
z = x
x = y
y = z
print("x:", x)
print("y:", y)

# simplified version

x, y = y, x
print("x:", x)
print("y:", y)
