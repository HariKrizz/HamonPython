import math

def charCount(s):
    cCount = 0
    for i in s:
        if i.isalnum():
            cCount += 1
    return cCount

def wordCount(s):
    wCount = 0
    for i in s:
        if i == " ":
           wCount += 1
    return wCount

def sentenceCount(s):
    return s.count('!') + s.count('.') + s.count("?")

def autoreadIndex_Calculate(s):
    chars = charCount(string)
    words = wordCount(string)
    sentences = sentenceCount(string)

    ari_index = math.ceil(4.71 *(chars/words) + 0.5*(words/sentences))

    dict={
          1:"5-6 Kindergarten",
          2:"6-7 First Grade",
          3:"7-8 Second Grade",
          4:"8-9 Third Grade",
          5:"9-10 Fourth Grade",
          6:"10-11 Fifth Grade",
          7:"11-12 Sixth Grade",
          8:"12-13 Seventh Grad",
          9:"13-14 Eighth Grade",
          10:'14-15 Ninth Grade',
          11:'15-16 Tenth Grade',
          12:'16-17 Eleventh Grade',
          13:'17-18 Twelfth Grade',
          14:'18-22 College student'
          }
    return dict[ari_index]

string = """The Automated Readability Index is derived from ratios representing word difficulty (number of letters per word) 
and sentence difficulty (number of words per sentence).The first consideration in developing the Automated Readability Index was 
to establish that the factors used relate to those found in other indices!? The factor relating to sentence structure 
(average number of words per sentence) is identical to that found in most currently used indices , such as the Coleman-Liau Index,
so no verification was required!. The verification of the relationship between the word structure factor was also virtually self-evident!.
Most readability indices consist of two factors!. One factor relates to sentence structure and is most generally a measure of the average 
number of words per sentence!.The other factor generally relates to word structure and is usually based on either the proportion of easy 
words determined with reference to word list (Dale and Chall, 1948) or the average number of syllables per word (Flesch, 1951).
While the word list has many advantages, especially in 4th lower grades, it is both slow? and relatively inaccurate when applied to adult 
reading material!. Syllable counts prove to be deceptively unreliable!.""" 

print(charCount(string))
print(wordCount(string))
print(sentenceCount(string))
print(autoreadIndex_Calculate(string))

