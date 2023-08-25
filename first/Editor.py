
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
class Editor:
    def __init__(self):
        
        self.rect = None
        self.circle = None


    def create_rectangle(self,width,height):
            self.rect=Rectangel(width,height)

    def create_circle(self,radius):
            self.circle=Circle(radius)

    def change_rectangle(self,factor):
        if self.rect == None:
            return
        
        width,height=self.rect.width +factor ,self.circle.radius +factor
        self.create_rectangle(width,height)

    def change_circle(self,factor):
        if self.circle == None:
            return
        
        self.create_circle(self.circle.radius + factor)
    def change(self,factor):
        self.change_circle(factor)
        self.change_rectangle(factor)

    def print(self):
            if self.rect !=None:
                print("Rectangke area",self.rect.get_area())
            if self.circle !=None:
                print("Circle area",self.circle.get_area())




editor=Editor()
editor.create_rectangle(3,5)
editor.print()
editor.create_circle(5)
editor.change(2)
editor.print()

