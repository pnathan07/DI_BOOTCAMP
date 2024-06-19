import math

class Circle:
    def __init__(self, radius=None, diameter=None):
        if radius:
            self.radius = radius
        elif diameter:
            self.radius = diameter / 2
        else:
            raise ValueError("Must provide either radius or diameter")

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2

    def area(self):
        return math.pi * self.radius ** 2

    def __str__(self):
        return f"Circle with radius: {self.radius} and diameter: {self.diameter}"

    def __repr__(self):
        return f"Circle(radius={self.radius})"

    def __add__(self, other):
        if isinstance(other, Circle):
            return Circle(radius=self.radius + other.radius)
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Circle):
            return self.radius < other.radius
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Circle):
            return self.radius == other.radius
        return NotImplemented

# Create Circle instances
circle1 = Circle(radius=5)
circle2 = Circle(diameter=10)
circle3 = Circle(radius=3)

# Compute area
print(f"Area of circle1: {circle1.area()}")  # Area of circle1: 78.53981633974483

# Print attributes
print(circle1)  # Circle with radius: 5.0 and diameter: 10.0

# Add two circles
circle4 = circle1 + circle3
print(circle4)  # Circle with radius: 8.0 and diameter: 16.0

# Compare two circles
print(circle1 < circle2)  # False
print(circle1 == circle2)  # True

# Sort circles in a list
circles = [circle1, circle2, circle3, circle4]
sorted_circles = sorted(circles)
print(sorted_circles)
# Output: [Circle(radius=3.0), Circle(radius=5.0), Circle(radius=5.0), Circle(radius=8.0)]
