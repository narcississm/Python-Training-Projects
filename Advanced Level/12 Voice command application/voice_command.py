import speech_recognition as sr
import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Komutunuzu bekliyorum...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio, language='tr-TR')
        print(f"Algılanan komut: {command}")
        return command.lower()
    except sr.UnknownValueError:
        print("Anlaşılamadı, lütfen tekrar edin.")
        speak("Anlaşılamadı, lütfen tekrar edin.")
        return None
    except sr.RequestError:
        print("Ses tanıma servisine ulaşılamıyor.")
        speak("Ses tanıma servisine ulaşılamıyor.")
        return None

def main():
    speak("Sesli komut uygulamasına hoş geldiniz.")
    while True:
        command = listen_command()
        if command:
            if "çıkış" in command or "kapat" in command:
                speak("Uygulamadan çıkılıyor, görüşmek üzere!")
                break
            elif "merhaba" in command:
                speak("Merhaba! Size nasıl yardımcı olabilirim?")
            else:
                speak(f"Komutunuz: {command} olarak algılandı.")

if __name__ == "__main__":
    main()
