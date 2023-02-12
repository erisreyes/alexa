import random
from gtts import gTTS
import pygame


# List of greetings
greetings = ["Hello!", "Hi there!", "Hi!", "Hey!", "What's up?"]

# List of responses
responses = ["I'm doing great, thank you!", "Just living the dream!", "I'm here to help you!", "I'm all good, how are you?", "I'm fabulous!"]

# List of farewells
farewells = ["Goodbye!", "See you later!", "Have a great day!", "Take care!", "Talk to you soon!"]

# Continuously prompt the user for input
while True:
    user_input = input("You: ")
    
    # If the user says hello, respond with a greeting
    if "hello" in user_input.lower():

        print("Alexa: " + random.choice(greetings))

        text = random.choice(greetings)
        print(text)

        # Use gTTS to convert the text to speech
        tts = gTTS(text=text, lang='en')

        # Save the speech to a file
        tts.save("output.mp3")

        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load("output.mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
    
    # If the user asks how Alexa is doing, respond with a response
    elif "how are you" in user_input.lower():
        print("Alexa: " + random.choice(responses))
    
    # If the user says goodbye, respond with a farewell and exit the program
    elif "goodbye" in user_input.lower():
        print("Alexa: " + random.choice(farewells))
        break
    
    # If the user says something else, respond with a default message
    else:
        print("Alexa: Sorry, I don't understand what you're saying.")

