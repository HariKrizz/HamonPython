
from Panagram import isPanagram

def testPanagramFalse():
    ret = isPanagram("Hello world")
    assert ret == False

def testPanagramTrue():
    ret = isPanagram("the quick brown fox jumps over the lazy dog")
    assert ret == True 

    