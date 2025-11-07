import requests

def get_weather(city):
    api_key = 'YOUR_OPENWEATHERMAP_API_KEY'  # Kendi API anahtarınızı buraya koyun
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=tr"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        desc = data['weather'][0]['description']
        print(f"{city} için hava durumu: {temp}°C, {desc}")
    else:
        print("Hava durumu alınamadı.")

def get_exchange_rate(base, target):
    url = f"https://api.exchangerate.host/latest?base={base}&symbols={target}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        rate = data['rates'][target]
        print(f"{base} → {target} Döviz kuru: {rate:.4f}")
    else:
        print("Döviz kuru alınamadı.")

def get_crypto_price(symbol):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={symbol}&vs_currencies=usd"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if symbol in data:
            price = data[symbol]['usd']
            print(f"{symbol.upper()} fiyatı: ${price}")
        else:
            print("Kripto para bulunamadı.")
    else:
        print("Kripto para fiyatı alınamadı.")

def main():
    print("API ile Takip Paneli")
    while True:
        print("\n1. Hava Durumu\n2. Döviz Kuru\n3. Kripto Para Fiyatı\n4. Çıkış")
        choice = input("Seçiminizi yapınız: ")
        if choice == '1':
            city = input("Şehir adı: ")
            get_weather(city)
        elif choice == '2':
            base = input("Temel para birimi (örnek: USD): ").upper()
            target = input("Hedef para birimi (örnek: EUR): ").upper()
            get_exchange_rate(base, target)
        elif choice == '3':
            symbol = input("Kripto para sembolü (örnek: bitcoin): ").lower()
            get_crypto_price(symbol)
        elif choice == '4':
            print("Program sonlandırılıyor.")
            break
        else:
            print("Geçersiz seçim, tekrar deneyiniz.")

if __name__ == "__main__":
    main()
