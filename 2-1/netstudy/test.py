import socket

class Furniture():

    def __init__(self,name,area):
        self.name = name
        self.area = area

    def __str__(self):
        
        return self.name


class House():

    def __init__(self,typename,area):

        self.typename = typename 
        self.area = area
        self.furnitures = []

    def add_furniture(self,furniture):

        self.furnitures.append(furniture.name)
        self.area -= furniture.area
        print("放入新家具【%s】，房子还剩余%.2f平米。" 
                %(furniture.name,self.area))

def main():
    print("Welcome my house")
    bed = Furniture("床",4)
    desk = Furniture("桌子",1.5)
    box = Furniture("箱子",0.5)

    myhouse = House("两房一厅",60.0)

    myhouse.add_furniture(bed)
    myhouse.add_furniture(desk)
    myhouse.add_furniture(box)

    print(myhouse.furnitures)

if __name__ == "__main__":
    main()

