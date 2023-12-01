import snowflake.connector
from snowflake.connector.pandas_tools import write_pandas
import pandas as pd


df=pd.read_csv("tags.csv")

# Snowflake connection parameters
snowflake_user = 'shirish'
snowflake_password = 'Northeastern123'
snowflake_account = 'PXTNTMC-FTB58373'
snowflake_database = 'CLOTHING_TAGS'
snowflake_schema = 'PUBLIC'
snowflake_warehouse = 'COMPUTE_WH'

# Create a Snowflake connection
conn = snowflake.connector.connect(
    user=snowflake_user,
    password=snowflake_password,
    account=snowflake_account,
    warehouse=snowflake_warehouse,
    database=snowflake_database,
    schema=snowflake_schema
)

# Assuming your table name is 'your_table'
table_name = 'Tags'

# Use the write_pandas function to upsert the DataFrame into Snowflake
write_pandas(conn, df, table_name)

# Close the connection
conn.close()
