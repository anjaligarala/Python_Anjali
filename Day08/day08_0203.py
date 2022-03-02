from lib2to3.pgen2.driver import Driver
import os
import sys


#print(os.getcwd())

#Cheks if any folder is present in current dir
dir_list = os.listdir('C:')
if 'Drivers' in dir_list:
    print("Dir present")
else:
    print("Dir not present")

#create new 5 folders in given dir 
for i in range(5):
    os.mkdir("test" + str(i))
