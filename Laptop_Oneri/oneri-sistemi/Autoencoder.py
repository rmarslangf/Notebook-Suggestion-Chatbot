import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder
from tensorflow.keras.models import Model  # type: ignore
from tensorflow.keras.layers import Input, Dense  # type: ignore
from tensorflow.keras.optimizers import Adam  # type: ignore
import matplotlib.pyplot as plt

  #========================(CSV'yi oku)========================================================
DATA_PATH = "./oneri-sistemi/tamveriseti.csv"
raw_df = pd.read_csv(DATA_PATH)

  #========================(Primary Column'ları elemeye sokma (tam dolu))========================================================
to_drop = ['Urun_Ad', 'Seri', 'Urun_URL']
df = raw_df.drop(columns=to_drop, errors='ignore')

#========================(Fiyat değerlerini numeric yapmak için işlemler)========================================================

if 'Fiyat' in df.columns:
    df['Fiyat'] = (
        df['Fiyat']
        .astype(str)
        .str.replace('.', '', regex=False)
        .str.replace(',', '.', regex=False)
    )
    df['Fiyat'] = pd.to_numeric(df['Fiyat'], errors='coerce')
#========================(Ağırlık değerlerini numeric yapmak için işlemler)========================================================

if 'Agirlik' in df.columns:
    df['Agirlik'] = pd.to_numeric(df['Agirlik'], errors='coerce')

#========================(En çok araştırılan column'ları elemeye hazırla)========================================================
important_cols = ['Marka', 'SSD', 'Ekran_Karti_Hafizasi', 'RAM',
                  'Ekran_Boyutu', 'Isletim_Sistemi', 'Agirlik', 'Ekran_Karti_Modeli']
df = df.dropna(subset=important_cols, axis=0) #nulleri sil

#========================(Stringleri (object) kategorik, sayısal değerleri numeric tutalım)========================================================
categorical_cols = df.select_dtypes(include='object').columns.tolist()
numeric_cols = df.select_dtypes(include='number').columns.tolist()

#========================(One Hot Encoder'ın Kategörik (Sözel) veriler için çağrılması)========================================================
encoder = OneHotEncoder(sparse_output=False, handle_unknown='ignore')
encoded = encoder.fit_transform(df[categorical_cols])
#========================(MinMax'ın Numerik veriler için çağrılması)========================================================
scaler = MinMaxScaler()
scaled = scaler.fit_transform(df[numeric_cols])

#========================(CSV Formatı için tüm verileri birleştir)========================================================
X = np.concatenate([encoded, scaled], axis=1)

#========================(Null değer ne olursa olsun 0.0 dönsün)========================================================
X = np.nan_to_num(X, nan=0.0, posinf=0.0, neginf=0.0)

#========================(Train Test verilerini ayır)========================================================
X_train, X_test = train_test_split(X, test_size=0.2, random_state=42)

#========================(Auto Encoder'ı ayarla)========================================================
input_dim = X.shape[1] 
input_layer = Input(shape=(input_dim,)) #Feature Tanımı 
encoded = Dense(64, activation='relu')(input_layer) #64 Nöron relu modeli ile Giriş katmanı
encoded = Dense(32, activation='relu')(encoded) #32 nöron ara katman relu modeli
decoded = Dense(64, activation='relu')(encoded) #64 nöron ara katman relu modeli
output_layer = Dense(input_dim, activation='sigmoid')(decoded) #Sigmoid kullan ve çıkış ver

autoencoder = Model(inputs=input_layer, outputs=output_layer) #Girdi ve Çıktı
autoencoder.compile(optimizer=Adam(1e-3), loss='mse') # Adam optimizerını kullan hiperparametre için en uygun değer ayrıca girildi ayrıca kayıpı göster

#========================(Model Eğitimini tamamla)========================================================
history = autoencoder.fit(
    X_train, X_train,
    epochs=50, # epoch sayısı
    batch_size=16, #Mini batch sayısı
    shuffle=True, #Verileri karıştır ki overfitting olmasın
    validation_data=(X_test, X_test) #Doğrula
)

#========================(Grafik Çiz)========================================================
plt.figure(figsize=(10, 5))
plt.plot(history.history['loss'], label='Train Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.title('Autoencoder Eğitim Süreci')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("autoencoder_loss_plot.png") 
plt.show()

#========================(Train Test verilerini ayır)========================================================
encoder_model = Model(inputs=input_layer, outputs=encoded)
latent_vectors = encoder_model.predict(X)

#========================(Latent vektörler ekle ve uygula)========================================================
latent_df = pd.DataFrame(latent_vectors, index=df.index)
final_df = pd.concat([raw_df.loc[df.index].reset_index(drop=True), latent_df.reset_index(drop=True)], axis=1)

#========================(Sonucu kaydet ve bitir)========================================================
final_df.to_csv("./oneri-sistemi/latent_vektorlu_laptoplar.csv", index=False)

print(f"✅ Eğitim tamamlandı. Sonuç dosyası: latent_vektorlu_laptoplar.csv")
print(f"📊 Eğitim grafiği: autoencoder_loss_plot.png")
