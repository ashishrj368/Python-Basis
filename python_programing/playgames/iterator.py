# mytuple=('apple','banana','cherry')
# my=iter(mytuple)

# print(next(my))
# print(next(my))
# print(next(my)) 

# list1=['apple','banana',54,25,'kiwi']
# king=iter(list1)

# print(next(king))
# print(next(king))
# print(next(king))
# print(next(king))
# print(next(king))

# class my_number:
#     def __iter__(self):
#         self.a=1
#         return self
#     def __next__(self):
#         x=self.a
#         self.a+=1
#         return x
    
# myclass=my_number()
# my=iter(myclass)

# print(next(my))
# print(next(my))
# print(next(my))
# print(next(my))
# print(next(my))


# class sqaure_number():
#     def __iter__(self):
#         self.a=5
#         return self
#     def __next__(self):
#         x=self.a
#         self.a*=5
#         return x
# my_number=sqaure_number()
# result=iter(my_number)

# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))


# class quotient():
#     def __iter__(self):
#         self.a=1000
#         return self
#     def __next__(self):
#         x=self.a
#         self.a/=10
#         return x
# my_num=quotient()
# result=iter(my_num)

# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))

# class subraction():
#     def __iter__(self):
#         self.y=1000
#         return self
#     def __next__(self):
#         x=self.y
#         self.y-=77
#         return x

# sub=subraction()
# result=iter(sub)

# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))


# class cube():
#     def __iter__(self):
#         self.z=5
#         return self
#     def __next__(self):
#         x=self.z
#         self.z*=5
#         return x

# cubes=cube()
# result=iter(cubes)

# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))


class summ():
    def __iter__(self):
        self.y=100000
        return self
    def __next__(self):
        x=self.y
        self.y+=58465
        return x
    
add=summ()
result=iter(add)

print(result(summ))
print(result(summ))
print(result(summ))
print(result(summ))
print(result(summ))
print(result(summ))


