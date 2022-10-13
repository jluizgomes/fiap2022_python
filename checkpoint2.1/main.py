# EXERCÍCIOS:
# 1. Contar palavras
#         Testes:
#         Olá, bom dia (3)
#         Olá,bom.dia(3)
#         Olá,                bom.dia (3)
# 2. Dados 9 digitos do numero do CPF, verificar se ele é ou não válido
# 3. Dados 9 digitos do numero do CPF, apresentar os 2 dígitos correspondentes
# 4. Gerar um CPF aleatório
# from random import randint
# numero = str(randint(100000000, 999999999))
# 5. Utilizando parâmetros dinâmicos, faça uma função que calcule a média dos argumentos
# 6. Utilizando parâmetros dinâmicos, retornar o maior valor

#   CPF = 168.995.350-09
#   ------------------------------------------------
#   1 * 10 = 10           #    1 * 11 = 11 <-
#   6 * 9  = 54           #    6 * 10 = 60
#   8 * 8  = 64           #    8 *  9 = 72
#   9 * 7  = 63           #    9 *  8 = 72
#   9 * 6  = 54           #    9 *  7 = 63
#   5 * 5  = 25           #    5 *  6 = 30
#   3 * 4  = 12           #    3 *  5 = 15
#   5 * 3  = 15           #    5 *  4 = 20
#   0 * 2  = 0            #    0 *  3 = 0
#                         # -> 0 *  2 = 0
#           297          #             343
#   11 - (297 % 11) = 11  #     11 - (343 % 11) = 9
#   11 > 9 = 0            #
#   Digito 1 = 0          #   Digito 2 = 9

import re

def countWords(phase):
  phase = re.sub("[^A-Za-zÀ-Úà-ú]", ' ', phase)
  words = phase.split()
  return len(words)

def validateCPF(cpf):
  cpf = re.sub("[^0-9]", '', cpf)

  if cpf in [
      '00000000000', '11111111111', '22222222222', '33333333333',
      '44444444444', '55555555555', '66666666666', '77777777777',
      '88888888888', '99999999999'
  ]:
    return False

  if len(cpf) != 11:
    return False

  verifyDigit = verify_digit_CPF(10, 9, cpf)
  verifyDigit2 = verify_digit_CPF(11, 10, cpf)
  
  if verifyDigit == int(cpf[9]) and verifyDigit2 == int(cpf[10]):
    return 'Válido'
  return 'Inválido'

def verify_digit_CPF(*args):
  sum_num = 0
  weight = int(args[0])

  for count in range(int(args[1])):
    sum_num = sum_num + int(args[2][count]) * weight
    weight = weight - 1

  value = 11 - (sum_num % 11)

  return 0 if value > 9 else value

def calcMedia(*args):
  sum_num = 0
  nums = re.sub("[^0-9]",'', args[0])
  
  for count in range(len(nums)):
    num = int(nums[count])
    sum_num += num
  return sum_num / len(nums)

def maxValue(*args):
  max_num = 0
  nums = args[0].replace(',', ' ').split(' ')

  for count in range(len(nums)):
    if nums[count] != ',':
      num = int(nums[count])
      if num > max_num:
        max_num = num
  return max_num

def want_continue():
  want_continue = str(input('\nDeseja continuar? (S/N): '))
  
  if want_continue in {'S', 's'}:
    main()
  else:
    print('\nObrigado por utilizar o nosso programa!\n')
    exit()

def assemble_menu():
  menu_options = {
    1: 'Contar palavras',
    2: 'Validar CPF',
    3: 'Calcular média',
    4: 'Maior valor',
    5: 'Sair do programa'
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
      phase = str(input('Digite uma frase: '))
      print(f"Total de palavras: {countWords(phase)}")
      want_continue()
    elif option == 2:
      cpf = str(input('Digite o CPF: '))
      print(f"O CPF digitado é {validateCPF(cpf)}")
      want_continue()
    elif option == 3:
      media = input('Digite a quantidade de números que deseja calcular a média separado por vírgula: ')
      print(f'Média: {round(calcMedia(media), 2)}')
      want_continue()
    elif option == 4:
      max_num = input('Digite a quantidade de números que deseja calcular a média separado por vírgula: ')
      print(f'Maior valor: {maxValue(max_num)}')
      want_continue()
    elif option == 5:
      print('\nObrigado por utilizar o nosso programa!\n')
      exit()
    else:
      print('\nOpção inválida! Por favor escolha entre as opções de 1 a 3.')

if __name__ == '__main__':
  main()