import pandas as pd
from sqlalchemy import create_engine

df_clean = pd.read_csv(
    r"C:\Users\Asus\Downloads\AI_Ecommerce_Project\online_retail_sql_ready.csv",
    low_memory=False
)

engine = create_engine(
    "mysql+pymysql://root:Root%40123@localhost/ecommerce_project"
)

df_clean.to_sql(
    "ecommerce_sales",
    con=engine,
    if_exists="replace",
    index=False,
    chunksize=5000
)

print("Data imported successfully")