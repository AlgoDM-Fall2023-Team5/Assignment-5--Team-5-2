import boto3
import streamlit as st
from io import BytesIO
from PIL import Image

# AWS credentials
aws_access_key_id = 'AKIAQ4WOK7VQVKP4WJVB'
aws_secret_access_key = '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'

# S3 bucket information
bucket_name = 'team5adm'
file_key = 'new_dataset_assignment_5/new_dataset/id_00000003_02_1_front.jpg'

# Create an S3 client
s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)

# Fetch the image from S3
image_obj = s3.get_object(Bucket=bucket_name, Key=file_key)
image_content = image_obj['Body'].read()

# Create a BytesIO object to treat the content as an in-memory binary stream
image_stream = BytesIO(image_content)

# Open the image using PIL
image = Image.open(image_stream)

# Display the image in Streamlit
st.image(image, caption='S3 Image', use_column_width=True)

# Optionally, you can provide additional information or metadata about the image
st.write(f"File Path: s3://{bucket_name}/{file_key}")
