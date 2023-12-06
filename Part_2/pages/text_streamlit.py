import streamlit as st
import clip
import torch
import numpy as np
import pandas as pd
from PIL import Image
import boto3


# Load CLIP model
device = "cuda" if torch.cuda.is_available() else "cpu"
# model, preprocess = clip.load("ViT-B/32", device=device)

# Function to encode search query
def encode_search_query(search_query):
    with torch.no_grad():
        text_encoded = clip.load("ViT-B/32", device=device)[0].encode_text(clip.tokenize(search_query).to(device))
        text_encoded /= text_encoded.norm(dim=-1, keepdim=True)
    return text_encoded

# Function to find best matches
def find_best_matches(text_features, image_features, image_ids, results_count=3):
    similarities = (image_features @ text_features.T).squeeze(1)
    best_image_idx = (-similarities).argsort()
    return [image_ids[i] for i in best_image_idx[:results_count]]

# Function for image search
def search(search_query, image_features, image_ids, results_count=3):
    text_features = encode_search_query(search_query)
    return find_best_matches(text_features, image_features, image_ids, results_count)

# Load image features and image IDs
features_path = "features" 
image_ids = pd.read_csv(f"{features_path}/image_ids.csv")
image_ids = list(image_ids['image_id'])
image_features = np.load(f"{features_path}/features.npy")
if device == "cpu":
    image_features = torch.from_numpy(image_features).float().to(device)
else:
    image_features = torch.from_numpy(image_features).to(device)

# Streamlit app
st.title("Image Search using Text Input")

# Input search query
search_query = st.sidebar.text_input("Enter a search query", 'T shirt')

# Number of results to display per query
n_results_per_query = 5  

if st.sidebar.button("Search"):
    result_image_ids = search(search_query, image_features, image_ids, n_results_per_query)

    st.text(search_query)
    columns = st.columns(n_results_per_query)
    s3_client = boto3.client(service_name = 's3',
            aws_access_key_id='AKIAQ4WOK7VQVKP4WJVB',
            aws_secret_access_key='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',
            region_name = 'us-east-2')
    

    for i in result_image_ids:
        st.write(i)
    for i in result_image_ids:
        try:
            img = s3_client.get_object(Bucket='team5adm', Key=f'new_dataset_assignment_5/new_dataset/{i}.jpg')
            image_bytes = img['Body'].read()
            st.image(image_bytes)
            #columns.image(image_bytes, caption=f"Image {i}", use_column_width=True)
        except s3_client.exceptions.NoSuchKey:
                pass
        