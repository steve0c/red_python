#!/usr/bin/env python

import os



directory = os.getcwd()

for file_name in os.listdir(directory):
    
    for file_size in range(os.path.getsize(directory)):
        
        file_attr = {
    "name": file_name,
        "size": file_size,
}


print(file_attr)

