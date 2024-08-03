import pandas as pd
from snowflake_connection import get_snowflake_connection
from azure_connection import download_blob

def fetch_data_from_snowflake():
    conn = get_snowflake_connection()
    query = "SELECT * FROM MEDICAL_DATA"
    df = pd.read_sql(query, conn)
    conn.close()
    return df

def fetch_data_from_azure():
    container_name = "your-container-name"
    blob_name = "sample_medical_data.csv"
    download_file_path = "../data/sample_medical_data.csv"
    download_blob(container_name, blob_name, download_file_path)
    df = pd.read_csv(download_file_path)
    return df

def transform_data(df):
    # Add your data transformation logic here
    transformed_df = df  # Example: no transformation
    return transformed_df

def main():
    df_snowflake = fetch_data_from_snowflake()
    df_azure = fetch_data_from_azure()
    df_combined = pd.concat([df_snowflake, df_azure])
    transformed_df = transform_data(df_combined)
    transformed_df.to_csv('../data/transformed_medical_data.csv', index=False)

if __name__ == "__main__":
    main()
