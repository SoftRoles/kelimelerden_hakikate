#%%



"""
Minimal Example
===============
Generating a square wordcloud from the US constitution using default arguments.
"""

import os

from os import path
from wordcloud import WordCloud
import arabic_reshaper
import codecs
from bidi.algorithm import get_display
from alphabet_detector import AlphabetDetector
ad = AlphabetDetector()

# get data directory (using getcwd() is needed to support running example in generated IPython notebook)
d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

# Read the whole text.
# text = open(path.join(d, 'fatiha-tr.txt')).read()
# text = codecs.open(os.path.join(d, 'fatiha.txt'), 'r', 'utf-8').read()
text = get_display(arabic_reshaper.reshape(codecs.open(os.path.join(d, 'fatiha.txt'), 'r', 'utf-8').read()))
# for word in text.split():
#     print(list(ad.detect_alphabet(word))[0])
    
# Generate a word cloud image
wordcloud = WordCloud().generate(text)

# Display the generated image:
# the matplotlib way:
import matplotlib.pyplot as plt
# plt.imshow(wordcloud, interpolation='bilinear')
# plt.axis("off")

# lower max_font_size
# wordcloud = WordCloud(max_font_size=50, max_words=30, min_font_size=50).generate(text)
# wordcloud = WordCloud(font_path='NotoNaskhArabic-Regular.ttf', max_font_size=40).generate(text)
# wordcloud = WordCloud(font_path='ArabicLatin.ttf', max_words=50, max_font_size=50, min_font_size=40).generate(text)
wordcloud = WordCloud(font_path='ArabicLatin.ttf', max_font_size=200, min_font_size=10, width=1080, height=1080, contour_color="white").generate(text)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.savefig("wordcloud.png",dpi=300)
plt.show()