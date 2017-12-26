# pip install pyaudio  & pip install SpeechRecognition
import speech_recognition
r = speech_recognition.Recognizer()

#Record sound by Microphone
with speech_recognition.Microphone() as source:
    print("請說話！")
    audio = r.listen(source)

#convert audio data to wav
with open("microphone-results.wav", "wb") as f:
    f.write(audio.get_wav_data())

#convert wav to audio data
with speech_recognition.WavFile("microphone-results.wav") as source:
    audio = r.record(source)

print(r.recognize_google(audio, language='zh-TW'))
