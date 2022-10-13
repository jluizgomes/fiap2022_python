#lendo 2 valores para iniciar a rotina
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 9:

    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] subtrair
    [ 4 ] dividir
    [ 5 ] maior
    [ 6 ] menor
    [ 7 ] média
    [ 8 ] novos números
    [ 9 ] fechar programa''')
    print('=-=' * 12)
    opcao = int(input('Qual é a sua opção? '))
    #Somando os valores
    if opcao == 1:
        soma = n1 + n2
        print('A soma entre {} + {} é {}'.format(n1, n2, soma))
    #Multiplicando os valores
    elif opcao == 2:
        mult = n1 * n2
        print('A multiplicação entre {} x {} é {}'.format(n1, n2, mult))
    #Subtraindo os valores
    elif opcao == 3:
        if n1 < n2:
            maior = n2
            sub = maior - n1
            print('A subtração entre {} - {} é {}'.format(n1, maior, sub))
        else:
            sub = n1 - n2
            print('A subtração entre {} - {} é {}'.format(n1, n2, sub))
    #Dividindo os valores
    elif opcao == 4:
        div = n1 / n2
        print('A divisão entre {} / {} é {:.2f}'.format(n1, n2, div))
    #Mostrando o maior valor
    elif opcao == 5:
        if n1 > n2:
            maior = n1
            print('Entre {} e {} o maior valor é {}'.format(n1, n2, maior))
        elif n2 > n1:
            maior = n2
            print('Entre {} e {} o maior valor é {}'.format(n1, n2, maior))
        else:
            print('{} e {} são valores iguais'.format (n1, n2))
    #Mostrando o menor valor
    elif opcao == 6:
        if n1 < n2:
            menor = n1
            print('Entre {} e {} o menor valor é {}'.format(n1, n2, menor))            
        elif n2 < n1:
            menor = n2
            print('Entre {} e {} o menor valor é {}'.format(n1, n2, menor))
        else:
            print('{} e {} são valores iguais'.format(n1, n2))
    #Mostrando a média
    elif opcao == 7:
        media = (n1 + n2) / 2
        print('Entre {} e {} a média é {}'.format(n1, n2, media))
    #Solicinando novos valores
    elif opcao == 8:
        print('Informe os números novamente: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    #Saindo do programa
    elif opcao == 9:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente')
    print('=-=' * 12)
print('Fim do programa! Volte sempre!!')
