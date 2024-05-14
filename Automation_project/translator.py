def create_translation_dict():
    translation_dict = {
        "hello": "hola",
        "goodbye": "adiós",
        "apple": "manzana",
        "woman": "mujer",
        "girl": "chica",
        "I": "yo",
        "he": "él",
        "eats": "come",
        "boy": "niño",
        "her": "su",
        "she": "ella",
        "one": "uno",
        "bread": "pan",
        "milk": "leche",
        "water": "agua",
        "the": "el",  # masculine
        "the_f": "la",  # feminine
        "I am": "soy",
        "is": "es",
        # Add more words and their translations here
    }
    return translation_dict

def translate_word(word, translation_dict):
    return translation_dict(word, "Translation not found")