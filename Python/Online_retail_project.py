import pandas as pd

df = pd.read_csv(
    r"C:\Users\Asus\Downloads\AI_Ecommerce_Project\online_retail_II.csv",
    low_memory=False
)

print(df.head())
print(df.shape)

# Check Missing Values
print(df.isnull().sum())  

# Check Duplicate Records
duplicates = df.duplicated().sum()  
print("Duplicate Rows:", duplicates)

# Rename columns
df.columns = [
    'InvoiceNo',
    'StockCode',
    'Description',
    'Quantity',
    'InvoiceDate',
    'UnitPrice',
    'CustomerID',
    'Country'
]

#Remove Missing values which are present in Customer IDs
df = df.dropna(subset=['CustomerID']) 

#Remove Missing values which are present in Description
df = df.dropna(subset=['Description']) 

# Remove duplicates
df = df.drop_duplicates()

# Check Data Types
df.info()

# Check Missing Values after removal
print(df.isnull().sum())  

# Check Duplicate Records after removal
duplicates = df.duplicated().sum()  
print("Duplicate Rows:", duplicates)

# Cancelled Orders
cancelled_orders = df[df['InvoiceNo'].astype(str).str.startswith('C')]
print(cancelled_orders)

# Negative Quantity
negative_qty = df[df['Quantity'] < 0]
print(negative_qty)

# Zero Price
zero_price = df[df['UnitPrice'] <= 0]
print(zero_price)

# To get the count of Cancelled orders, negative quantity and Zero price
print("Cancelled Orders:", cancelled_orders.shape[0])
print("Negative Quantity:", negative_qty.shape[0])
print("Zero Price:", zero_price.shape[0])

# Remove cancelled orders, negative quantities and invalid prices
df_clean = df[
    (~df['InvoiceNo'].astype(str).str.startswith('C')) &
    (df['Quantity'] > 0) &
    (df['UnitPrice'] > 0)
]

print("Original rows:", df.shape[0])  # number of rows before cleaning
print("Cleaned rows:", df_clean.shape[0]) # number of rows after cleaning
print(df.head())  # preview first few rows

# Create Revenue Column (Revenue = Quantity × Price)
df_clean["Revenue"] = (df_clean["Quantity"] * df_clean['UnitPrice'])

# Convert Date Formate
df_clean['InvoiceDate'] = pd.to_datetime(df_clean['InvoiceDate'])

"""# Format as dd/mm/yyyy
df['InvoiceDate'] = df['InvoiceDate'].dt.strftime('%d-%m-%Y')"""

# Create Month
df_clean["Month"] = df_clean['InvoiceDate'].dt.month

# Create Year
df_clean["Year"] = df_clean['InvoiceDate'].dt.year

# Create Day
df_clean["Day"] = df_clean['InvoiceDate'].dt.day

# Create Hour
df_clean["Hour"] = df_clean['InvoiceDate'].dt.hour

# Revenue Distribution
df_clean['Revenue'].describe()

# Top Countries
Top_Countries = df_clean.groupby(
    'Country'
)['Revenue'].sum()

# Top Products
Top_Products = df_clean.groupby(
    'Description'
)['Revenue'].sum()

# Top Customers
Top_Customers = df_clean.groupby(
    'CustomerID'
)['Revenue'].sum()

# Create final dataset
df_clean.to_csv(
    'online_retail_clean.csv',
    index=False
)

print(df_clean.shape)


# Rename Columns.
df_clean.columns = [
'InvoiceNo',
'StockCode',
'Description',
'Quantity',
'InvoiceDate',
'UnitPrice',
'CustomerID',
'Country',
'Revenue',
'Month',
'Year',
'Day',
'Hour'
]

# Export again
df_clean.to_csv(
    'online_retail_sql_ready.csv',
    index=False
)

# Validation
print("Shape:", df_clean.shape)
print("Cancelled Orders:",
      df_clean['InvoiceNo'].astype(str).str.startswith('C').sum())
print("Negative Quantity:",
      (df_clean['Quantity'] < 0).sum())
print("Negative Revenue:",
      (df_clean['Revenue'] < 0).sum())

# Save clean file
df_clean.to_csv(
    r"C:\Users\Asus\Downloads\AI_Ecommerce_Project\online_retail_sql_ready.csv",
    index=False
)

print(df_clean.shape)
print("File created successfully")



