"""
SPRINT 3 - Entregáveis
1 - Considerando o Sprint 2 devidamente criado, escolha e codifique ao menos 3 funcionalidades do menu, utilizando os conceitos aprendidos: Funções / procedimentos / listas.

Entrega:
Compactar em um arquivo (de preferência extensão .zip), o arquivo .py com o projeto em Python Postar o arquivo .zip no portal.

RM93250 - Caio Santos
RM93293 - Eduardo Oliveira Santos Cunha
RM96078 - ISABELLI ANDRADE DE SOUZA
RM92815 - Jorge Luiz Gomes
RM95965 - Rodrigo Fernandes
"""

from libs.spell_check import spell_check
from libs.words_cloud import create_wordcloud
from libs.sentiment_analysis import sentiment_analysis

def option_one():
  spell_check()
  want_continue()

def option_two():
  create_wordcloud()
  want_continue()
  
def option_three():
  sentiment_analysis()
  want_continue()

def want_continue():
  want_continue = str(input('\nDeseja continuar? (S/N): '))
  
  if want_continue in {'S', 's'}:
    main()
  else:
    print('\nObrigado por utilizar o nosso programa!\n')
    exit()

def assemble_menu():
  menu_options = {
    1: 'Correção ortográfica',
    2: 'Nuvem de palavras',
    3: 'Análise de sentimento',
    4: 'Sair do programa'
  }

  print('\nEscolha uma opção do menu\n')
  
  for key in menu_options:
    print(f'{key}. {menu_options[key]}')
    
def main():
  while True:
    assemble_menu()
    option = ''

    try:
      print()
      option = int(input('Digite a opção desejada: '))
    except Exception:
      print('\nOpção inválida! Por favor escolha entre as opções de 1 a 3.')

    if option == 1:
      option_one()
    elif option == 2:
      option_two()
    elif option == 3:
        option_three()
    elif option == 4:
      print('\nObrigado por utilizar o nosso programa!\n')
      exit()
    else:
      print('\nOpção inválida! Por favor escolha entre as opções de 1 a 3.')

if __name__ == '__main__':
  main()