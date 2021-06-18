# python speech recognisition
import speech_recognition as sr
import webbrowser as wb

a1 = sr.Recognizer()
a2 = sr.Recognizer()
a3 = sr.Recognizer()

with sr.Microphone() as source:
    print('[search google: search youtube]')
    print('speak now')
    audio = a3.listen(source)
    
if google in a2.recognise_google(audio):
    a2 = sr.Recogniser()
    url ="https://www.google.co.in/ "
with sr.Microphone() as source:
     print('search your query')
     audio = a2.listen(source)
    
     try:
         get = a2.Recognise_google(audio)
         wb.get().open_new(url+get)
     except sr.unknownvalueError:
         print("error")
     except sr.RequestError as e:
         print('failed',format(e))
