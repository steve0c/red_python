#finding the creation date of s3 buckets
import boto3
s3_resource=boto3.client("s3")
#s3_resource.list_buckets()["Buckets"][0]["Name"]
#creation_date=s3_resource.list.buckets()["Buckets"][0]["creation_date"]
for bucket in s3_resource.list_buckets()["Buckets"]:
    print(bucket["Name"])
    print(bucket["CreationDate"])


