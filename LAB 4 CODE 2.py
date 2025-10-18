import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    # Method to compute area of the circle
    def area(self):
        return math.pi * (self.radius ** 2)

    # Method to compute perimeter (circumference) of the circle
    def perimeter(self):
        return 2 * math.pi * self.radius


# Example usage
if __name__ == "__main__":
    # Create a Circle object
    c = Circle(5)  # You can change 5 to any radius value

    print(f"Radius: {c.radius}")
    print(f"Area of Circle: {c.area():.2f}")
    print(f"Perimeter of Circle: {c.perimeter():.2f}")
