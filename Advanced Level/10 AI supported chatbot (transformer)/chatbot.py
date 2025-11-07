from transformers import pipeline

def main():
    print("Yapay Zekâ Destekli Chatbot'a Hoşgeldiniz! (Çıkmak için 'exit' yazınız)")
    chatbot = pipeline("conversational", model="microsoft/DialoGPT-small")

    while True:
        user_input = input("Siz: ")
        if user_input.lower() == "exit":
            print("Görüşmek üzere!")
            break

        response = chatbot(user_input)
        print("Bot:", response[0]['generated_text'])

if __name__ == "__main__":
    main()
