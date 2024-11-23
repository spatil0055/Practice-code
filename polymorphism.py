class shape:
    def Area(self):
        pass
class Rectangle(shape):
    def __init__(self, l, b):
        self.l = l
        self.b = b
    def Area(self):
        return self.l*self.b
class Square(shape):
    def __init__(self, s):
        self.s = s
    def Area(self):
        return self.s**2
s = Square(3)
r = Rectangle(3,4)
print(s.Area())
print(r.Area()) 