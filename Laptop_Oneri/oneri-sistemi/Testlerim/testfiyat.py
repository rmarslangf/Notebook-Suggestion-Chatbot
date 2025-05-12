import pandas as pd

# 📥 CSV'yi oku
df = pd.read_csv("./latent_vektorlu_laptoplar.csv")

# 💰 Fiyatları sayıya çevir (virgül vs. varsa 'coerce' ile NaN'a çevir)
df['Fiyat'] = pd.to_numeric(df['Fiyat'], errors='coerce')

# 🧹 NaN fiyatları at, artan şekilde sırala
df_sorted = df.dropna(subset=['Fiyat']).sort_values(by='Fiyat', ascending=False)

# 🖨️ İlk 20 sonucu yazdır (dilersen arttırabilirsin)
print(df_sorted[['Fiyat']].head(20))