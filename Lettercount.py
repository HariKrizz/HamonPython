
import unittest

def charCount(word):
    dictionary = {}
    for character in word:

        if character in dictionary:
            dictionary[character] += 1
        else:
            dictionary[character] = 1

    for character, count in dictionary.items() :
        print(character,"-->",count)

#charCount("Apple")

class Test_charCount(unittest.TestCase):
    def testRepeat(self):
        ret = charCount("cccccc")
        self.assertEqual(ret, {"c" : 6})

    def testNone(self):
        ret = charCount("")
        self.assertEqual(ret, {})

    def testOneLetter(self):
        ret = charCount("a")
        self.assertEqual(ret, {"a" : 1})
        
    def testSingleOccurence(self):
        ret = charCount("abcd")
        self.assertEqual(ret, {"a":1 , "b":1, "c": 1, "d": 1})


if __name__ == "__main__":
    unittest.main()
