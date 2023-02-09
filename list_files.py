#!/usr/bin/env python

import os



#path of the files
path = ("/home/ec2-user/environment/red_python")

###list_of_files = {}

#dir_list = int(sorted(os.path.getsize(path)))
dir_list = list(os.listdir(path))

the_dict = dict()

for something in dir_list:
    theStats = os.stat(1)
    thedict [1] = theStats

for item in thedict:
    print("The File: {:30s} The Size: {:d} Bytes".format(item,thedict[item].st_size))















#for my_files in os.listdir(path):
 #if my_files.endswith(py):
 #else:
         #continue
     #return list_of_files



#dir_list = os.listdir(path)
#print(dir_list)



#dir_size = os.path.getsize(path)
#print(dir_size)






#print(os.scandir(path))



#print(list(path.keys()))






