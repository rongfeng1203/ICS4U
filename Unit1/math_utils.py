"""this module contains utility functions for basic mathematical operations."""
area_rectangle = lambda length, width: length * width
"""perimeter_rectangle = lambda length, width: 2 * (length + width)"""
area_triangle = lambda base, height: 0.5 * base * height
"""circumference_circle = lambda radius: 2 * 3.14159 * radius"""
area_circle = lambda radius: 3.14159 * radius ** 2
"""perimeter_circle = lambda radius: 2 * radius"""
perimeter_rectangle = lambda length, width: 2 * (length + width)
"""perimeter_triangle = lambda base, height: base + height + (base ** 2 + height ** 2) ** 0.5"""
circumference_circle = lambda radius: 2 * 3.14159 * radius
"""perimeter_triangle = lambda base, height: base + height + (base ** 2 + height ** 2) ** 0.5"""
if __name__ == "__main__":
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    print(f"Area of rectangle: {area_rectangle(length, width)}")
    print(f"Perimeter of rectangle: {perimeter_rectangle(length, width)}")

    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    print(f"Area of triangle: {area_triangle(base, height)}")

    radius = float(input("Enter the radius of the circle: "))
    print(f"Area of circle: {area_circle(radius)}")
    print(f"Circumference of circle: {circumference_circle(radius)}")