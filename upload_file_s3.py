import boto3
#how to uploaod single file
#Filename=file path
#key="new file name in buket"
#Bucket="Bucketname"

s3_resource=boto3.client("s3")

s3_resource.upload_file(Filename="/home/ec2-user/environment/red_python/lists.py", Bucket="labbucket0560440",Key="project_list.py")


