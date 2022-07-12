from typing import Dict


# Language Translator Base class
class LanguageTranslator:
    """
    Specify the source and destination language while instantiation and
    the tool translates the text to desired language
    """
    def __init__(self, source: str, destination: str):
        self.source = source
        self.destination = destination
        self.translations: Dict[str, str] = None

    def translate(self, text: str):
        return str(self.translations[text])


