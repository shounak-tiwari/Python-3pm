class student:
    def get_data(self):
        name = input("Enter the name of student : ")
        age  = float(input("Enter the age of student  : "))
        self.N = name
        self.A = age
    def show_data(self):
        print("Name of student : ",self.N)
        print("Age of student : ",self.A)


obj = student()

obj.get_data()
obj.show_data()
