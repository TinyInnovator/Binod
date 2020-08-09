# execute in cmd:
# pip install pywin32
# pip install pygame
# pip install gTTS
from win32com.client import Dispatch
import pygame
from gtts import gTTS

sp = Dispatch('SAPI.SpVoice')
# open file binod.txt
f = open('binod.txt')
# initialize pygame speaker
pygame.mixer.init()
# read content of file
binod = f.read()
# don't forget to close file
f.close()
# get audio from text
audio1 = gTTS(text=binod, lang='hi', slow=True) # hindi
audio2 = gTTS(text=binod, lang='ar', slow=False) # arabian
audio3 = gTTS(text=binod, lang='bn', slow=False) # bengali
audio4 = gTTS(text=binod, lang='en', slow=False) # english
audio5 = gTTS(text=binod, lang='ta', slow=False) # tamil
# save all...
audio1.save('binod0.mp3')
audio2.save('binod1.mp3')
audio3.save('binod2.mp3')
audio4.save('binod3.mp3')
audio5.save('binod4.mp3')
# run an infinite loop
# enjoy...:)
i = 1
while True:
    sp.Speak('Be node')
    pygame.mixer.music.load(f"binod{i}.mp3")
    i+=1
    i%=5
    pygame.mixer.music.play()
