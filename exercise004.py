import math

radius = float(
    input("Introduce the radius of the circle you want to calculate the area")
)

if radius < 0:
    print("Error, you haven't introduce a correct number")
else:
    area = math.pi * radius**2
    print(f"The area of the circle with radius {radius} is equal to {area}!")