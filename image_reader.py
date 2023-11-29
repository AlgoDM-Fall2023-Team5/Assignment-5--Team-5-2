import boto3
import pandas as pd
import os

# aws_access_key_id = os.environ.get('AWS_ACCESS_KEY_ID')
# aws_secret_access_key = os.environ.get('AWS_SECRET_ACCESS_KEY')

# print("AWS_ACCESS_KEY_ID:", aws_access_key_id)
# print("AWS_SECRET_ACCESS_KEY:", aws_secret_access_key)

# if aws_access_key_id is None or aws_secret_access_key is None:
#     raise ValueError("AWS credentials are missing. Please check your .env file.")

'''to access a file in the bucket 
s3.Bucket('Bucket_name').Object('file name').get()
to show all the object sin the bucket we do
s3.Bucket("Bucket_name").objects.all()
downlaod a file and read fromt the bucket
s3.Bucket('bycket_name).download_file(key = 'key name',Filename = 'filename')'''


s3 = boto3.resource(
    service_name = 's3',
    region_name = 'us-east-2',
    aws_access_key_id = 'AKIAQ4WOK7VQVKP4WJVB',
    aws_secret_access_key = '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'
    )

image_names = []
for obj in s3.Bucket('team5adm').objects.all():
    image_names.append(obj.key)

with open('image_path.txt', 'w') as file:
    for element in image_names:
        file.write(f"{element}\n")