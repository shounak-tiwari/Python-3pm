# file handing is means that file is manage or save your data in secondary or permanent storage
# we have three modes which is work with files 
# read : read modes we use only read existing data we can not create files using read this read mode is use for reading the data which is store inside the files which is open by open function 
# write : write modes we use for create and write data in a file write modes is provide a type of facility where we erase previous data  and add new data
# append  : write modes we use for create and write data in a file append modes is provide a type of facility where we have previous data  and append new data append after previous data 

# object = open-class('name of file','modes of file')


file = open('student.txt','w')

file.write("This is arvind  ")


file.close()