import streamlit as st
import requests
from PIL import Image
from io import BytesIO
from sentence_transformers import SentenceTransformer
import json  # Add this import
import snowflake.connector
import os
from PIL import Image
import boto3



from image_fetcher import search_and_display_images
from image_to_image import get_annotations_for_images


#image_encoder = SentenceTransformer('clip-ViT-B-32')

st.title("Image Similarity Search")

uploaded_image = st.file_uploader("Choose an image...", type="jpg")

def encode_image(uploaded_image, encoder):
    image_bytes = uploaded_image.read()
    image_pil = Image.open(BytesIO(image_bytes))

    # Encode the image
    image_input = encoder.encode(image_pil, convert_to_tensor=True)
    image_features = image_input.flatten()

    return image_features
snowflake_role = 'ACCOUNTADMIN'
snowflake_table_name = 'Tags'
snowflake_user = 'shirish'
snowflake_password = 'Northeastern123'
snowflake_account = 'PXTNTMC-FTB58373'
snowflake_database = 'CLOTHING_TAGS'
snowflake_schema = 'PUBLIC'
snowflake_warehouse = 'COMPUTE_WH'

conn = snowflake.connector.connect(
    user=snowflake_user,
    password=snowflake_password,
    account=snowflake_account,
    warehouse=snowflake_warehouse,
    database=snowflake_database,
    role=snowflake_role
)

if uploaded_image is not None:
    if st.button("Find Similar Images"):
        st.image(uploaded_image, caption="Uploaded Image.", use_column_width=True)

        # Encode the image
        image_features = encode_image(uploaded_image, SentenceTransformer('clip-ViT-B-32'))

        # Convert the NumPy array to a list
        image_features_list = image_features.tolist()
        # st.write(image_features_list)


        closest_image_ids, images_from_s3 = search_and_display_images(image_features_list)
        st.write(closest_image_ids)

        annotations_result = get_annotations_for_images(closest_image_ids, conn, snowflake_table_name)

        st.header("Annotations")
        st.write(annotations_result)



        # image_folder_path = "images"


        # image_files = [f for f in os.listdir(image_folder_path) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]

        # # Output folder for converted images
        # output_folder_path = "/path/to/your/converted/images"

        # # Create the output folder if it doesn't exist
        # os.makedirs(output_folder_path, exist_ok=True)

        # st.header("Similar Images")
        # for image_file in image_files:
        #     # Create the full path to the input image file
        #     input_image_path = os.path.join(image_folder_path, image_file)

        #     # Determine the output image file path with the new format (JPEG)
        #     output_image_file = os.path.splitext(image_file)[0] + ".jpeg"
        #     output_image_path = os.path.join(output_folder_path, output_image_file)

        #     # Open the input image
        #     image = Image.open(input_image_path)

        #     # Save the image in JPEG format
        #     image.save(output_image_path, "JPEG")

        #     # Close the image
        #     image.close()

        #     # Display the converted image using Streamlit
        #     st.image(output_image_path, caption=output_image_file, use_column_width=True)
        s3_client = boto3.client(service_name = 's3',
                aws_access_key_id='AKIASGVOLPG2BPBLER6T',
                aws_secret_access_key='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',
                region_name = 'us-east-2')
        

        for i in closest_image_ids:
            img = s3_client.get_object(Bucket='assignment4admt5', Key=f'dataset/{i}')
            


            image_bytes = img['Body'].read()

            # Display the image in Streamlit
            st.image(image_bytes)

        del uploaded_image
        del image_features
        del image_features_list
        del closest_image_ids
        del images_from_s3
        del annotations_result
        del s3_client
        del img








