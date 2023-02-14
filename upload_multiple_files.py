import boto3
import os
import glob
#upload multiple files to s3 bucket
s3_resource=boto3.client("s3")
cwd=os.getcwd()
cwd=cwd+"/red_python/"
files=glob.glob(cwd+"*.py")
#files =glob.glob(os.path.join(os.path.dirname(__file__), '*.py'))
for file in files:
    s3_resource=boto3.client("s3")
    s3_resource.upload_file(Filename="file", Bucket="labbucket0560440",Key=file.split("/")[-1])