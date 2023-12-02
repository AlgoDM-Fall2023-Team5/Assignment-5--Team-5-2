import pandas as pd
import os

# with open("new_pinecone_tags.csv", 'r'):
df=pd.read_csv(r"D:\Projects\ADM Assg 5\Assignment-5--Team-5\Part_1\new_pinecone_tags.csv")

x=list(df.IMAGE)
print(type(x))
image_path=[]
for i in x:
    image_path.append(i.split("/")[2])

# print(image_path)

import os
import shutil

def copy_images(source_folder, destination_folder, image_names):
    for image_name in image_names:
        source_path = os.path.join(source_folder, image_name)
        destination_path = os.path.join(destination_folder, image_name)

        try:
            shutil.copy(source_path, destination_path)
            print(f"Successfully copied {image_name} to {destination_folder}")
        except FileNotFoundError:
            print(f"Error: {image_name} not found in {source_folder}")
        except Exception as e:
            print(f"Error: {e}")

# Example usage:
source_folder = r"D:\Projects\ADM Assg 5\Assignment-5--Team-5\new_dataset"
destination_folder = r"D:\Projects\ADM Assg 5\Assignment-5--Team-5\new_dataset_2"
image_names_to_copy = image_path

copy_images(source_folder, destination_folder, image_names_to_copy)


