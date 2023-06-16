'''Peer Review Assignment'''
from deep_translator import MyMemoryTranslator
def englishtofrench(englishtext):
    """
    This function returns the translation from english to french
     """
    frenchtext = MyMemoryTranslator(source='en', target='french').translate(englishtext)
    print(frenchtext)
    return frenchtext

def frenchtoenglish(frenchtext):
    """
    This function returns the translation from french to english
     """
    englishtext = MyMemoryTranslator(source='fr', target='english').translate(frenchtext)
    print(englishtext)
    return englishtext
