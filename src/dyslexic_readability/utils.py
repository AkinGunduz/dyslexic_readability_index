import nltk
from nltk.tokenize import RegexpTokenizer

TOKENIZER = RegexpTokenizer('(?u)\W+|\$[\d\.]+|\S+')
SPECIAL_CHARS = ['.', ',', '!', '?']
LOWER_VOWEL = {'a', 'â', 'e', 'ê', 'ı', 'î', 'i', 'o', 'ô', 'ö', 'u', 'û', 'ü'}
SPELL_SLICER = (('001000', 5), ('000100', 5), ('01000', 4), ('00100', 4), ('00010', 4), ('1000', 3), ('0100', 3),
                ('0011', 3), ('0010', 3), ('011', 2), ('010', 2), ('100', 2), ('10', 1), ('11', 1))

def to_lower(word):
    tolower_text = (word.replace('İ', 'i'))
    tolower_text = (tolower_text.replace('I', 'ı'))

    return tolower_text.lower()

def wordtoten(word: str):
    wtt = ''
    for ch in word:
        if ch in LOWER_VOWEL:
            wtt += '1'
        else:
            wtt += '0'

    return wtt

def spellword(word: str):
    word = to_lower(word)
    syllable_list = []
    tenword = wordtoten(word)
    len_spell = tenword.count('1')

    for i in range(tenword.count('1')):
        for x, y in SPELL_SLICER:
            if tenword.startswith(x):
                syllable_list.append(word[:y])
                word = word[y:]
                tenword = tenword[y:]
                break

    if tenword == '0' and len(word) > 1:
        syllable_list[-1] = syllable_list[-1] + word
    elif word:
        syllable_list.append(word)

    return syllable_list

def get_syllable_count(words):
    syllable_cnt = 0
    for word in words:
        syllable_cnt = syllable_cnt + len(spellword(word))
    
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