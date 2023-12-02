import snowflake.connector

def get_annotations_for_images(image_ids, conn, table_name):
    annotations_list = []

    try:
        cursor = conn.cursor()

        for image_id in image_ids:
            try:
                print(f"new_dataset_assignment_5/new_dataset/{image_id}")
                cursor.execute(f"SELECT annotations FROM {table_name} WHERE image = 'new_dataset_assignment_5/new_dataset/{image_id}'")
                result = cursor.fetchone()

                if result:
                    annotations_list.append({
                        'image': image_id,
                        'annotations': result['annotations'],  # Assuming annotations is a column in your table
                    })
                else:
                    print(f"No information found for image {image_id}")
            except Exception as e:
                print(f"Error retrieving information for image {image_id} from Snowflake: {str(e)}")

    except Exception as e:
        print(f"Error executing Snowflake query: {str(e)}")

    return annotations_list

# Example usage
image_ids_to_search = ['id_00001757_05_1_front.jpg', 'id_00004504_03_1_front.jpg', 'id_00005602_01_1_front.jpg', 'id_00001384_12_1_front.jpg', 'id_00001384_14_1_front.jpg', 'id_00001596_05_1_front.jpg', 'id_00003494_12_1_front.jpg', 'id_00002821_04_1_front.jpg', 'id_00006056_04_1_front.jpg', 'id_00006056_03_1_front.jpg', 'id_00005918_06_1_front.jpg', 'id_00005085_03_1_front.jpg', 'id_00005954_05_1_front.jpg', 'id_00005602_03_1_front.jpg', 'id_00001404_02_1_front.jpg', 'id_00002201_01_1_front.jpg', 'id_00003343_19_1_front.jpg', 'id_00005085_08_1_front.jpg', 'id_00003494_06_1_front.jpg', 'id_00007721_47_1_front.jpg', 'id_00006863_42_1_front.jpg', 'id_00003494_04_1_front.jpg', 'id_00006546_12_1_front.jpg', 'id_00000879_01_1_front.jpg', 'id_00001619_02_1_front.jpg']

# Replace these placeholders with your actual Snowflake credentials
snowflake_role = 'ACCOUNTADMIN'
snowflake_table_name = 'Tags'
snowflake_user = 'shirish'
snowflake_password = 'Northeastern123'
snowflake_account = 'PXTNTMC-FTB58373'
snowflake_database = 'CLOTHING_TAGS'
snowflake_schema = 'PUBLIC'
snowflake_warehouse = 'COMPUTE_WH'

# Connect to Snowflake
conn = snowflake.connector.connect(
    user=snowflake_user,
    password=snowflake_password,
    account=snowflake_account,
    warehouse=snowflake_warehouse,
    database=snowflake_database,
    role=snowflake_role
)

# Get annotations for the specified image IDs
annotations_result = get_annotations_for_images(image_ids_to_search, conn, snowflake_table_name)

print(f"Annotations for images: {annotations_result}")
