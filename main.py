from shape_calculator import Rectangle, Square

def main():
    # Rectangle
    rect = Rectangle(10, 5)
    print("Rectangle:")
    print(f"Area: {rect.get_area()}")
    rect.set_height(3)
    print(f"Perimeter: {rect.get_perimeter()}")
    print(f"Description: {rect}")
    print("Picture:")
    print(rect.get_picture())

    # Square
    sq = Square(9)
    print("\nSquare:")
    print(f"Area: {sq.get_area()}")
    sq.set_side(4)
    print(f"Diagonal: {sq.get_diagonal()}")
    print(f"Description: {sq}")
    print("Picture:")
    print(sq.get_picture())

    # Test amount inside
    rect.set_height(8)
    rect.set_width(16)
    print(f"\nNumber of squares inside the rectangle: {rect.get_amount_inside(sq)}")

if __name__ == "__main__":
    main()
