#!/usr/bin/pythoimport glob
  
  
print('Named explicitly:')
for name in glob.glob('/home/geeks'):
    print(name)