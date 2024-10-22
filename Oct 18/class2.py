class Dog_Record:
    def Get_data(self):
        self.name = input("Enter the name  : ")
        self.age = float(input("Enter the age  : "))
    def Show_data(self):
        print("Name of dog : ",self.name)
        print("Age of dog : ",self.age)
s1 = Dog_Record()
s1.Get_data()
s1.Show_data()
s2 = Dog_Record()
s2.Get_data()
s2.Show_data()
s3 = Dog_Record()
s3.Get_data()
s3.Show_data()
