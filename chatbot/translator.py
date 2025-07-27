from deep_translator import GoogleTranslator

def translate_text(text, src='auto', dest='en'):
    return GoogleTranslator(source=src, target=dest).translate(text)

