class Degree:
    def getDegree(self):
        print("I got a degree")

class Undergraduate(Degree):
    def getDegree(self):
        print("I am an Undergraduate")

class Postgraduate(Degree):
    def getDegree(self):
        print("I am a Postgraduate")

# Creating objects
d = Degree()
d.getDegree()

ug = Undergraduate()
ug.getDegree()

pg = Postgraduate()
pg.getDegree()
