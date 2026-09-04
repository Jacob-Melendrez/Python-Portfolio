def triangle_type(a, b, c):
    if a == b and b == c:
        print("Equilateral")
    elif a != b and b == c:
        print("Isosceles")
    elif b != c and c == a:
        print("Isosceles")
    elif c != a and a == c: 
        print("Isosceles")
    elif a != b and b != c and c != a:
        print("Scalene")
    
triangle_type(4, 5, 6)
