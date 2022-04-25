from operator import imod
import dyslexic_scores
import readability_scores

sentences = [
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
    "bombeli bambulardan pompa yaptık",
    "Gagavuz kuşunun gagası gerdandan sarkar, ger ger gerilen gergefin gültası Galata’dan galat gergedana gül atar.",
    "Safranbolulu Safinazla Salihlili Salih, Soğukoluk’ta soğuklamışlar, sinüzit olmuşlar, sonra sımsıkı sarınarak söylene söylene Seyitgazi’ye varıp sarmısaklı su teresini susarmısağıyla karıştırarak suyunu süzmüşler."]


for i in sentences:
    obj = dyslexic_scores.DyslexicScores(i)
    obj_r = readability_scores.Readability(i)

    print('Sentence: ', i,
          '  Dyslexic Score:  ' + str(round(obj.overall_dyslexic_score(),2)) + 
          '  Atesman Score: ' + str(obj_r.Atesman()) +
          '  Mean Score:  ' + str((1- (0.01*obj.overall_dyslexic_score()))*obj_r.Atesman()))

