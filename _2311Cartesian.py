# Q)plot the points on a cartesian plane which has 2 coordinates
# x and y. do the following

# 1.define a class Point. Its instance should have 2 attributes x and y
# define x and y default value must be zero

# 2.define an  method reset().
# when called it will set x,y values to zero(ie it will set the points to origin(0,0))
 	
# 3. define an  method move().
# this should change the values of x and y.

# 4.Use this move method to update reset() method.

# 5.define 2  methods xmove and ymove.
# this should move the values of x and y seperately.



class Point:
    def __init__(self):
        self.x = 0
        self.y = 0

    def reset(self):
        self.x = 0
        self.y = 0
        print("Values of x and y reseted to zero")
    def move(self,*args):
        # print(args)
        if args[0] == "reset":
            self.reset()
        else:
            self.x += args[0]
            self.y += args[1]
            print(self.x,self.y)
    def yMove(self,y):
        self.y += y
        print(self.x,self.y)
    def xMove(self,x):
        self.x += x
        print(self.x,self.y)
    def display(self):
        print(f"Value of X : {self.x}\nValue of Y : {self.y}")
point = Point()

while True:
    print("Update the Cartesian Point")
    choice = input("Enter your choice\n1.Move both x and y\n2.Move X only\n3.Move Y only\n4.Reset\n5.Display\n6.Exit\n")
    if choice == "1":
        x = int(input("Enter Value for X: "))
        y = int(input("Enter Value for Y: "))
        point.move(x,y)
    elif choice == "2":
        x = int(input("Enter Value for X: "))
        point.xMove(x)
    elif choice == "3":
        y = int(input("Enter Value for y: "))
        point.yMove(y)
    elif choice == "4":
        point.move("reset")
    elif choice == "5":
        point.display()
    elif choice == "6":
        print("Existed")
    else:
        print("Wrong choice !!")
        continue
