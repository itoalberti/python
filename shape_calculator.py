# Polygon Area Calculator
# https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/polygon-area-calculator

import array
class Rectangle:
    pic=[]
    def __init__(self, width, height):
        self.width=width
        self.height=height
    
    def __str__(self):
        return('Rectangle(width=%s , height=%s)' %(str(self.width), str(self.height)))

    def set_width(self, width):
        self.width=width
    
    def set_height(self, height):
        self.height=height

    def get_area(self):
        return(self.width*self.height)
    
    def get_perimeter(self):
        return(2*(self.width + self.height))
    
    def get_diagonal(self):
        return((self.width**2+self.height**2)**0.5)
    
    def get_picture(self):
        pic_array=[]
        pic=str()
        if self.width<=50 and self.height<=50:
            for i in range(0,self.height):
                pic_array.append('*'*self.width)
                pic=pic+pic_array[i]+'\n'
            return(pic)
        else:
            return('Too big for picture')

    def get_amount_inside(self, shape):
        return int(self.get_area()/shape.get_area())


class Square(Rectangle):
    def __init__(self, side):
        self.width=side
        self.height=side

    def __str__(self):
        return('Square(side=%s)' %(str(self.width)))

    def set_side(self, side):
        self.width=side
        self.height=side