class Circle:
    def __init__(self, radius):
        self.__pi = 3.141  # Private member variable for pi
        self.radius = radius

    def calculate_area(self):
        # Calculate the area of the circle using the private member variable pi
        area = self.__pi * (self.radius ** 2)
        return area


radius = 5
circle = Circle(radius)
print("Area of the circle with radius", radius, "is:", circle.calculate_area())
