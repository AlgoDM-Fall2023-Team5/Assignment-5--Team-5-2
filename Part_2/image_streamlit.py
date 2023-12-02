import snowflake.connector
import streamlit as st
from PIL import Image
import requests

# Snowflake connection parameters
snowflake_role = 'ACCOUNTADMIN'
snowflake_table_name = 'Tags'
snowflake_user = 'shirish'
snowflake_password = 'Northeastern123'
snowflake_account = 'PXTNTMC-FTB58373'
snowflake_database = 'CLOTHING_TAGS'
snowflake_schema = 'PUBLIC'
snowflake_warehouse = 'COMPUTE_WH'

# Function to retrieve annotations for images
def get_annotations_for_images(image_ids, conn, table_name):
    annotations_list = []

    try:
        cursor = conn.cursor()

        for image_id in image_ids:
            try:
                cursor.execute(f"SELECT annotations FROM {table_name} WHERE image = '{image_id}'")
                result = cursor.fetchone()

                if result:
                    annotations_list.append({
                        'image': image_id,
                        'annotations': result[0]  # Assuming annotations is a column in your table
                    })
                else:
                    print(f"No information found for image {image_id}")
            except Exception as e:
                print(f"Error retrieving information for image {image_id} from Snowflake: {str(e)}")

    except Exception as e:
        print(f"Error executing Snowflake query: {str(e)}")

    return annotations_list

# Function to search for similar images
def search_similar_images(image_path):
    # Replace with your Pinecone API key and index name
    pinecone_api_key = '7f78befa-055d-41ac-a90a-cff6a5282d66'
    index_name = 'adm4'

    # Convert image to binary data
    with open(image_path, 'rb') as f:
        image_data = f.read()

    # Send search request to Pinecone
    response = requests.post(
        'https://api.pinecone.io/v2/indexes/{}/query?top=10'.format(index_name),
        headers={'Authorization': 'Bearer {}'.format(pinecone_api_key)},
        json={'data': image_data, 'vectors': 'image'})

    if response.status_code == 200:
        similar_image_ids = response.json()['results']['ids']
        return similar_image_ids
    else:
        print('Error retrieving similar images from Pinecone:', response.text)
        return None

# Initialize Streamlit app
st.title('Image Similarity Search and Annotation Retrieval')

# Upload image
uploaded_image = st.file_uploader('Upload an image:', type='jpg')

# Process image and retrieve annotations
if uploaded_image:
    # Display uploaded image
    st.image(Image.open(uploaded_image))

    # Search for similar images
    similar_image_ids = search_similar_images(uploaded_image.name)

    # Retrieve annotations for similar images
    if similar_image_ids:
        # Connect to Snowflake
        conn = snowflake.connector.connect(
            user=snowflake_user,
            password=snowflake_password,
            account=snowflake_account,
            warehouse=snowflake_warehouse,
            database=snowflake_database,
            role=snowflake_role
        )

        # Get annotations for similar images
        annotations = get_annotations_for_images(similar_image_ids, conn, snowflake_table_name)

        # Display annotations
        for annotation in annotations:
            st.write(f"Image: {annotation['image']}")
            st.write(f"Annotations: {annotation['annotations']}")

st.stop()
