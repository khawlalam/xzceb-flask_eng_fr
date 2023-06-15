import unittest

from translator import englishtofrench,frenchtoenglish

class TestFrensh(unittest.TestCase): 
    def test1(self): 
        self.assertNotEqual(englishtofrench("Hello"), "Bonjour")
         # test when  Hello is given as input the output is Bonjour.
        
        
class TestEnglish(unittest.TestCase): 
    def test1(self): 
        self.assertNotEqual(frenchtoenglish('Bonjour'), 'Hello') 
        # test when  Bonjour is given as input the output is Hello.
        
        
unittest.main()

