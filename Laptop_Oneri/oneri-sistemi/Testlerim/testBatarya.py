import pandas as pd

# 📥 CSV'yi oku
df = pd.read_csv("latent_vektorlu_laptoplar.csv")

# 🔋 Pil_Gucu'ndan "Wh", boşluk vs. temizle → sadece sayısal değer kalsın
df['Pil_Gucu'] = (
    df['Pil_Gucu']
    .astype(str)
    .str.replace(",", ".")  # virgüllü ondalıkları noktaya çevir
    .str.extract(r"(\d+\.?\d*)")  # yalnızca sayı kısmını al
    .astype(float)
)

# 🧹 NaN'leri at
df = df.dropna(subset=['Pil_Gucu'])

# 🔽 Azalan sıraya göre sırala
df_sorted = df.sort_values(by='Pil_Gucu', ascending=False)

# 🖨️ En yüksek batarya gücüne sahip 20 cihazı göster
print(df_sorted[['Pil_Gucu', 'Fiyat', 'Agirlik']].Head(20))  # İsteğe bağlı ekstra kolonlar