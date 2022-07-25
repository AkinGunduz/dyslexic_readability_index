import math

from utils import get_char_count
from utils import get_words
from utils import get_sentences
from utils import get_syllable_count


class Readability:
    analyzedVars = {}

    def __init__(self, text):
        self.analyze_text(text)

    def analyze_text(self, text):
        words = get_words(text)
        
        char_count = get_char_count(words)
        word_count = len(words)
        sentence_count = len(get_sentences(text))
        syllable_count = get_syllable_count(words)
        avg_words_p_sentence = word_count / sentence_count
        
        self.analyzedVars = {
            'words': words,
            'char_cnt': float(char_count),
            'word_cnt': float(word_count),
            'sentence_cnt': float(sentence_count),
            'syllable_cnt': float(syllable_count),
            'avg_words_p_sentence': float(avg_words_p_sentence)
        }

    def ARI(self):
        score = 0.0
        if self.analyzedVars['word_cnt'] > 0.0:
            score = 4.71 * (self.analyzedVars['char_cnt'] / self.analyzedVars['word_cnt']) + 0.5 * (
                        self.analyzedVars['word_cnt'] / self.analyzedVars['sentence_cnt']) - 21.43
        return score

    def FleschReadingEase(self):
        score = 0.0
        if self.analyzedVars['word_cnt'] > 0.0:
            score = 206.835 - (1.015 * (self.analyzedVars['avg_words_p_sentence'])) - (
                        84.6 * (self.analyzedVars['syllable_cnt'] / self.analyzedVars['word_cnt']))
        return round(score, 4)

    def Atesman(self):
        score = 0.0
        if self.analyzedVars['word_cnt'] > 0.0:
            score = 198.825 - (2.61 * (self.analyzedVars['avg_words_p_sentence'])) - (
                        40.175 * (self.analyzedVars['syllable_cnt'] / self.analyzedVars['word_cnt']))
        #print("avg_words_p_sentence ",self.analyzedVars['avg_words_p_sentence'])
        #print("syllable_cnt ",self.analyzedVars['syllable_cnt'])
        #print("word_cnt ",self.analyzedVars['word_cnt'])
        if score>100: score = 100.000
        if score<0: score = 10
        return round(score, 4)

    def FleschKincaidGradeLevel(self):
        score = 0.0
        if self.analyzedVars['word_cnt'] > 0.0:
            score = 0.39 * (self.analyzedVars['avg_words_p_sentence']) + 11.8 * (
                        self.analyzedVars['syllable_cnt'] / self.analyzedVars['word_cnt']) - 15.59
        return round(score, 4)

    def ColemanLiauIndex(self):
        score = 0.0
        if self.analyzedVars['word_cnt'] > 0.0:
            score = (5.89 * (self.analyzedVars['char_cnt'] / self.analyzedVars['word_cnt'])) - (
                        30 * (self.analyzedVars['sentence_cnt'] / self.analyzedVars['word_cnt'])) - 15.8
        return round(score, 4)

    def LIX(self):
        longwords = 0.0
        score = 0.0
        if self.analyzedVars['word_cnt'] > 0.0:
            for word in self.analyzedVars['words']:
                if len(word) >= 7:
                    longwords += 1.0
            score = self.analyzedVars['word_cnt'] / self.analyzedVars['sentence_cnt'] + float(100 * longwords) / \
                    self.analyzedVars['word_cnt']
        return score

    def RIX(self):
        longwords = 0.0
        score = 0.0
        if self.analyzedVars['word_cnt'] > 0.0:
            for word in self.analyzedVars['words']:
                if len(word) >= 7:
                    longwords += 1.0
            score = longwords / self.analyzedVars['sentence_cnt']
        return score

    def overall_readability_scores(self):
        ARI = self.ARI()
        FleschReadingEase = self.FleschReadingEase()
        FleschKincaidGradeLevel = self.FleschKincaidGradeLevel()
        ColemanLiauIndex = self.ColemanLiauIndex()
        LIX = self.LIX()
        RIX = self.RIX()
        Atesman = self.Atesman()
        
        readibilityscores = [ARI,FleschReadingEase,FleschKincaidGradeLevel,ColemanLiauIndex,LIX,RIX,Atesman]
        
        return readibilityscores

