import argparse
import pandas as pd
from nlp import prompt_to_filters
from filterMotor import filter_products
import sys
import io
import random
#========================(Unicode uygula)========================================================
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
#========================(Talep edilen flag'ler)========================================================
def main():
    parser = argparse.ArgumentParser(description="Laptop suggestion engine")
    parser.add_argument("--csv", type=str, default="latent_vektorlu_laptoplar.csv", help="CSV path")
    parser.add_argument("--prompt", type=str, required=True, help="Prompt text")
    args = parser.parse_args()

    try:
        df = pd.read_csv(args.csv)
    except Exception as e:
        print(f"CSV could not be loaded: {e}")
        return
#========================(CSV'yi kullan)========================================================
    df = pd.read_csv("latent_vektorlu_laptoplar.csv")  
    filters = prompt_to_filters(args.prompt, df)
    if filters.get("greeting"):
        print("🤖 Selam dostum! Sana nasıl yardımcı olabilirim? Kullanım ihtiyacını yaz yeter 😎") #Selam denirse selam ver
        return

    result = filter_products(df, filters)
#========================(Cevap dönmez ise bunu yaz)========================================================
    if result.empty:
        print("No matching products found.")
        return

#========================(Herzaman gösterilecke sütunlar)========================================================
    base_cols = ["Urun_Ad", "Fiyat"]
    prompt_cols = filters.get("fields", [])
    show_cols = list(dict.fromkeys(base_cols + prompt_cols))  # Tekrarları temizle

#========================(Tablonun Gösterimi)========================================================
    header = " | ".join([col.ljust(20) for col in show_cols])
    print("\n" + header)
    print("-" * len(header))

#========================(Filtreye uyanlardan rastgele 5 ürünü çıkar ve ayrım yap)========================================================
    selected = result.sample(n=min(5, len(result)), random_state=random.randint(1, 9999))
    for _, row in selected.iterrows():
        row_data = [str(row.get(col, "N/A")).ljust(20) for col in show_cols]
        print(" | ".join(row_data))

    print("\nUrun Linkleri:")
#========================(5 Ürünün sütunlarını çıkar)========================================================
    for _, row in selected.iterrows():
        ad = row.get("Urun_Ad", "Bilinmeyen Ürün")
        url = row.get("Urun_URL", "No URL")
        print(f"{ad}: {url}")



if __name__ == "__main__":
    main()
