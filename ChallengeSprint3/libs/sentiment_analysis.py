from nltk.sentiment.vader import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt

def sentiment_analysis():
  sid = SentimentIntensityAnalyzer()
  
  text = """A inteligência artificial é a inteligência similar à humana máquinas. 
      Definem como o estudo de agente artificial com inteligência. 
      Ciência e engenharia de produzir máquinas com inteligência. 
      Resolver problemas e possuir inteligência. 
      Relacionada ao comportamento inteligente. 
      Construção de máquinas para raciocinar. 
      Aprender com os erros e acertos. 
      Inteligência artificial é raciocinar nas situações do cotidiano."""

  sentiments_scores = sid.polarity_scores(text)
  sentiments = []
  scores = []
  
  for key in sentiments_scores:
    if key == 'neg':
      sentiments.append('Negativo')
      scores.append(sentiments_scores[key])
    elif key == 'neu':
      sentiments.append('Neutro')
      scores.append(sentiments_scores[key])
    elif key == 'pos':
      sentiments.append('Positivo')
      scores.append(sentiments_scores[key])
  
  plt.bar(sentiments, scores)
  plt.xlabel('Polaridade dos Sentimentos')  
  plt.ylabel('Scores dos Sentimentos')
  plt.show()
  
  if ord('q') == 0xFF:
    plt.close()