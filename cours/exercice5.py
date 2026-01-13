import math
class point:
    def __init__(self,x:None,y:None):
        self.__x=x
        self.__y=y
    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self,new):
        self.__x=new
    @property
    def y(self):
        return self.__y
    @y.setter
    def y(self,new):
        self.__y=new
    
    def Distance(self):
        return math.sqrt((self.__x**2)+(self.__y**2) )
    def __str__(self):
        return f"{self.__x}\t{self.__y}\t{self.Distance()}"
if __name__=='__main__':        
    a=point(12,10)
    print(a)
    b=point(4,3)
    print(b)
    a=b
    print(a)