import nltk
from nltk.tokenize import RegexpTokenizer
from dyslexic_readability.syllable.syllable import Encoder

TOKENIZER = RegexpTokenizer('(?u)\W+|\$[\d\.]+|\S+')
SPECIAL_CHARS = ['.', ',', '!', '?']


def get_syllable_count(words):
    encoder = Encoder(lang="tr", limitby="vocabulary", limit=3000)
    syllable_cnt = 0
    for word in words:
        syllable_cnt = syllable_cnt + len(encoder.tokenize(word).split())
    
    return syllable_cnt

def get_char_count(words):
    characters = 0
    for word in words:
        characters += len(word)
    return characters


def get_words(text=''):
    words = []
    words = TOKENIZER.tokenize(text)
    filtered_words = []
    for word in words:
        if word in SPECIAL_CHARS or word == " ":
            pass
        else:
            new_word = word.replace(",", "").replace(".", "")
            new_word = new_word.replace("!", "").replace("?", "")
            filtered_words.append(new_word)
    return filtered_words


def get_sentences(text=''):
    tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
    sentences = tokenizer.tokenize(text)
    return sentences