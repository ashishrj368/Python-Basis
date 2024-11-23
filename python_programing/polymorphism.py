# class calculation:
    # def add(self,a,b):
    #     x=a+b
    #     return x
    # def add(self,a,b,c):
    #     x=a+b+c
    #     return x
# obj1=calculation()
# print(obj1.add(10,20))
# print(obj1.add(10,20,30))

class animal:
    def speak(self):
        return 'animal_sound'
class dog(animal):
    def speak(self):
            return 'bark'
class cat(animal):
    def speak(self):
            return 'meow'
class lion(animal):
    def speak(self):
            return 'roar'
x=dog()
print(x.speak())
y=cat()
print(y.speak())
z=lion()
print(z.speak())

# class animal:
#     def speak(self):
#         return "animal_sound"
    
# class dog(animal):
#     def speak(self):
#         return "bark"

# class cat(animal):
#     def speak(self):
#         return "meow"
# x=dog()
# print(x.speak())
# c=cat()
# print(c.speak())

