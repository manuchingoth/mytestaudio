import os

print(os.name)

def current_path():
    cwd = os.getcwd()
    print(cwd)

current_path()

'''#change directory
os.chdir('../')

current_path()
#change directory back to previous one  
os.chdir('monday')

current_path()

#makedir method
newdirectory = "GeekforGeeks3"
parentdirectory = "/home/monday/"
newpathtocreate = os.path.join(parentdirectory, newdirectory)
createdpath = str(os.mkdir(newpathtocreate))
print(createdpath)

newdirectory4 = "GeekforGeeks9"
parentdirectory = "/home/monday/sample3"
newpathtocreate = os.path.join(parentdirectory, newdirectory4)
mode = 0o666
createdpath4 = os.makedirs(newpathtocreate, mode)
print(createdpath4)'''

pathtoretrievefilesfolders = "/"

#retrieve files and folders
filesfolders = os.scandir(pathtoretrievefilesfolders)
print("Files and Folders ",filesfolders)

'''pathtoretrievefilesfolders = "/"
#retrieve only files from the path
files = os.listdir(pathtoretrievefilesfolders)
for file in files:
    if os.path.isfile(file):
        print("Only Files ", file)
    else:
        print("No Files")

#retrieve only folders from the path
folders = os.listdir(pathtoretrievefilesfolders)
for folder in folders:
    if os.path.isdir(folder):
        print("Only Folders ", folder)
    else:
        print("No Folders")'''



