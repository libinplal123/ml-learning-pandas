sales_report = [
    {"date": "2026-01-01", "product": "Laptop", "category": "Electronics", "quantity": 2, "price": 55000, "salesperson": "Anil"},
    {"date": "2026-01-01", "product": "Mouse", "category": "Electronics", "quantity": 5, "price": 500, "salesperson": "Meera"},
    {"date": "2026-01-02", "product": "Chair", "category": "Furniture", "quantity": None, "price": 3500, "salesperson": "Rahul"},
    {"date": "2026-01-02", "product": "Desk", "category": "Furniture", "quantity": 1, "price": None, "salesperson": "Rahul"},
    {"date": "2026-01-03", "product": "Pen", "category": "Stationery", "quantity": 20, "price": 10, "salesperson": None},
    {"date": "2026-01-03", "product": "Notebook", "category": "Stationery", "quantity": 10, "price": 50, "salesperson": "Anil"},
    {"date": None, "product": "Printer", "category": "Electronics", "quantity": 1, "price": 12000, "salesperson": "Meera"},
    {"date": "2026-01-04", "product": "Monitor", "category": "Electronics", "quantity": 2, "price": None, "salesperson": "Anil"},
    {"date": "2026-01-05", "product": None, "category": "Furniture", "quantity": 1, "price": 8000, "salesperson": "Rahul"},
    {"date": "2026-01-05", "product": "Table Lamp", "category": None, "quantity": 3, "price": 1500, "salesperson": "Meera"}
]
import pandas as pd
df=pd.DataFrame(sales_report)
print(df.shape)
print(df.columns)
print(df.head())
print(df.tail())
print(df.isnull().sum()) # finding all null values then filling it
# filling null value in date column
most_frequent_date=df["date"].mode()[0]
df["date"].fillna(most_frequent_date,inplace=True) # inplace means same df is used
print(df)
df["product"].fillna("unknown",inplace=True)
# print(df)
# print(df.isnull().sum())
most_frequent_category=df["category"].mode()[0]
print(most_frequent_category)
df["category"].fillna(most_frequent_category,inplace=True) # df.dropna(subset=["column_name"],inplace=T/F)
average_quantity=df["quantity"].mean()                      # to delete entire row
df["quantity"].fillna(average_quantity,inplace=True)
# print(df.isnull().sum())
average_price=df["price"].mean()
df["price"].fillna(average_price,inplace=True)
# print(df.isnull().sum())
most_frquent_salesperson=df["salesperson"].mode()[0]
df["salesperson"].fillna(most_frquent_salesperson,inplace=True)
print(df)
print(df.isnull().sum())
# Sale count by category
print(df["category"].value_counts())
# Sale count by salesperson
print(df["salesperson"].value_counts())
# category electronics and quantity>2
print(df[(df["category"]== "Electronics") & (df["quantity"]>2)])
# group by
print(df.groupby("category")["price"].sum())
print(df.groupby("category")["quantity"].sum())
# sort by
print(df.sort_values(by="price",ascending=False))
# printing rows
print(df.loc[2])
print(df.iloc[1])
# costly product
print(df[df["price"]==df["price"].max()])
df["price"].idxmax() # returns index of max price
print(df.loc[df["price"].idxmax()])
# lowest price product
print(df.loc[df["price"].idxmin()])
# adding new column to df
df["revenue"]=df["price"]*df["quantity"]
print(df)
print(df.loc[0,["product","category"]])