
class Student :
    name = ""
    roll = 0

    def show_details(self):
        print("Name: ",self.name)
        print("Roll: ",self.roll)

class Result(Student):
    m1 = 0
    m2 = 0

    def show_result(self):
        print("Subject 1 Marks: ",self.m1)
        print("Subject 1 Marks: ",self.m2)
        print("Subject 1 Marks: ",((self.m1+self.m2)/2))

s = Result()
s.name = "Prachiti"
s.roll = 185
s.show_details()
s.m1 = 40
s.m2 = 80
s.show_result()
