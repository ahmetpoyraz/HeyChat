import openai
import os
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import sys

openai.api_key = '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'  # OpenAI API anahtarınızı buraya girin

def send_chatgpt_api(soru):
    response = openai.Completion.create(
        engine='text-davinci-003',  # GPT-3.5 Türkçe modelini kullanmak için
        prompt=soru,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.7
    )
    return response.choices[0].text.strip()

# Ses algılama fonksiyonu
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # r.adjust_for_ambient_noise(source)
        print("Dinleniyor...")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio, language="tr-TR")  # Türkçe metni çevrimi yapar
        print(text)
        return text
    except sr.UnknownValueError:
        return ""
    except sr.RequestError:
        print("Ses hizmetine erişilemiyor.")

# komut algıladığında çalışacak kod bloğu
def dialog(metin):
    try:
        print("Apiye gidiyor:")
        cevap = send_chatgpt_api(metin)
        speak(cevap)
    except sr.UnknownValueError:
        speak("Anlaşılamadı")
    except sr.RequestError as e:
        speak("API hatası")
    

#sese çevirme fonksyionu
def speak(text):
    tts = gTTS(text, lang='tr')
    tts.save('chatspeak.mp3')
    playsound('chatspeak.mp3')
    os.remove('chatspeak.mp3')


# ana program döngüsü
while True:
    print("Program started...")
    text = listen()
    if text and "hey asistan" in text.lower():
        speak('selam, nasıl yardımcı olabilirim?')
        playsound('receivesound.mp3')
        text2 = listen()
        if text2 and "programı kapat" in text2.lower():
            speak('tamam, kapatıyorum')
            sys.exit()
        else:
            if not text2:
                speak('Anlayamadım tekrarlar mısın!')
                playsound('receivesound.mp3')
                text3 = listen()
                if not text3:
                    speak('Sessiz bir ortama geçtikten sonra bana Hey asistan! diye seslenebilirsin.')
                else:
                    dialog(text3)
            else:
                 dialog(text2)
    elif  text and "programı kapat" in text.lower():
         speak('tamam, kapatıyorum')
         sys.exit()
    
    
        