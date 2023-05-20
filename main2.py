import pyttsx3
import speech_recognition as sr

def dinle():
    r = sr.Recognizer()
    engine = pyttsx3.init()
    engine.setProperty("rate", 150)  # Konuşma hızı (varsayılan: 200)
    engine.setProperty("volume", 1.0)  # Konuşma ses düzeyi (varsayılan: 1.0)

    with sr.Microphone() as source:
        print("Dinliyorum...")
        audio = r.listen(source)
        
    try:
        metin = r.recognize_google(audio, language="tr-TR")
        print("Söylediğiniz: " + metin)
    except sr.UnknownValueError:
        print("Anlaşılamadı")
    except sr.RequestError as e:
        print("Sistem hatası: {0}".format(e))
    
    engine.say(metin)
    engine.runAndWait()

dinle()