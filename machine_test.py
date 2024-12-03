class plus_one:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
    def printname(self):
        print(self.firstname,self.lastname)
class student(plus_one):
    pass
x=student('vasukkuttan','bio_science')
x.printname()


class company:
    def __init__(self,sala,exp):
        self.salary=sala
        self.experience=exp
    def printname(self):
        print(self.salary,self.experience)
class employee(company):
    pass
y=employee(25000,"2 years")
y.printname()