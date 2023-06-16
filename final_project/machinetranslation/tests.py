import unittest
from translator import englishtofrench,frenchtoenglish

class TestFrensh(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(englishtofrench('Hello'),'Bonjour')
        self.assertNotEqual(englishtofrench('Bonjour'), 'Hello')
        # test when  Hello is given as input the output is Bonjour.


         
class TestEnglish(unittest.TestCase): 
    def test1(self): 
        self.assertNotEqual(frenchtoenglish('Hello'), 'Bonjour')
        # test when  Bonjour is given as input the output is Hello.
        self.assertEqual(frenchtoenglish('Bonjour'), 'Hello') 
        
        
unittest.main()

