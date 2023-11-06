import random

import wordcloud

chars = [chr(x+ord('A')) for x in range(26)]
freq = [random.randint(1,100) for i in range(26)]
cf = {x[0]:x[1] for x in zip(chars,freq)}
print(cf)
wc = wordcloud.WordCloud()
wc.fit_words(cf)
wc.to_file('ex.png')