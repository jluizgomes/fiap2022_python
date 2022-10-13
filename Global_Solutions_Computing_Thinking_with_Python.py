opcao = 100
while opcao != 0:
    print("\nVOTAÇÃO - SEGUNDO TURNO")
    print("-------------------------------------------")
    print("1 - Efetuar a votação")
    print("2 - Exibir o relatório dos votos")
    print("3 - Efetuar a apuração / Exibir o resultado")
    print("4 - Mostrar o percentual dos votos")
    print("0 - Sair")
    print("-------------------------------------------\n")
    opcao = int(input("Digite a Opção desejada: "))

#1 – Efetuar a votação Nesta rotina, os eleitores terão a opção de votar em 2 (dois) candidatos (pode escolher os nomes),
# haja vista que é uma rotina criada para o segundo turno. 
    
    if opcao == 1:
        nulos = []
        pedrinho = []
        joaozinho = []
        voto = 10
        print('\n------------------------------------------------')
        print("Votação de segundo turmo!")
        print('Para votar digite o número do candidato desejado')
        print('[1] Joãozinho')
        print('[2] Pedrinho')
        print('DIGITE [OUTRO VALOR] PARA ANULAR O VOTO')
        print('------------------------------------------------\n')
        while voto != 0:
            voto = int(input("Escolha um candidato: "))
            if voto == 1:
                joaozinho.append(voto)
            elif voto == 2:
                pedrinho.append(voto)
            elif voto != 0 and voto != 1 and voto != 2:    
                nulos.append(voto)

#2 – Exibir o Relatório dos Votos - Esta rotina exibirá a lista que está com os votos preenchidos.
    
    if opcao == 2:
        print('--------------------------------------------')
        print('            RELATÓRIO DOS VOTOS             ')
        print(f'Votos do candidato Joãozinho:\n {joaozinho}')
        print(f'Votos do candidato Pedrinho:\n {pedrinho}')
        print(f'Votos Nulos:\n {nulos}')
        print('--------------------------------------------')
#3 – Efetuar a apuração | Exibir o resultado - Esta rotina contará os votos de cada candidato 
# #(e os nulos. Considere nulos todos os votos que não sejam 0, 1 ou 2) e exibirá o relatório com os votos de cada candidato e os nulos.
    
    if opcao == 3:
        candidato_1 = 0
        for i in range( len(joaozinho)):
            candidato_1 = (i + 1)
        candidato_2 = 0
        for i in range( len(pedrinho)):
            candidato_2 = (i + 1)
        nulo = 0
        for i in range( len(nulos)):
            nulo = (i + 1)
        print('\n----------------------------------------------------------')
        print('                        APURAÇÃO                          ')
        print(f'O candidato Joãozinho teve {candidato_1} votos válidos.')
        print(f'O candidato Pedrinho teve {candidato_2} votos válidos.')
        print(f'Já votos Nulos foram {nulo}.')
        print('----------------------------------------------------------\n')
#4 – Mostrar o percentual dos votos Esta rotina apresentará a quantidade de votos que cada candidato atingiu e a quantidade de votos nulos. 
# #Exibir ao lado o percentual que cada candidato (e nulos) atingiu.

    if opcao == 4:
        total_votos_validos = (candidato_1 + candidato_2 + nulo)
        percentual_1 = (candidato_1/total_votos_validos)*100
        percentual_2 = (candidato_2/total_votos_validos)*100
        percentual_nulo = (nulo/total_votos_validos)*100
        print('\n-----------------------------------------------------------------------------------')
        print('                     RESULTADO PERCENTUAL POR CANDIDATO E NULOS                    ')
        print('O candidato Joãozinho teve {} votos e uma porcentagem de {:.2f}% dos votos válidos.'.format(candidato_1,percentual_1))
        print('O candidato Pedrinho teve {} votos e uma porcentagem de  {:.2f}% dos votos válidos.'.format(candidato_2,percentual_2))
        print('A quantidade de Nulos foi {} votos com uma porcentagem de {:.2f}% dos votos válidos.'.format(nulo,percentual_nulo))
        print('-----------------------------------------------------------------------------------\n') 