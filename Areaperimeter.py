class rectangle:
    def getData(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        a=self.length*self.breadth
        print("area of rectangle with length",self.length,"and breadth",self.breadth,"is",a)
    def perimeter(self):
        p=2*(self.length+self.breadth)
        print("perimeter of rectangle with length",self.length,"and breadth",self.breadth,"is",p)
ch=0
l=int(input("Enter the length of a rectangle:"))
b=int(input("Enter breadth of a rectangle:"))
obj=rectangle()
obj.getData(l,b)
while ch!=3:
        print("1.area")
        print("2.perimeter")
        print("3.exit")
        ch=int(input("Enter your choice:"))
        if ch==1:obj.area()
        if ch==1:obj.perimeter()
else:print("End of the program:")
