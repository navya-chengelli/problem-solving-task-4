class Circle:
    def __init__(self, radius):
        self.radius = radius

    @classmethod
    def calculate_area(cls, radius):
        
        #Class method to calculate the area of a circle.

       # Args:
        #    radius (float): The radius of the circle.

       # Returns:
       #     float: The area of the circle.
        
        pi = 3.141  # Value of pi
        return pi * (radius ** 2)

    @classmethod
    def calculate_parameter(cls, radius):
        
       # Class method to calculate the parameter (circumference) of a circle.

        #Args:
        #    radius (float): The radius of the circle.

       # Returns:
        #    float: The parameter (circumference) of the circle.
        
        pi = 3.141  # Value of pi
        return 2 * pi * radius

# Example usage
radius = 5
print("Area of the circle with radius", radius, "is:", Circle.calculate_area(radius))
print("Parameter of the circle with radius", radius, "is:", Circle.calculate_parameter(radius))
