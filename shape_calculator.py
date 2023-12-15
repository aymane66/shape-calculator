class Rectangle:
    def __init__(self, width, height):
        # Initialize the Rectangle with width and height
        self.width = width
        self.height = height

    def set_width(self, width):
        # Set the width of the rectangle
        self.width = width

    def set_height(self, height):
        # Set the height of the rectangle
        self.height = height

    def get_area(self):
        # Calculate and return the area of the rectangle
        return self.width * self.height

    def get_perimeter(self):
        # Calculate and return the perimeter of the rectangle
        return (2 * self.width) + (2 * self.height)

    def get_diagonal(self):
        # Calculate and return the diagonal of the rectangle
        return ((self.width**2 + self.height**2)**.5)

    def get_picture(self):
        # Return a string representing a picture of the rectangle with '*' characters
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        else:
            return ((("*" * self.width) + "\n") * self.height)

    def get_amount_inside(self, shape):
        # Check if the shape has zero width or height
        if shape.width == 0 or shape.height == 0:
            return 0

        # Calculate and return the number of times the given shape can fit inside the rectangle
        width_fit = self.width // shape.width
        height_fit = self.height // shape.height
        return width_fit * height_fit

    def __str__(self):
        # Return a string representation of the Rectangle
        return (("Rectangle(width={0}, height={1})").format(
            self.width, self.height))


class Square(Rectangle):
    def __init__(self, side):
        # Initialize the Square with a side, using the Rectangle constructor
        super().__init__(side, side)

    def set_side(self, side):
        # Set the side of the square
        self.width = side
        self.height = side

    def set_width(self, side):
        # Set the width of the square
        self.width = side

    def set_height(self, side):
        # Set the height of the square
        self.height = side

    def __str__(self):
        # Return a string representation of the Square
        return f"Square(side={self.width})"