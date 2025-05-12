import pandas as pd
import re
from nlp import prompt_to_filters as generate_filters

#========================(RAM'deki Gereksiz Kelimeleri yoket ayrıca Değerlerini tek bir değer olarak hesapla)========================================================
def parse_ram(ram_str):
    ram_str = str(ram_str).lower()
    if 'mb' in ram_str:
        match = re.search(r'(\d+)', ram_str)
        return float(match.group(1)) / 1024 if match else None
    elif 'gb' in ram_str:
        match = re.search(r'(\d+)', ram_str)
        return float(match.group(1)) if match else None
    return None
#========================(Pil Gücü'deki Gereksiz Kelimeleri yoket ayrıca Değerlerini tek bir değer olarak hesapla)========================================================
def parse_battery_power(power_str):
    if not isinstance(power_str, str):
        return None
    power_str = power_str.lower().replace(",", ".")
    match = re.search(r'(\d+(\.\d+)?)', power_str)
    return float(match.group(1)) if match else None
#========================(SSD'dedki Gereksiz Kelimeleri yoket ayrıca Değerlerini tek bir değer olarak hesapla)========================================================
def parse_ssd_size(ssd_str):
    if not isinstance(ssd_str, str):
        return None
    ssd_str = ssd_str.lower()
    match = re.search(r'(\d+(?:\.\d+)?)\s*(tb|gb)', ssd_str)
    if match:
        size = float(match.group(1))
        unit = match.group(2)
        return size * 1024 if unit == 'tb' else size
    return None
#========================(VRAM'deki Gereksiz Kelimeleri yoket ayrıca Değerlerini tek bir değer olarak hesapla)========================================================
def parse_vram(vram_str):
    if not isinstance(vram_str, str):
        return None
    vram_str = vram_str.lower().replace(",", ".")
    match = re.search(r'(\d+(\.\d+)?)(\s*)?g?b?', vram_str)
    return float(match.group(1)) if match else None
#========================(Ekran Boyutu'ndaki Gereksiz Kelimeleri yoket ayrıca Değerlerini tek bir değer olarak hesapla)========================================================
def parse_screen_size(size_str):
    if not isinstance(size_str, str):
        return None
    size_str = size_str.lower().replace(",", ".")
    match = re.search(r'(\d+(\.\d+)?)', size_str)
    return float(match.group(1)) if match else None
#========================(İşlemci tipini algıla ayrıca bir işlemci hiyerarşisi yapma)========================================================
def get_processor_type(processor_string):
    if not isinstance(processor_string, str):
        return 'Unknown'
    processor_string = processor_string.lower()
    hierarchy = ['ryzen 9', 'ryzen 7', 'ryzen 5', 'ryzen 3', 'core i9', 'core i7', 'core i5', 'core i3']
    for item in hierarchy:
        if item in processor_string:
            return item.title() if "ryzen" in item else item.split()[-1]
    return 'Unknown'

def filter_products(df: pd.DataFrame, filters: dict) -> pd.DataFrame:
    filtered_df = df.copy()
    print("Aktif filtreler:", filters)

#========================(Fiyat Filtresi ve sıralamada kullanımı)========================================================
    if 'max_price' in filters or 'min_price' in filters:
        filtered_df['Fiyat'] = filtered_df['Fiyat'].astype(str).str.replace(r'[^\d]', '', regex=True) # gereksiz harf rakam değerlerini yoket
        filtered_df['Fiyat'] = pd.to_numeric(filtered_df['Fiyat'], errors='coerce')

    if 'max_price' in filters:
        filtered_df = filtered_df[filtered_df['Fiyat'] <= filters['max_price']]

    if 'min_price' in filters:
        filtered_df = filtered_df[filtered_df['Fiyat'] >= filters['min_price']]

#========================(Marka Filtresi)========================================================
    if 'brand' in filters:
        filtered_df = filtered_df[filtered_df['Marka'].str.lower() == filters['brand'].lower()] #Markayı Küçült (harf karışıklığı olmasın)

#========================(Ram Filtresi ve sıralamada kullanımı)========================================================
    if 'exact_ram' in filters: # Ram kesin olarak belirtilmişse devreye girer
        filtered_df['RAM'] = filtered_df['RAM'].apply(parse_ram)
        filtered_df = filtered_df[filtered_df['RAM'] == filters['exact_ram']]
    elif 'min_ram' in filters:
        filtered_df['RAM'] = filtered_df['RAM'].apply(parse_ram)
        filtered_df = filtered_df[filtered_df['RAM'] >= filters['min_ram']]
        filtered_df = filtered_df.sort_values(by='RAM', ascending=False)

 #========================(İşlemci Filtresi ve hiyerarşi ayarlamaları)========================================================
    if filters.get('cpu') or filters.get('prefer_cpu'):
        prefer_processors = filters.get('prefer_cpu', [])
        if prefer_processors:
            filtered_df = filtered_df[
                filtered_df['Islemci_Turu'].apply(lambda x: isinstance(x, str) and any(cpu.lower() in x.lower() for cpu in prefer_processors))
            ]
            filtered_df['Processor_Type'] = filtered_df['Islemci_Turu'].apply(get_processor_type)
            filtered_df['Processor_Type'] = pd.Categorical(
                filtered_df['Processor_Type'],
                categories=prefer_processors,
                ordered=True
            )
            filtered_df = filtered_df.sort_values(by='Processor_Type', ascending=True)
        else:
            processor_priority = ['i9', 'Ryzen 9', 'i7', 'Ryzen 7', 'i5', 'Ryzen 5', 'i3', 'Ryzen 3']
            filtered_df['Processor_Type'] = filtered_df['Islemci_Turu'].apply(get_processor_type)
            filtered_df = filtered_df[filtered_df['Processor_Type'] != 'Unknown']
            filtered_df['Processor_Type'] = pd.Categorical(
                filtered_df['Processor_Type'],
                categories=processor_priority,
                ordered=True
            )
            filtered_df = filtered_df.sort_values(by='Processor_Type', ascending=False)

  #========================(VRAM Filtresi ve hiyerarşi ayarlamaları)========================================================
    if filters.get("gpu"):
        filtered_df['VRAM'] = filtered_df['Ekran_Karti_Hafizasi'].apply(parse_vram)
        filtered_df = filtered_df[filtered_df['VRAM'].notna()]
        filters['sort_by'] = 'VRAM'
        filters['ascending'] = False
        print("\n🎮 GPU siralaması (VRAM):")
        print(filtered_df[['Urun_Ad', 'Ekran_Karti_Modeli', 'Ekran_Karti_Hafizasi', 'VRAM']].sort_values(by='VRAM', ascending=False).head(5))

  #========================(SSD Filtresi ve Sıralanması)========================================================
    sort_by = filters.get('sort_by')
    ascending = filters.get('ascending', False)
    if sort_by == 'SSD':
        filtered_df['SSD'] = filtered_df['SSD'].apply(parse_ssd_size)
    elif sort_by == 'Ekran_Boyutu':
        filtered_df[sort_by] = filtered_df[sort_by].apply(parse_screen_size)
    elif sort_by == 'Pil_Gucu':
        filtered_df['Pil_Gucu'] = filtered_df['Pil_Gucu'].apply(parse_battery_power)

  #========================(Özel durumu olmayan değerlerdde sıralama)========================================================
    if sort_by and sort_by in filtered_df.columns:
        print(f"\n Siralama uygulaniyor: {sort_by} ({'artan' if ascending else 'azalan'})")
        try:
            filtered_df[sort_by] = pd.to_numeric(filtered_df[sort_by], errors='coerce')
            filtered_df = filtered_df[filtered_df[sort_by].notna()]
            filtered_df = filtered_df.sort_values(by=sort_by, ascending=ascending)
        except Exception as e:
            print(f" Siralama hatasi: {e}")
    else:
        print(" Siralama yapılmadı.")
#***************************************************************************************************************************
    return filtered_df