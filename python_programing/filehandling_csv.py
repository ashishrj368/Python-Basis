# csv_file_handling

# file_creating

# f=open('movies.csv','x')

# write_file

# import csv
# with open('movies.csv','w',newline='')as file:
#     writer=csv.writer(file)
#     writer.writerow(['sn', 'actor', 'movie', 'movie_type'])
#     writer.writerow([1, 'Mohanlal', 'Barroz', 'Fantasy'])
#     writer.writerow([2, 'Mammoty', ' Big_B', 'Action'])
#     writer.writerow([3, 'Dileep', 'Crazy_gopalan', "Comady"])
#     writer.writerow([4, 'Jayaram', 'Aanachantham', "comady"])
#     writer.writerow([5, 'Privthiraj', 'Hero', 'Action_comady'])


# file_reading

# import csv
# with open('movies.csv','r')as file:
#     reader=csv.reader(file)
#     for row in reader:
#         print(row)
import csv
with open('movies.csv','r')as file:
    reader=csv.reader(file)
    for row in reader:
        print(row)
        

