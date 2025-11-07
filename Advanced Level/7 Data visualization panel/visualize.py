import matplotlib.pyplot as plt
import pandas as pd

def create_sample_data():
    data = {
        'Ay': ['Ocak', 'Şubat', 'Mart', 'Nisan', 'Mayıs', 'Haziran'],
        'Satış': [250, 300, 280, 350, 400, 420],
        'Maliyet': [150, 200, 180, 220, 250, 300]
    }
    df = pd.DataFrame(data)
    return df

def plot_data(df):
    plt.figure(figsize=(10,6))
    plt.plot(df['Ay'], df['Satış'], marker='o', label='Satış')
    plt.plot(df['Ay'], df['Maliyet'], marker='o', label='Maliyet')
    plt.title('Aylık Satış ve Maliyet Grafiği')
    plt.xlabel('Ay')
    plt.ylabel('Miktar')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def main():
    df = create_sample_data()
    plot_data(df)

if __name__ == "__main__":
    main()
