class cycle:
    def __init__(self):
        self.name =  input("Enter the Model Name : ")
        self.maxspeed = float(input("Enter the Maximum Speed : "))
    def show(self):
        print("The name : ",self.name)
        print("Maximum speed : ",self.maxspeed)
    
class Motorcycle(cycle):
    def __init__(self):
        super().__init__()
        self.nocy = int(input("Enter the number of cylinders in motor cycle : "))
        self.noseat = int(input("Enter the number of seat  : "))
    def show(self):
        cycle.show(self)
        print("No of cylinders in motor cycle : ",self.nocy)
        print("No of seat in motor cycle : ",self.noseat)
    
Obj1 = Motorcycle()
Obj1.show()