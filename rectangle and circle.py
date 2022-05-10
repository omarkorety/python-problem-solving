class Rectangel:
    def __init__(self,width,height):
        self.width=width
        self.height=height

    def get_area(self):
        area=self.width *self.height
        return area

class Circle:
    def __init__(self,radius) :
        self.radius=radius
    def get_area(self):
        area=(self.radius**2)*3.14
        return area

        
r=Rectangel(2,5)
print(r.get_area())

c=Circle(5)
print(c.get_area())
