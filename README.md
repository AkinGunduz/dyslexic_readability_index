# Dyslexic Readability Package

A readability scoring library tailored to the specific needs of Turkish dyslexic readers.

## Install

The package is available on PyPI. Simply install it with pip:

```bash
  pip install dyslexic-readability
```

## Dependencies

This project uses the following python libraries. Please use Python3+.

`nltk`
`numpy`
`editdistance`

## Basic Usage

```python
from dyslexic_readability import dyslexic_scores, readability_scores

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
```