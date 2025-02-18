import math

def degree_to_radian(degree):
    return degree * (math.pi / 180)

degree = 15
radian = degree_to_radian(degree)
print(f"Input degree: {degree}")
print(f"Output radian: {radian:.6f}\n")

def trapezoid_area(height, base1, base2):
    return (base1 + base2) * height / 2

height = 5
base1 = 5
base2 = 6
area_trapezoid = trapezoid_area(height, base1, base2)
print(f"Trapezoid Area: {area_trapezoid}\n")

def regular_polygon_area(sides, length):
    return (sides * length**2) / (4 * math.tan(math.pi / sides))

sides = 4
length = 25
area_polygon = regular_polygon_area(sides, length)
print(f"The area of the polygon is: {area_polygon}\n")

def parallelogram_area(base, height):
    return base * height

base = 5
height = 6
area_parallelogram = parallelogram_area(base, height)
print(f"Parallelogram Area: {area_parallelogram}\n")
