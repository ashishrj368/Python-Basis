# TRY and EXCEPT
# try:
#     numerator=10
#     denominator=0
#     result=numerator/denominator
#     print(result)
# except:
#     print('Error :Denominator cannot be 0')

# try:
#     even_number=[2,4,6,8,10,12]
#     print(even_number[5])
# except:
#     print('index out of bound')

# else

try:
    num=int(input('Enter a number: '))
except ValueError:
    print('That is not a valid number!')
else:
    print(f'you entered the number:{num}')
finally:
    print('Execution complete.')
    

