import boto3
aws_resource=boto3.resource("s3")
bucket=aws_resource.Bucket("labbucket05604e40")

response = bucket.create(
    ACL='public-read',
    CreateBucketConfiguration= {
        'LocationConstraint':  
},
    )

print(response)