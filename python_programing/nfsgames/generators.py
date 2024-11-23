def sqaure_number():
    n=10
    print('printed first')
    yield n

    n=n*2
    print('printed second')
    yield n

    n=n*3
    print('printed last')
    yield n
    
# a=sqaure_number()
# print(a)
# print(next(a))
# print(next(a))
# print(next(a))
# for value in sqaure_number():
#     print(value)

def sum_number():
    n=7
    print("first")
    yield n

    n=n+7
    print("second")
    yield n

    n=n+7+7
    print("third")
    yield n

# for value in sum_number():
#     print(value)

# z=sum_number();
# print(next(z))
# print(next(z))
# print(next(z))

def subtraction():
    n=170
    print("first")
    yield n

    n=n-20
    print("second")
    yield n

    n=n-25
    print("third")
    yield n

for value in subtraction():
    print(value)
