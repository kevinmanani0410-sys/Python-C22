class Rectangle:
    def __init__(self, rect_length, rect_width):
        self.rect_length = rect_length
        self.rect_width = rect_width

    def area(self):
        return self.rect_length * self.rect_width

rect_obj = Rectangle(10, 5)
print("Area:", rect_obj.area())
