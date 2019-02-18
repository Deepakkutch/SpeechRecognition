import speech_recognition as sr
import moviepy.editor as mp
clip = mp.VideoFileClip("kid.mp4").subclip(0,30)
clip.audio.write_audiofile("theaudio.wav")
r = sr.Recognizer()
audio ='theaudio.wav'
with sr.AudioFile(audio) as source:
    print('Speak anything:')
    audio = r.record(source)
    print('Done')
try:
       text = r.recognize_google(audio)
       text_file = open("Output.txt", "w")
       text_file.write(text)
       text_file.close()
except Exception as e:
        print(e)
