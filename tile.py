from graphics import *
class Tile(object):
    def __init__(self,centerpoint,size,value="",color="white",textcolor="black"):
        """constructor, create a tile object"""
        self.centerpoint = centerpoint
        self.size = size
        self.value = value
        self.color = color
        self.textcolor = textcolor
        p1 = Point(self.centerpoint.getX()-self.size/2,self.centerpoint.getY()-self.size/2)
        p2 = Point(self.centerpoint.getX()+self.size/2,self.centerpoint.getY()+self.size/2)
        self.rect = Rectangle(p1,p2)
        self.rect.setFill(self.color)
        self.text = Text(self.centerpoint,self.value)
        self.text.setTextColor(self.textcolor)
        self.text.setSize(28)

    def draw(self,win):
        """draw the tile"""
        self.rect.draw(win)
        self.text.draw(win)

    def move(self,dx,dy):
        """moves both the rectangle and text object by (dx,dy)"""
        self.rect.move(dx,dy)
        self.text.move(dx,dy)

    def setColor(self,ncolor):
        """set new color to the rectangle object"""
        self.rect.setFill(ncolor)

    def getValue(self):
        """return the value stored in the object"""
        return self.value

    def setValue(self,nvalue):
        """change the value stored in the object and the text display"""
        self.value = nvalue
        self.text.setText(self.value)
        self.text.setTextColor(self.textcolor)
        self.text.setSize(36)

    def __lt__(self,other):
        """return whether the value of tile1 is less than tile2"""
        if int(self.getValue()) < int(other.getValue()):
            return True
        else:
            return False

    def __gt__(self,other):
        """return whether the value of tile1 is greater than tile2"""
        if int(self.getValue()) > int(other.getValue()):
            return True
        else:
            return False

    def __eq__(self,other):
        """return whether the value of tile1 is equal to tile2"""
        if int(self.getValue()) == int(other.getValue()):
            return True
        else:
            return False

def main():
    gw = GraphWin("tiles",500,150)
    cp1 = Point(25,75)
    cp2 = Point(75,75)
    t1 = Tile(cp1, 50, "A")
    t2 = Tile(cp2, 50, "B")
    t2.move(10,10)
    t1.setColor("blue")
    v = t1.getValue()
    print(v)
    t2.setValue("6")
    t1.draw(gw)
    t2.draw(gw)
    gw.getMouse()
    gw.close()

if __name__ == "__main__":
    main()
