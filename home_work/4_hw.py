class Box:
    def __init__(self, h, w):
        self.h = h
        self.w = w
    def plo (self):
        print (self.h * self.w)
    def per (self):
        print ((2*self.h)+(2*self.w))


cube1 = Box(2, 4)
cube2 = Box(3, 4)
cube3 = Box(4, 4)
cube1.plo()
cube1.per()
cube2.plo()
cube2.per()
cube3.plo()
cube3.per()
