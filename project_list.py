#!/usr/bin/env python
#project week 13
import os


directory = os.getcwd()
file_attr_list = []

for file_name in os.listdir(directory):
    
    for file_size in range(os.path.getsize(directory)):
        
        file_attr = {
    "name": file_name,
        "size": file_size,
}

file_attr_list.append(file_attr)

print(file_attr)

