import pandas as pd
from nlp import prompt_to_filters, get_word_similarity

# Test sorguları
test_queries = [
    "Oyun oynamak için güçlü bir laptop istiyorum",
    "Ofis için hafif ve pil ömrü uzun bir laptop lazım",
    "Bu laptop çok pahalı, daha uygun bir şey var mı?",
    "Tasarım yapacağım, iyi bir ekran kartı olmalı",
    "Bütçem 15000 TL, bu fiyata ne alabilirim?",
    "Hafif ve güçlü bir laptop arıyorum"
]

# Test veri setini yükle
try:
    df = pd.read_csv("tamveriseti.csv")
except:
    print("Veri seti bulunamadı!")
    exit(1)

print("🤖 Laptop Öneri Sistemi Testi")
print("=" * 50)

for query in test_queries:
    print(f"\n📝 Sorgu: {query}")
    
    # Filtreleri uygula
    filters = prompt_to_filters(query, df)
    print("\n🔍 Uygulanan Filtreler:")
    for key, value in filters.items():
        print(f"  - {key}: {value}")
    
    print("-" * 50) 