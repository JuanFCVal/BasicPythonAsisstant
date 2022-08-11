# Python program to translate
# speech to text and text to speech
 
 
import speech_recognition as sr
import pyttsx3
import json
import random
 
# Initialize the recognizer
r = sr.Recognizer()
engine = pyttsx3.init()
# Function to convert text to
# Opening JSON file with utf8
f = open('answers.json', 'r', encoding='utf8')  
# returns JSON object as 
# a dictionary
data = json.load(f)
# speech
def SpeakText(command):
     
    # Initialize the engine
    engine.say(command)
    engine.runAndWait()
     
def getResponse(inputText):
    for element in data: #Recorre todo el .json
        if(element != "error"):  #Recorre todos los elementos menos el de error que tiene otra estructura
            for keyword in data[element]['keywords']: #Extrae las keywords de cada elemento
                tokenWords = inputText.split(" ") #Separa las palabras del input
                for token in tokenWords: #Recorre las palabras del input con las keywords de cada elemento
                    if(keyword == token): #Si encuentra una keyword en el input, entonces se busca las respuestas del elemento
                        arrayRespuestas = data[element]['respuestas'] #Obtiene las respuestas y almacena en un arreglo
                        answer = random.choice(tuple(arrayRespuestas)) #Selecciona aleatoriamente una de las respuestas
                        return(answer)
    errorAnswer = random.choice(tuple(data['error'])) 
    return(errorAnswer)
     
# Loop infinitely for user to
# speak
 
while(1):   
     
    # Exception handling to handle
    # exceptions at the runtime
    try:
         
        # use the microphone as source for input.
        with sr.Microphone() as source2:
        # filename = "recording.wav"
        # with sr.AudioFile(filename) as source2:
            # wait for a second to let the recognizer
            # adjust the energy threshold based on
            # the surrounding noise level
            r.adjust_for_ambient_noise(source2, duration=0.2)
             
            #listens for the user's input
            audio2 = r.listen(source2)
            # Using google to recognize audio
            MyText = r.recognize_google(audio2, language='es-ES' )
            MyText = MyText.lower()
            print("Did you say "+MyText)
            # SpeakText(MyText)
            SpeakText(getResponse(MyText))
             
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
         
    except sr.UnknownValueError:
        print("unknown error occured")
# import speech_recognition as sr
# filename = "recording.wav"
# r = sr.Recognizer()
# #method to get the audio from the microphone
# def getAudio():
#     with sr.Microphone() as source:
#         print("Say something!")
#         audio = r.listen(source)
#         print("Done!")
#     return audio

# def getTextFromAudio():
#     with sr.AudioFile(filename) as source:
#         print("Triying to obtain audio from source")
#         # listen for the data (load audio to memory)
#         audio_data = r.record(source)
#         # recognize (convert from speech to text)
#         text = r.recognize_google(audio_data)
#         print(text)
        
# getTextFromAudio()