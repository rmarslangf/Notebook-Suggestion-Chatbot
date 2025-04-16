import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Veri setini oku
df = pd.read_csv('tamveriseti.csv')


df = df[~df['Marka'].str.startswith(('CR', 'Cr'), na=False)] #CR ve Cr ile başlayan markaları filtrele (bir BUG)

# 1. Ağırlık - Bilgisayar Sayısı histogramı
plt.figure(figsize=(10, 6)) #Bar Büyüklüğü
sns.histplot(data=df, x='Agirlik', bins=20) #histogramı ağırlık ve hücre sayısına oranla oluştur.
plt.title('Ağırlık Dağılımı') # Tablo Adı
plt.xlabel('Ağırlık') # x ekseninin adı
plt.ylabel('Bilgisayar Sayısı') # y ekseninin adı
plt.savefig('agirlik_histogram.png') #bu dosyaya kaydet
plt.close()

# 2. Fiyat - Bilgisayar Sayısı histogramı
plt.figure(figsize=(15, 8))
bins = np.arange(0, 400, 25)  # 25 bin TL aralıklarla 400.000 TL de sonlanacak şekilde yap.
sns.histplot(data=df, x='Fiyat', bins=bins)
plt.title('Fiyat Dağılımı')
plt.xlabel('Fiyat (Bin TL)')
plt.ylabel('Bilgisayar Sayısı')
plt.xticks(bins, [f'{int(x)}K' for x in bins], rotation=45) #X eksenindeki verileri isimlendir (K ile bitir.)
plt.tight_layout() #otomatik aralıklar yarat.
plt.savefig('fiyat_histogram.png')
plt.close()

# 3. Marka - Bilgisayar Sayısı (Top 25)
plt.figure(figsize=(15, 8))
marka_sayisi = df['Marka'].value_counts().head(25)  #CSV'deki ilk 25 markayı kullan. Çok fazla olduğu için grafik çakışmakta.
sns.barplot(x=marka_sayisi.index, y=marka_sayisi.values) # Şu değerleri kullan.
plt.title('En Çok Bilgisayar Satışı Yapan İlk 25 Marka')
plt.xlabel('Marka')
plt.ylabel('Bilgisayar Sayısı')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('marka_sayisi.png')
plt.close()

# 4. Marka başına ortalama fiyat (Top 25)
plt.figure(figsize=(15, 8))
marka_fiyat = df.groupby('Marka')['Fiyat'].mean().sort_values(ascending=False).head(25)
sns.barplot(x=marka_fiyat.index, y=marka_fiyat.values)
plt.title('En Pahalı İlk 25 Marka (Ortalama Fiyat)')
plt.xlabel('Marka')
plt.ylabel('Ortalama Fiyat (Bin TL)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('marka_ortalama_fiyat.png')
plt.close()

# 5. Ekran Kartı Tipi ve Ekran Kartı pasta grafiği
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1) #İki pasta grafiğinden 1. si 
ekran_karti_tipi = df['Ekran_Karti_Tipi'].value_counts() #Ekran_Karti_Tipi verisini kullan
plt.pie(ekran_karti_tipi.values, labels=ekran_karti_tipi.index, autopct='%1.1f%%') #Pasta grafiğini kullan: Parametreler Sırasıyla: Ekran_Karti_Tipi dataFrame'indeki verilerin hacmiyle büyüklüğünü yaz, Dilimlerin etiketleri, Dilimde yüzdelik oranı yazdır.
plt.title('Ekran Kartı Tipi Dağılımı')

plt.subplot(1, 2, 2) # İki pasta grafiğinden 2. si.
ekran_karti = df['Ekran_Kart'].value_counts()
plt.pie(ekran_karti.values, labels=ekran_karti.index, autopct='%1.1f%%')
plt.title('Ekran Kartı Dağılımı')
plt.tight_layout()
plt.savefig('ekran_karti_dagilimi.png')
plt.close()