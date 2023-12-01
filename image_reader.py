import boto3
import pandas as pd
import os

# aws_access_key_id = os.environ['AWS_ACCESS_KEY_ID']
# aws_secret_access_key = os.environ['AWS_SECRET_ACCESS_KEY']

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

# resource
s3 = boto3.client(
    service_name = 's3',
    region_name = 'us-east-2',
    aws_access_key_id = 'AKIAQ4WOK7VQVKP4WJVB',
    aws_secret_access_key = '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'
    )

# image_names = []
# for obj in s3.Bucket('team5adm').objects.all():
#     image_names.append(obj.key)

# with open('image_path.txt', 'w') as file:
#     for element in image_names:
#         file.write(f"{element}\n")

bucket_name = 'team5adm'
file_key = 'new_dataset_assignment_5/new_dataset/id_00000003_02_1_front.jpg'

file_path = f's3://{bucket_name}/{file_key}'

# Download the file locally
local_file_path = 'downloaded_file.jpg'
s3.download_file(bucket_name, file_key, local_file_path)

print(f"File downloaded to: {local_file_path}")

#s3.Bucket('Bucket_name').Object('new_dataset_assignment_5/new_dataset/id_00000003_02_1_front.jpg').get()