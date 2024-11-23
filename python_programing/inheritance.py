# class student:
#     def __init__(self,fname,lname):
#         self.firstname=fname
#         self.lastname=lname

#     def printname(self):
#         print(self.firstname,self.lastname)

# x=student('joe','luther')
# x.printname()

# class student1:
#     def __init__(self,fname,lname):
#         self.name=fname
#         self.age=lname
#     def printname(self):
#         print(self.name,self.age)

# y=student1('ashi',25)
# y.printname()

# class job:
#     def __init__(self,fname,lname):
#         self.job_name=fname
#         self.salary=lname
#     def printname(self):
#         print(self.job_name,self.salary)

# z=job('tailor',10000)
# z.printname() 

# class teacher:
#     def __init__(self,fname,lname):
#         self.name=fname
#         self.subject=lname
#     def printname(self):
#         print(self.name,self.subject)
# z=teacher('zera','maths')
# z.printname()

class train:
    def __init__(self,fname,lname):
        self.name_train=fname
        self.un_fee=lname
    def printname(self):
        print(self.name_train,self.un_fee)
z=train('memu_exp',50)
z.printname()