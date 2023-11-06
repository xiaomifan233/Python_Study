import cv2
from wordcloud import WordCloud

mask = cv2.imread('R-C.png')
f = open('word.txt', 'r', encoding='utf-8')
text = f.read()
wc = WordCloud(background_color='white',
               width=512, height=512,
               max_words=200,
               max_font_size=50,
               mask=mask,
               ).generate(text)
wc.to_file('苹果.jpg')
