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
]


for i in sentences:
    obj = dyslexic_scores.DyslexicScores(i)
    obj_r = readability_scores.Readability(i)

    print(
        "Sentence: ",
        i,
        "Dyslexic Score:  ",
        obj.overall_dyslexic_score(),
        "Atesman Score: ",
        obj_r.Atesman(),
        "Overall Score:  ",
        obj.overall_calculated_score(),
    )

story = (
    "Ormanların birinde bir sivrisinek yaşarmış."
    " Bu sivrisinek tüm hayvanları rahatsız edercesine kral olduğunu iddia ediyormuş."
    " Her önüne gelen hayvana kafa tutuyormuş. Yine hayvanlara laf ederken sıra kurbağaya gelmiş."
    " Kurbağa ona hayvanların kralının aslan olduğunu söylemiş. Buna sinirlenen sinek aslanın yanına gitmiş."
    " Aslan bir ağacın dibinde uyukluyormuş. Gidip başında vızıldayarak kral olduğunu iddia etmiş."
    " Aslanı sinir edince aslan sineğe pençe sallamış. Ama ıskalayınca sinek daha da uğraşmaya başlamış."
    " Aslan bir daha sinir olunca yine pençe sallamış ama tutturamamış."
    " Sinek iyice şımarmaya başlamış, kulağının dibine vızıldayarak daha da sinir bozmaya çalışıyormuş."
    " Aslında hedefine ulaşması için son bir şey yapması lazımmış. Aslana zarar vererek üstünlüğünü kanıtlayacağını düşünüyormuş."
    " Bunun da ardından sinek gidip aslanın burnunu iğnesi ile sokmuş. Aslan ise öfkelenerek kükremiş."
    " Sinek oradan uzaklaşarak aslanı yendiği için mutlu davranıyormuş. Örümcek ağına yakalanana kadar sürecekmiş bu mutluluğu."
    " Örümcek ağına yakalanınca kurtulamamış. Yardım çığlıkları atınca aslan gelip onu kurtarmış."
    " Bu da sineğe ders olmuş ve bir daha hiç kral olduğunu iddia etmemiş."
)

obj = dyslexic_scores.DyslexicScores(story)
obj_r = readability_scores.Readability(story)

print(
    "Dyslexic Score:  ",
    obj.overall_dyslexic_score(),
    "Atesman Score: ",
    obj_r.Atesman(),
    "Overall Score:  ",
    obj.overall_calculated_score(),
)