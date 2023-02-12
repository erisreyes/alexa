from gtts import gTTS
import os
import pygame

# Take input for the text to be converted to speech
text = input("Enter the text you want to be converted to speech: ")

# Use gTTS to convert the text to speech
tts = gTTS(text=text, lang='en')

# Save the speech to a file
# tts.save("output.mp3")
tts.save("custom_output.mp3")


# Play the speech file
# os.system("start output.mp3")

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("output.mp3")
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)

