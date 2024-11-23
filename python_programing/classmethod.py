class Employee:
    def __init__(self,name,position):
        self.name=name
        self.position=position

    @classmethod
    def create_manager(cls,name):
        return cls(name,"manager")

    @classmethod
    def create_engineer(cls,name):
        return cls(name,"engineer")

manager=Employee.create_manager("alice")
engineer=Employee.create_engineer("bob")

print(manager.name, manager.position)
print(engineer.name, engineer.position)

