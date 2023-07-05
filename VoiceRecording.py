import speech_recognition as sr


def convert_speech_to_text():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Konuşmayı başlatın:")
        audio = recognizer.listen(source)

    try:
        print("Metin dökümü:")
        text = recognizer.recognize_google(audio, language="en-US")
        print(text)

        # Metni bir dosyaya yazmak için:
        with open("metin_dokumu.txt", "w") as file:
            file.write(text)

    except sr.UnknownValueError:
        print("Anlaşılamadı")
    except sr.RequestError as e:
        print("Hata: {0}".format(e))


convert_speech_to_text()
