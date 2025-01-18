delete = """
import os
os.system("cls")
"""



import tempfile
import time
from gtts import gTTS
import pygame

exec(delete) # for ignore Pygame's patch

def generate_speech(Pathfile , lan):
        
    with open(Pathfile , "r" , encoding="utf-8") as READ:

        phrases = [READ.read()]

    for line in phrases:
            speech = gTTS(text=line, lang=lan) # to generate the speech (any language)

            with tempfile.NamedTemporaryFile(suffix = ".mp3", delete=False) as audio: 
                speech.write_to_fp(audio)  # write the data in the file
                audio_file_path = audio.name  # store the path


            exec(delete)

            print("listen")
            pygame.mixer.init()  # initialize pygame mixer
            pygame.mixer.music.load(audio_file_path) # load the the temporary file
            pygame.mixer.music.play() # play the sound
        
            
            while pygame.mixer.music.get_busy():
                time.sleep(0.1) # keeping the code running while speaking time


            audio.close() # clean up the temporary file after finishing




def asking_for_data():
        print("enter the name of the file (in English please , and with the extension) : ")
        file_name = input("--> ")

        print("Enter the partition")
        partition = input("--> ")

        print("Enter the path")
        path = input("--> ")

        print("Enter the type of language (ar or en) : ")
        lang = input("--> ")
            
        if path[0] == '\\':
            path = path[1:]

        final_path = rf"{partition}:\{path}\{file_name}"

        generate_speech(final_path , lang)



asking_for_data()