import pandas as pd
from datetime import datetime

def create_sample_data():
    data = {
        'Ürün': ['Kalem', 'Defter', 'Silgi', 'Cetvel'],
        'Satış Adedi': [150, 120, 100, 80],
        'Birim Fiyat': [1.5, 2.0, 0.5, 1.0]
    }
    df = pd.DataFrame(data)
    df['Toplam'] = df['Satış Adedi'] * df['Birim Fiyat']
    return df

def generate_excel_report(df, filename):
    with pd.ExcelWriter(filename, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='Satış Raporu')
        # Özet sayfası
        summary = pd.DataFrame({
            'Toplam Satış': [df['Toplam'].sum()],
            'Toplam Ürün': [df['Satış Adedi'].sum()]
        })
        summary.to_excel(writer, index=False, sheet_name='Özet')

def main():
    df = create_sample_data()
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f'sales_report_{now}.xlsx'
    generate_excel_report(df, filename)
    print(f"Rapor başarıyla oluşturuldu: {filename}")

if __name__ == "__main__":
    main()
