import snowflake.connector
from snowflake.connector.pandas_tools import write_pandas

# Snowflake connection parameters
snowflake_user = 'your_username'
snowflake_password = 'your_password'
snowflake_account = 'your_account_url'
snowflake_database = 'your_database'
snowflake_schema = 'your_schema'
snowflake_warehouse = 'your_warehouse'

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
table_name = 'your_table'

# Use the write_pandas function to upsert the DataFrame into Snowflake
write_pandas(conn, df, table_name)

# Close the connection
conn.close()
