import matplotlib.pyplot as plt
from wordcloud import WordCloud
from collections import Counter
from spellchecker import SpellChecker
from nltk.tokenize import word_tokenize
from libs.text_normalization import text_normalization

def create_wordcloud():
  spell = SpellChecker(language="pt")
  
  text = """A inteligência artificial é a inteligência similar à humana máquinas. 
      Definem como o estudo de agente artificial com inteligência. 
      Ciência e engenharia de produzir máquinas com inteligência. 
      Resolver problemas e possuir inteligência. 
      Relacionada ao comportamento inteligente. 
      Construção de máquinas para raciocinar. 
      Aprender com os erros e acertos. 
      Inteligência artificial é raciocinar nas situações do cotidiano."""

  text = text_normalization(text)
  word_tokens = word_tokenize(text)
  words = [spell.correction(word_tokens[x]) for x in range(len(word_tokens))]
  word_cloud_lst = Counter(words)
  wordcloud = WordCloud(background_color='black', min_font_size=10).generate_from_frequencies(word_cloud_lst)
  plt.imshow(wordcloud, interpolation='bilinear')
  plt.axis("off")
  plt.tight_layout(pad = 0)
  plt.show()

  if ord('q') == 0xFF:
    plt.close()