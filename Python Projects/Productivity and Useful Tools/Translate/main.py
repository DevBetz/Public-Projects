#pip install googletrans==4.0.0-rc1
from googletrans import Translator

def translate_to_english():
    translator = Translator()
    
    # Ask the user for the text they want to translate
    text_to_translate = input("What text would you like to translate into English? ")
    
    # Detect the language of the input text
    detected_language = translator.detect(text_to_translate).lang
    
    # Print the detected language
    print(f"Detected language: {detected_language}")
    
    # Translate the text to English
    translation = translator.translate(text_to_translate, src=detected_language, dest='en')
    
    # Print the translated text
    print(f"Translated text: {translation.text}")

# Run the translation function
translate_to_english()
