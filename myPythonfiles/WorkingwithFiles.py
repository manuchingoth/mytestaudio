
import os

'''for myfile in  os.listdir("/home/monday/sample3"):
    if myfile.endswith('.txt'):
        print(myfile)

#using fnmatch
import fnmatch

for root, dirnames, filenames in os.walk('/home/monday/sample3'):   #os.walk() is a new thing
    for filename in fnmatch.filter(filenames, '*.txt'):
        print(filename)

import fnmatch
for f_name in os.listdir("/home/monday/sample3"):
    if fnmatch.fnmatch(f_name,'*.txt'):
        print(f_name)

import fnmatch
for f_name in os.listdir("/home/monday/sample3"):
    if fnmatch.fnmatch(f_name,'data_*_backup.txt'):
        print(f_name)'''

#using glob
'''import glob
somefile = glob.glob('*.py')
print(somefile) #output will be in an iterated object format
for name in glob.glob('*.py'):
    print(name)
path = '/home/monday/sample3'
for filename in glob.glob(path + '/*.txt'):
    print(filename)

import glob
for file in glob.iglob('**/*.py', recursive=True):
    print(file)

from pathlib import Path
p = Path('.')
for name in p.glob('*es*'):
    print(name)'''

for dirpath,dirname,files in os.walk('/home/monday'):
    print("directory is ",dirpath)
    for file_name in files:
        print(file_name)
