class Engineering:
    def Curriculum(self):
        print("B.Tech AI&DS")
        print("B.Tech CS")
        print("B.Tech Electrical Engg")
        print("B.Tech Mechatronics")

class Business:
    def Departments(self):
        print("BBA")
        print("MBA")
        print("CBA")

class Faculties:
    def Names(self):
        print("Ajit Sir")
        print("Uttam Sir")
        print("Khushbu Mam")

class Students(Engineering, Business, Faculties):
    def Edu(self):
        print("Hii I'm a Student")

Stu = Students()
Stu.Edu()
Stu.Names()
Stu.Departments()
Stu.Curriculum()