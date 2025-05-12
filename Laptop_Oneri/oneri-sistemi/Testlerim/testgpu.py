import pandas as pd

# CSV dosyasını oku
df = pd.read_csv("./latent_vektorlu_laptoplar.csv")

# 🎮 Ekran kartı hafızası: "6 GB", "4GB" → sayıya çevir
df['Ekran_Karti_Hafizasi'] = (
    df['Ekran_Karti_Hafizasi']
    .astype(str)
    .str.replace("gb", "", case=False, regex=True)
    .str.replace("[^0-9.]", "", regex=True)
)

# Sayıya çevir
df['Ekran_Karti_Hafizasi'] = pd.to_numeric(df['Ekran_Karti_Hafizasi'], errors='coerce')

# NaN'leri at ve azalan sırada sırala
df_sorted = df.dropna(subset=['Ekran_Karti_Hafizasi']).sort_values(by='Ekran_Karti_Hafizasi', ascending=False)

# Sonuçları göster
print(df_sorted[['Ekran_Karti_Hafizasi', 'Fiyat', 'Ekran_Kart']].head(20))  # Ekstra bilgiyle birlikte
