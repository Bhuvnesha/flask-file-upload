import os

# check if file exists or not
# if os.path.exists('test.xlsx'):
#     print("File exists!")
# else:
#     print("File not exists!")

# create directory
# if not os.path.exists('test_folder'):
#     os.mkdir('test_folder')
#     print("Directory created !")
# else:
#     print("Directory already exists!")

# list files in drirectory
# files = os.listdir('templates')
# print("Files in directory:", files)

# Join paths to create a filepath
folder = 'my_folder'
filename = 'example.txt'
filepath = os.path.join(folder, filename)
print("Full filepath:", filepath)