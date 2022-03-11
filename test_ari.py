from ari import *


def test_char_count_None():
    ret = charCount("")
    assert ret == 0

def test_char_count_Invalidchar():
    ret = charCount('"~!@#$%^&*()_+*/-{}''[]|;:`=')
    assert ret == 0

def test_char_count_Multiple():
    ret = charCount("hello there 12345")
    assert ret == 15

def test_word_count_None():
    ret = wordCount("abcd")
    assert ret == 0

def test_word_count_Multiple():
    ret = wordCount("abcd 1234 wxyz 5678")
    assert ret == 3

def test_sentence_count_None():
    ret = sentenceCount("abcd1234hello")
    assert ret == 0
    
def test_sentence_count_Multiple():
    ret = sentenceCount("abcd.1234?hello!")
    assert ret == 3

def test_ari_calculate_score_greater14():
    ret = autoreadIndex_Calculate("Hello! How are you?") > 14
    assert ret == True


