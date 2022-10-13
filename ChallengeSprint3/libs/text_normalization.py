import re,string
from nltk.corpus import stopwords

stopwords = stopwords.words('portuguese')

def text_normalization(text):
    text = str(text).lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub('https?://\S+|www\.\S+', '', text)
    text = re.sub('<.*?>+', '', text)
    text = re.sub(f'[{re.escape(string.punctuation)}]', '', text)
    text = re.sub('\n', '', text)
    text = re.sub('\w*\d\w*', '', text)

    return ' '.join([word for word in text.split() if word not in (stopwords)])