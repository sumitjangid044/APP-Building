import pandas as pd
import sqlite3

df = pd.read_csv('products.csv')

conn = sqlite3.connect('ecommerce.db') 

df.to_sql('products', conn, if_exists='replace', index= False)

cursor = conn.cursor()
for row in cursor.execute("SELECT * FROM products LIMIT 5"):
    print(row)
    
conn.close()