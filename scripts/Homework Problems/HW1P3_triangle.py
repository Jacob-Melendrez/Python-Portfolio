def triangle_type(a, b, c):
    if a == b and b == c and c == a:
        return "Equilateral"
    elif a == b and b != c:
        return "Isosceles"
    elif b == c and c != a:
        return "Isosceles"
    elif c == a and a != b:
        return "Isosceles"
    elif a != b and b != c and c != a:
        return "Scalene"
"""
print(triangle_type(4, 5, 6))
print(triangle_type(5, 5, 5))
print(triangle_type(5, 5, 8))
print(triangle_type(8, 5, 8)
"""
