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
                        'annotations': result[0],  # Assuming annotations is a column in your table
                    })
                else:
                    print(f"No information found for image {image_id}")
            except Exception as e:
                print(f"Error retrieving information for image {image_id} from Snowflake: {str(e)}")

    except Exception as e:
        print(f"Error executing Snowflake query: {str(e)}")

    return annotations_list


if __name__ == "__main__":

    # Example usage
    image_ids_to_search = ['id_00000117_11_1_front.jpg', 'id_00000619_08_1_front.jpg', 'id_00001044_16_1_front.jpg', 'id_00000031_02_1_front.jpg', 'id_00000960_06_1_front.jpg', 'id_00000025_05_1_front.jpg', 'id_00000364_01_1_front.jpg', 'id_00001013_03_1_front.jpg', 'id_00000929_01_1_front.jpg', 'id_00000882_02_1_front.jpg', 'id_00000357_02_1_front.jpg', 'id_00000437_01_1_front.jpg', 'id_00000425_08_1_front.jpg', 'id_00000109_02_1_front.jpg', 'id_00000414_02_1_front.jpg', 'id_00000041_03_1_front.jpg', 'id_00000555_04_1_front.jpg', 'id_00000583_01_1_front.jpg', 'id_00000291_04_1_front.jpg', 'id_00000134_02_1_front.jpg', 'id_00000731_03_1_front.jpg', 'id_00000433_06_1_front.jpg', 'id_00000061_06_1_front.jpg', 'id_00000390_15_1_front.jpg', 'id_00000824_06_1_front.jpg', 'id_00000584_07_1_front.jpg', 'id_00000817_01_1_front.jpg', 'id_00000004_05_1_front.jpg', 'id_00000626_02_1_front.jpg', 'id_00000061_04_1_front.jpg', 'id_00000360_04_1_front.jpg', 'id_00000239_02_1_front.jpg', 'id_00000274_02_1_front.jpg', 'id_00000957_02_1_front.jpg', 'id_00000828_05_1_front.jpg', 'id_00000529_01_1_front.jpg', 'id_00000453_02_1_front.jpg', 'id_00000397_03_1_front.jpg', 'id_00000974_01_1_front.jpg', 'id_00000057_03_1_front.jpg', 'id_00000287_01_1_front.jpg', 'id_00000149_06_1_front.jpg', 'id_00000634_02_1_front.jpg', 'id_00000546_01_1_front.jpg', 'id_00000001_02_1_front.jpg', 'id_00000804_04_1_front.jpg', 'id_00000165_02_1_front.jpg', 'id_00000933_01_1_front.jpg', 'id_00000589_10_1_front.jpg', 'id_00000687_02_1_front.jpg']
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
