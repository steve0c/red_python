import boto3
#delete one object

#s3_resource=boto3.client("s3")
#s3_resource.delete_object(Bucket='labbucket0560440', Key='Python.py')

#delete multiple objects

import os 
import glob
objects=s3_resource.list_objects(Bucket="labbucket0560440")["Contents"]
for object in objects:
    response=s3_resource.delete_object(Bucket="labbucket0560440"), 

    key=object["Key"]
    print(response)
    
