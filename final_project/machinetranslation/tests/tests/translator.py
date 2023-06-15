'''Peer Review Assignment'''
from deep_translator import MyMemoryTranslator
def englishtofrench(englishtext):
    """
    This function returns the translation from english to french
     """
    frenchtext = MyMemoryTranslator(source='fr', target='french').translate(englishtext)
    return frenchtext

def frenchtoenglish(frenchtext):
    """
    This function returns the translation from french to english
     """
    englishtext = MyMemoryTranslator(source='en', target='english').translate(frenchtext)
    return englishtext
