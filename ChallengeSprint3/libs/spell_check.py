from spellchecker import SpellChecker
from nltk.tokenize import word_tokenize

# frase de teste: Meu corasão não çei porque bati felis quando ti vê

def spell_check():
  phrase = str(input('Digite uma frase que deseja corrigir: '))
  original_phrase = phrase
  
  spell = SpellChecker(language="pt")
  tokens = word_tokenize(phrase)
  misspelled = spell.unknown(tokens)
  
  for word in misspelled:
    phrase = phrase.replace(word, spell.correction(word))
  
  print(f"Frase original: {original_phrase}")
  print(f"Frase corrigida: {phrase}")
