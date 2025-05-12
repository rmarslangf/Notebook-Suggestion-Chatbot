import pandas as pd

# CSV'yi oku
df = pd.read_csv("./latent_vektorlu_laptoplar.csv")

# NaN'li Agirlikları at
df = df[df["Agirlik"].notna()]

# Agirlik'ı float'a çevir
df["Agirlik"] = df["Agirlik"].astype(float)

# Agirlik'a göre azalan sırala
sorted_df = df.sort_values(by="Agirlik", ascending=False)

# Urun_Ad ve Agirlik birleşimi
sonuc_listesi = [f"{row['Urun_Ad']},{row['Agirlik']}" for _, row in sorted_df.iterrows()]

# Sonuçları yazdır
for item in sonuc_listesi:
    print(item)
