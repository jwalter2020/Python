class Rectangle:
        
               
        def __init__(self,length,width):
                self.length=length
                self.width=width
             
        def getLength(self):
                return self.length
        
        def setLength(self,length):
                self.length=length
                
        def getWidth(self):
                return self.width
        
        def setWidth(self,width):
                self.width=width
                
        def getArea(self):
                return self.length*self.width
                
class Rug(Rectangle):
        def __init__(self,length,width, price=250.80):
                Rectangle.__init__(self,length,width)
                self.price=price
                
        def getPrice(self):
                return self.price
        def __str__(self):
                return stringForObject

class Carpet(Rectangle):
        def __init__(self,length,width,price=2.15):
                Rectangle.__init__(self,length,width)
                self.ppsf=ppsf
                
        def getPrice(self):
                return self.price * self.getArea
        
        def __str__(self):
                return stringForObject

#def main():
#    if __name__ == "__main__":
#        length=float(input("Enter Length : "))
#        width=float(input("Enter Width : "))   
#        r1=Rectangle(length,width)
#        print('Length : ',r1.getLength())
#        print('Width : ',r1.getWidth())
#        print('Area : ',r1.getArea())


def main():
    if __name__ == "__main__":
        length=float(input("Enter Length : "))
        width=float(input("Enter Width : "))   
        r1=Rectangle(length,width)
        print('Length : ',r1.getLength())
        print('Width : ',r1.getWidth())
        print('Area : ',r1.getArea())

        rugs = Rug()
        for i in range (2):
                rug = Rug()
                rug.addRug(rug)
        def __iter__(self):
                self.__index = -1
                return self
        
        def __next__(self):
                if self__index ==len(self.__list)-1:
                        raise StopIteration()
                self.__index += 1
                rug = self.__list[self.__index]
                return rug
        for rug in Rug:
                print(rug, end= ' ')
main() #calling the main function
