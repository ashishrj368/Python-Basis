# create_zip_file

# f=open('games.zip',"x")

# # write_zip_file
# import zipfile
# with zipfile.ZipFile('games.zip','w')as f:
#     f.write('ashi.txt')
#     f.write('ashi2.txt')
#     f.write('iterator.py')
#     f.write('movies.csv')


# Read_zip_file

# import zipfile
# with zipfile.ZipFile('games.zip','r')as f:
#     f.extractall('playgames')
#     list1=f.namelist()
#     print(list1)


# f=open('nfs.zip','x')

# import zipfile
# with zipfile.ZipFile('nfs.zip','w')as file:
#     file.write('lambda.py')
#     file.write('generators.py')
import zipfile
with zipfile.ZipFile('nfs.zip','r')as file:
    file.extractall('nfsgames')
    result=file.namelist()
    print(result)