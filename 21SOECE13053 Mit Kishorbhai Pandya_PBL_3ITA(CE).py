import os, shutil
path = input('Enter the folder path: ')
list_of_extensions = os.listdir(path)

for file in list_of_extensions:
    filename, extension = os.path.splitext(file)
    extension = extension[1:]
    print(extension)

    if os.path.exists(path+'/'+extension):
        shutil.move(path + '/' + file, path + '/' + extension + '/' + file)
    
    else: 
        os.makedirs(path + '/' + extension)
        shutil.move(path +'/' + file, path + '/' + extension + '/' + file)