import os
from pathlib import Path
from llama_index.multi_modal_llms.openai import OpenAIMultiModal
from llama_index import SimpleDirectoryReader
from llama_index.indices.multi_modal.base import MultiModalVectorStoreIndex
from llama_index.vector_stores import PineconeVectorStore
from llama_index import StorageContext
import pinecone
import snowflake.connector
import boto3

# Set up Pinecone client
pinecone.init(api_key="878f92d2-ce36-4be5-bbc0-05a56ff092fc")
pinecone_index = pinecone.Index(index_name="adm4")

# Set up Snowflake connection
snowflake_conn = snowflake.connector.connect(
    user='shirish',
    password='Northeastern123',
    account='PXTNTMC-FTB58373',
    warehouse='COMPUTE_WH',
    database='CLOTHING_TAGS',
    schema='PUBLIC'
)

# Set up MultiModal index
storage_context = StorageContext.from_defaults(vector_store=PineconeVectorStore(pinecone_index))

# Function to fetch an image from S3
def fetch_image_from_s3(bucket_name, key, region='us-east-2', aws_access_key_id='AKIAQ4WOK7VQVKP4WJVB', aws_secret_access_key='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'):
    s3 = boto3.client('s3', region_name=region, aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
    local_path = f"new_dataset_assignment_5/new_dataset/{key}"  # Adjust the local path as needed
    s3.download_file(bucket_name, key, local_path)
    return local_path

# Function to encode image using CLIP
def encode_image_with_clip(image_path):
    from PIL import Image
    import torch
    import clip
    from torchvision.transforms import Compose, Resize, CenterCrop, ToTensor, Normalize

    # Load the pre-trained CLIP model
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model, transform = clip.load("ViT-B/32", device=device)

    # Encode image using CLIP
    image = Image.open(image_path).convert("RGB")
    image_input = transform(image).unsqueeze(0).to(device)
    image_embedding = model.encode_image(image_input)
    image_embedding = image_embedding.squeeze().cpu().detach().numpy()

    return image_embedding

# Function to encode text using GPT4V
def encode_text_with_gpt4v(query_text):
    # Implement text encoding using GPT4V
    # Add your code here

# Function to display or process retrieval results
def display_retrieval_results(retrieval_results):
    # Implement result display or processing
    # Add your code here

# Given an image, find similar images and text tags
def find_similar_images_and_text(image_path):
    query_image_embedding = encode_image_with_clip(image_path)
    retrieval_results = index.retrieve_similar_images_and_text(query_image_embedding)
    display_retrieval_results(retrieval_results)

# Given a text string, find matching images
def find_matching_images(query_text):
    query_text_embedding = encode_text_with_gpt4v(query_text)
    retrieval_results = index.retrieve_matching_images(query_text_embedding)
    display_retrieval_results(retrieval_results)

# Example usage
bucket_name = 'team5adm'
image_key = 'your_image_key.jpg'
local_image_path = fetch_image_from_s3(bucket_name, image_key)
find_similar_images_and_text(local_image_path)
find_matching_images("description of the desired image")
