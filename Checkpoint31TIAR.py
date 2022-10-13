opcao = 4583
while opcao != 0:
    print("MENU GERENCIAL")
    print("--------------")
    print("1 - Preencher Tickets")
    print("2 - Calcular a média dos tickets")
    print("3 - Análise das medias com o ano anterior")
    print("4 - Gerar outra lista com comparações")
    print("0 - Sair")
    opcao = int(input("Digite a Opção desejada: "))

    if opcao == 1:
        # ROTINA 1 - Fazer uma rotina que permita ao usuário preencher os tickets em uma lista float
        # (Vendas) até que seja digitado o valor 0 (zero).
        # - Preencher uma lista float
        # - Condição de saída, digitar zero

        vendas = []
        ticket = 10
        print("Digite os valores dos tickets ou zero para finalizar")
        while ticket != 0:
            ticket = float(input("R$ "))
            if ticket != 0:
                vendas.append(ticket)
        print(vendas)
    elif opcao == 2:
        # ROTINA 2 - Considerando que a lista Vendas está preenchida, fazer uma rotina que calcule e
        # exiba a média dos tickets, tipo:
        # A média dos elementos é R$ 137.95
        soma = 0
        cont = 0
        for ticket in vendas:
            soma += ticket  # soma = soma + ticket
            cont += 1
        media = soma / cont
        print(f"\nA média dos elementos é R$ {media}\n")
    elif opcao == 3:
        # ROTINA 3: Compare se esta média calculada está acima da média diária do último ano (129.37),
        # exibir a mensagem “Houve evolução média dos Tickets”, senão “Não houve evolução média dos
        # tickets”. Tipo a mensagem abaixo:
        # SAÍDA:
        # A média do ano anterior foi de R$ 129.37
        # Média atual é de R$ 137.95.
        # Houve evolução média dos Tickets
        soma = 0
        cont = 0
        for ticket in vendas:
            soma += ticket  # soma = soma + ticket
            cont += 1
        media = soma / cont
        print(f"A média do ano anterior foi de...: R$ {129.37:8.2f}")
        print(f"Média atual é de.................: R$ {media:8.2f}")
        if media > 129.70:
            print(f"Houve evolução na média dos tickets")
        else:
            print(f"Não Houve evolução na média dos tickets")
    elif opcao == 4:
        # ROTINA 4 - Para cada um dos tickets armazenados na lista anterior, criar uma lista de string
        # com a mesma quantidade de elementos e armazene em cada elemento correspondente as mensagens:
        # “Superior”, “Inferior” ou “Igual” ao ticket médio
        status_tickets = []
        for ticket in vendas:
            if ticket > 129.37:
                status_tickets.append("Superior")
            elif ticket < 129.37:
                status_tickets.append("Inferior")
            else:
                status_tickets.append("Igual")
        print(vendas)
        print(status_tickets)
    elif opcao == 0:
        ...
    else:
        print("Opcao invalida, digite algo entre 0 e 4!")
