import pandas as pd
import sqlite3


df = pd.read_csv('tamveriseti.csv') #CSV'nin yolu

conn = sqlite3.connect('veritabani.db') #Bağlantı aç ve database yarat.


df.to_sql('bilgisayar', conn, if_exists='replace', index=False) # Verileri Tabloya yaz

conn.close()