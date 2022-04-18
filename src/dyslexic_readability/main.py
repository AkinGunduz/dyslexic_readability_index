# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 22:03:46 2021

@author: aking
"""

import numpy as np
import nltk
import editdistance
from nltk.util import ngrams
import utils

class Dyslexia():
    
    def __init__(self, my_text):
        self.my_text = my_text
        
    def find_Levenshtein_Distance(self):
        token = nltk.word_tokenize(self.my_text)
        similarities = []
        
        for x in token:
            count_distance = 0
            count_compute = 0
            for y in token:
                count_compute= count_compute+1
                Max_Levenshtein_Distance = max(len(x),len(y))
                Levenshtein_Distance = editdistance.eval(x, y)
                if (Levenshtein_Distance >(Max_Levenshtein_Distance/2)):
                    count_distance = count_distance+1
    
            similarities.append(count_distance / len(token))

        count_distance_bigrams = 0
        count_compute_bigrams = 0
        bigrams = ngrams(token, 2)

        for i in bigrams:
            count_compute_bigrams = count_compute_bigrams + 1
            Max_Levenshtein_Distance_Bigrams = max(len(i[0]),len(i[1]))
            Levenshtein_Distance_Bigrams = editdistance.eval(i[0],i[1])
            if (Levenshtein_Distance_Bigrams > (Max_Levenshtein_Distance_Bigrams/2)):
                count_distance_bigrams = count_distance_bigrams + 1
    
        similarities_bigrams = (count_distance_bigrams / len(token))

        return (np.mean(similarities)+similarities_bigrams)/2

    def find_mirror_words(self):
        mirror_word_count = 0
        my_text1 = self.my_text.lower()
        result1 = my_text1.replace("p", "1").replace("b", "1").replace("d", "1").replace("h", "1").replace("g", "1").replace("ğ", "1")
        result2 = result1.replace("m", "2").replace("n", "2").replace("a", "2").replace("e", "2").replace("r", "2").replace("u", "2").replace("ü", "2")
        result3 = result2.replace("v", "3").replace("k", "3").replace("z", "3").replace("y", "3")
        result4 = result3.replace("s", "4").replace("ş", "4").replace("ö", "4").replace("o", "4").replace("c", "4").replace("ç", "4")
        result5 = result4.replace("ı", "5").replace("i", "5").replace("l", "5").replace("f", "5").replace("t", "5").replace("j", "5")
      
        token = nltk.word_tokenize(result5)
        token_scores = []
        for i in token:
            count_1 = 0
            d = dict.fromkeys(i, 0)
            
            for c in i:
                d[c] += 1
                if (d[c]>1):
                    count_1 += 1
            score_x = count_1 / len(i)
            token_scores.append([score_x])
            
            if (count_1>0):
                mirror_word_count += 1

        return np.mean(token_scores)
    
    def find_similar_starts(self):
        similar_starts_count = 1
        equal_words = 0
        a, b, c, d = [],[],[],[]
        first_word, second_word = [],[]
        token = nltk.word_tokenize(self.my_text)   
        bigrams = ngrams(token, 2)

        for i in bigrams:
            first_word.append(i[0])
            second_word.append(i[1])
            if(i[0]==i[1]):
                equal_words += 1
   
        for x in first_word:
            a.append(x[0:2])

        for y in second_word:
            b.append(y[0:2])

        for harf in a:
            c.append(harf)

        for harf in b:
            d.append(harf)
                
        for t in range(len(c)):
            if(c[t]==d[t]):
                similar_starts_count += 1

        return ((similar_starts_count-equal_words)/(len(token)-1))
    
    def kokofoni(self):
        kokofoni = 0
        
        result1 = self.my_text.replace("f","1").replace("ğ", "1").replace("h", "1").replace("j", "1").replace("l", "1").replace("m", "1").replace("n", "1").replace("r", "1").replace("s", "1").replace("ş", "1").replace("v", "1").replace("y", "1").replace("z", "1")
        result2 = result1.replace("b", "2").replace("c", "2").replace("ç", "2").replace("d", "2").replace("g", "2").replace("k", "2").replace("p", "2").replace("t", "2")
        result3 = result2.replace("a", "").replace("e", "").replace("u", "").replace("o", "").replace("ö", "").replace("ü", "").replace("i", "").replace("ı", "")
        
        token = nltk.word_tokenize(result3)
        
        kokofoni = []
        for i in token:
            count_1 = 0
            d = dict.fromkeys(i, 0)   
            for c in i:
                d[c] += 1
                if (d[c]>1):
                    count_1 += 1 
            kokofoni.append(count_1/len(i))

        return np.mean(kokofoni)

    def find_readability_scores(self):
        rd = Readability(self.my_text)
        ARI = rd.ARI()
        FleschReadingEase = rd.FleschReadingEase()
        FleschKincaidGradeLevel = rd.FleschKincaidGradeLevel()
        GunningFogIndex = rd.GunningFogIndex()
        SMOGIndex = rd.SMOGIndex()
        ColemanLiauIndex = rd.ColemanLiauIndex()
        LIX = rd.LIX()
        RIX = rd.RIX()
        Atesman = rd.Atesman()
        
        readibilityscores = [ARI,FleschReadingEase,FleschKincaidGradeLevel,GunningFogIndex,SMOGIndex,ColemanLiauIndex,LIX,RIX,Atesman]
        
        return readibilityscores

    def bogumlanmalarinagore(self):
        dudak = self.my_text.replace("b","1").replace("f", "1").replace("m", "1").replace("p", "1").replace("v", "1")
        diş = dudak.replace("c", "2").replace("ç", "2").replace("d", "2").replace("j", "2").replace("n", "2").replace("s", "2").replace("ş", "2").replace("t", "2").replace("z", "2")
        damak = diş.replace("g", "3").replace("ğ", "3").replace("k", "3").replace("l", "3").replace("r", "3").replace("y", "3")
        girtlak = damak.replace("h", "4")
        result = girtlak.replace("a", "").replace("e", "").replace("u", "").replace("o", "").replace("ö", "").replace("ü", "").replace("i", "").replace("ı", "")
        
        token = nltk.word_tokenize(result)

        bogum = []
        for i in token:
            count_1 = 0
            d = dict.fromkeys(i, 0)   
            for c in i:
                d[c] += 1
                if (d[c]>1):
                    count_1 += 1 
            bogum.append(count_1/len(i))
                
        return np.mean(bogum)

def main(my_text):
    sentences = utils.get_sentences(my_text)
    corpus = []
    
    for i in sentences:
        transcript = i.lower()
        transcript = transcript.split()
        transcript = ' '.join(transcript)
        
        scoreCalculator = Dyslexia(transcript)
        
        LD = scoreCalculator.find_Levenshtein_Distance()
        M = scoreCalculator.find_mirror_words()
        FS = scoreCalculator.find_similar_starts()
        K = scoreCalculator.kokofoni()
        B = scoreCalculator.bogumlanmalarinagore()
        score =  (M + FS + K + B + LD)/5
        corpus.append(score)

    dyslexicReadabilityScore = np.mean(corpus)*100
    
    return dyslexicReadabilityScore,sentences

tez_cumleleri = [
    "özge sarı topla oynadı",
    "kemal sakince ikna oldu",
    "gelen mektup kısa cevaplı",
    "önceki koşul baki kaldı",
    "köpek kafası başka yönde",
    "demir derede olta atar",
    "bade banada pudra sürdü",
    "edip depodan buğday getir",
    "aşçı mera menüsü açmış",
    "atıl altı alet atıldı",
    "sonunda asetonu asitle temizledim",
    "destansı donatı dostlukla bitti",
    "doğuş aşağıya doğru yuvarlandı",
    "eminönünü gezenler memnun ayrıldı",
    "bombeli bambulardan pompa yaptık"]

#f = open('teststory2.txt', encoding="utf8")

for i in tez_cumleleri:
    result,sentences = main(i)
    print('Sentence: ', sentences, '   Score:  ' + str(result))












