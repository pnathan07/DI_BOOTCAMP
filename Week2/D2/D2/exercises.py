class Circle:
    color = "red"

class NewCircle(Circle):
    color = "blue"

nc = NewCircle
print(nc.color)


class Door:
    def __init__(self, is_opened=True) -> None:
        self.is_opened = is_opened

    def open_door(self):
        self.is_opened = True
        return self.is_opened

    def close_door(self):
        self.is_opened = False
        print('the door is now closed')

class Blockeddoor(Door):
    
    def open_door(self):
        raise Exception('a blocked door can\'t be open')
    
    def close_door(self):
        raise Exception('a blocked door can\'t be closed')

# door1 = Door()
# door1.close_door()
# print(door1.is_opened)

# door2 = Blockeddoor()
# door2.close_door()


class A():

    def dothis(self):
        print("doing this in A")


class B(A):
    pass


class C():
    def dothis(self):
        print("doing this in C")


class D(B, C):
    pass

d_instance = D()
d_instance.dothis() 





