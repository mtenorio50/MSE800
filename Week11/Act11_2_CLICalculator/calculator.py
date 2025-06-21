import math


def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def power(a, b):
    if a == 0 and b < 0:
        raise ValueError("0 cannot be raised to a negative power.")
    try:
        result = a ** b
    except OverflowError:
        raise OverflowError("Result too large.")
    except Exception as e:
        raise ValueError(f"Invalid input for power: {e}")
    return result


def root(a, n):
    if n == 0:
        raise ValueError("Zeroth root is undefined.")
    if a < 0 and n % 2 == 0:
        raise ValueError("Cannot take even root of negative number.")
    try:
        result = a ** (1/n)
    except Exception as e:
        raise ValueError(f"Invalid input for root: {e}")
    return result


def sine(x): return math.sin(x)
def cosine(x): return math.cos(x)
def tangent(x): return math.tan(x)
