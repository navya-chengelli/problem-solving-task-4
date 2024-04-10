

import math

class Circle:
    def __init__(self, radii_list):
        self.radii_list = radii_list

    def calculate_area(self):
        areas = []
        for radius in self.radii_list:
            area = math.pi * radius**2
            areas.append(area)
        return areas

    def calculate_circumference(self):
        circumferences = []
        for radius in self.radii_list:
            circumference = 2 * math.pi * radius
            circumferences.append(circumference)
        return circumferences

# Example usage:
radii = [10, 501, 22, 37, 100, 999, 87, 351]
circle = Circle(radii)

areas = circle.calculate_area()
circumferences = circle.calculate_circumference()

print("Areas:", areas)
print("Circumferences:", circumferences)
