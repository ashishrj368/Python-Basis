# def check_even(numbers):
#     if numbers % 2 == 0:
#         return True
#     return False
# numbers = [1,2,3,4,5,6,7,8,9,10]
# even_numbers=filter(check_even,numbers)
# even_numbers_finals=list(even_numbers)
# print(even_numbers_finals)

# letters=['a','b','c','d','e','f','g','h','i']
# def check_vowels(letters):
#     vowels=['a','e','i','o','u']
#     if letters in vowels:
#         return True
#     else:
#         return False
# check_vowels=filter(check_vowels,letters)
# check_vowels_finals=list(check_vowels)
# print(check_vowels_finals)

# numbers=[1,2,3,4]
# def square(numbers):
#     return numbers*numbers
# squared_numbers=map(square,numbers)
# result=list(squared_numbers)
# print(result)

# numbers=[5,6,7,8,9]
# def cube(numbers):
#     return numbers *numbers*numbers
# cubes_numbers=map(cube,numbers)
# result=list(cubes_numbers)
# print(result)

# list1=[1,2,3,4]
# from functools import reduce
# product=reduce(lambda x,y:x*y,list1)
# print(product)

# numbers=[5,6,7,8]
# from functools import reduce
# sum=reduce(lambda x,y:x+y,numbers)
# print(sum)

# letters=['j','k','l','m','n','o']
# def find_vowels(letters):
#     vowels=('a','e','i','o','u')
#     if letters in vowels:
#         return True
#     else:
#         return False
# find_vowels=filter(find_vowels,letters)
# result=list(find_vowels)
# print(result)

letters=['p','q','r','s','t','u','v','w','x','y','z']
vowels=['a','e','i','o','u']
def find_vowels(letters):
    if letters in vowels:
        return True
    else:
        return False
find_vowels=filter(find_vowels,letters)
result=list(find_vowels)
print(result)