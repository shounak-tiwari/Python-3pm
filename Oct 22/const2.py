class student:
    def __init__(self):
        self.name = input("Enter the name of student : ")
    def show(self):
        print("The name of student : ",self.name)
    def __del__(self):
        print("this is distructor of student class")
class management:
    def __init__(self):
        print("this is manabgement class")
    def __del__(self):
        print("this is distructor of management ")
obj1 = student()
obj1.show()
obj2 = student()
obj3 = management()
obj4 = management()