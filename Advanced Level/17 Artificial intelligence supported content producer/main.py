import openai

def generate_content(prompt):
    openai.api_key = "YOUR_OPENAI_API_KEY"  # Kendi OpenAI API anahtarınızı buraya ekleyin

    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=200,
            temperature=0.7,
            n=1,
            stop=None
        )
        content = response.choices[0].text.strip()
        return content
    except Exception as e:
        return f"Hata oluştu: {e}"

def main():
    print("Yapay Zeka Destekli İçerik Üretici")
    while True:
        prompt = input("\nİçerik üretmek istediğiniz konuyu yazınız (Çıkmak için 'exit' yazın): ")
        if prompt.lower() == "exit":
            print("Program sonlandırılıyor.")
            break
        result = generate_content(prompt)
        print("\n--- Üretilen İçerik ---")
        print(result)

if __name__ == "__main__":
    main()
