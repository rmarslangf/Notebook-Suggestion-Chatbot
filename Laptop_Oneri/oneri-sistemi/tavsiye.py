import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from nlp import prompt_to_filters
from filterMotor import filter_products

  #========================(Temel Öneri Fonksiyonu)========================================================
def recommend_laptops(prompt: str, df_with_latents: pd.DataFrame, latent_start_col: int, top_n: int = 5):
    filters = prompt_to_filters(prompt)
    filtered_df = filter_products(df_with_latents, filters)

    if filtered_df.empty:
        return "❌ Üzgünüm, filtrelere uyan ürün bulunamadı."

   #========================(Latent vektörü çağır)========================================================
    filtered_latents = filtered_df.iloc[:, latent_start_col:].values

   #========================(Kullanıcının Latent Vektör'de temsili)========================================================
    query_vector = filtered_latents.mean(axis=0).reshape(1, -1)

    #========================(Kelimelerin benzerlikteki teemsili)========================================================
    similarities = cosine_similarity(query_vector, filtered_latents)[0]
    top_indices = similarities.argsort()[-top_n:][::-1]

    top_matches = filtered_df.iloc[top_indices].copy()

    #========================(Sıralama istendiyse tekrar uyarla)========================================================
    sort_col = filters.get("sort_by")
    ascending = filters.get("ascending", True)

    #========================(Eşlenenleri hazırla ve nulleri yoket.)========================================================
    if sort_col and sort_col in top_matches.columns:
        try:
            top_matches[sort_col] = pd.to_numeric(top_matches[sort_col], errors='coerce')
            top_matches = top_matches[top_matches[sort_col].notna()]
            top_matches = top_matches.sort_values(by=sort_col, ascending=ascending)
        except Exception as e:
            print(f"⚠️ Top sonuçlarda sıralama hatası: {e}")

    return top_matches


