class Rectangle:
    def __init__(self,width,height):
        self.height=height
        self.width=width
    def set_height(self,height):
        self.height=height
    def set_width(self, width):
        self.width=width
    def get_area(self):
        return self.width*self.height
    def get_perimeter(self):
        return 2 * self.width + 2 * self.height
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5
    def get_picture(self):
        if self.width>50 or self.height>50:
            return "Too big for picture."
        else:
            figura = ""
            for i in range(0,self.height):
                for j in range(0,self.width):
                    figura = figura + "*"
                figura=figura+"\n"
        return figura
    def get_amount_inside(self,shape):
        cabehorizontal=self.width//shape.width
        cabevertical=self.height//shape.height
        return cabehorizontal*cabevertical
    def __str__(self):
        return "Rectangle(width="+str(self.width)+", height="+str(self.height)+")"
class Square (Rectangle):
    def __init__(self,length):
        self.height=length
        self.width=length
    def set_height(self,length):
        self.height = length
        self.width = length
    def set_width(self, length):
        self.height = length
        self.width = length
    def set_side(self,length):
        self.height = length
        self.width = length
    def __str__(self):
        return "Square(side="+str(self.width)+")"