# Boas-vindas
print('Bem-Vindo sistema de cobrança de serviços de uma copiadora de Marcus Vinicius de Araujo Torres\n')

# Função para escolher o serviço desejado
def escolha_servico():
    while True:
        servico = input("Escolha o serviço desejado:\n"
                        "DIG - Digitalização\n"
                        "ICO - Impressão colorida\n"
                        "IPB - Impressão preto e branco\n"
                        "FOT - Fotocópia\n").upper()

        if servico in ['DIG', 'ICO', 'IPB', 'FOT']:
            return servico
        else:
            print("Opção inválida. Escolha entre DIG, ICO, IPB ou FOT.")

# Função para obter o número de páginas com desconto
def num_pagina():
    while True:
        try:
            num_paginas = int(input("Informe o número de páginas: "))
            if num_paginas > 10000:
                print("O número de páginas não pode ser superior a 10.000.")
            else:
                return num_paginas
        except ValueError:
            print("Digite um valor numérico válido.")

# Função para escolher serviço adicional
def servico_extra():
    while True:
        opcao = input("Escolha um serviço adicional\n"
                      "1 - Encadernação simples\n"
                      "2 - Encadernação capa dura\n"
                      "0 - Para nenhum: \n")
        if opcao in ['1', '2', '0']:
            return opcao
        else:
            print("Opção inválida. Escolha entre 1, 2 ou 0 para nenhum serviço adicional.")

# Função principal
def main():
    # Boas-vindas
    print("Bem-vindo! Sou o assistente de impressão.")

    # Escolha do serviço
    servico = escolha_servico()

    # Número de páginas com desconto
    num_paginas = num_pagina()

    # Serviço adicional
    servico_adicional = servico_extra()

    # Cálculo do total a pagar
    preco_base = 0
    if servico == 'DIG':
        preco_base = 0.1
    elif servico == 'ICO':
        preco_base = 1.0
    elif servico == 'IPB':
        preco_base = 0.40
    elif servico == 'FOT':
        preco_base = 0.20

    total = preco_base * num_paginas

    # desconto de 0%
    if num_paginas < 10:
        total = total * 1

    # desconto de 10%
    elif num_paginas >= 10 and num_paginas < 100:
        desconto = 10
        total = total-(total * desconto / 100)

    # desconto de 15%
    elif num_paginas >= 100 and num_paginas < 1000:
        desconto = 15
        total = total - (total * desconto / 100)

    # desconto de 20%
    else:
        num_paginas >= 1000 and num_paginas < 10000
        desconto = 20
        total = total - (total * desconto / 100)

    #serviço adicional
    if servico_adicional == '1':
        servico1 = total + 10
        print('total a pagar R${:.2f}, serviço adicional: {}, quantidade de paginas: {}, extra: {}'
              .format(servico1, servico_adicional, num_paginas-desconto, num_paginas*desconto/100))

    elif servico_adicional == '2':
        servico2 = total + 25
        print('total a pagar R${:.2f}, serviço adicional: {}, quantidade de paginas: {}, extra: {}'
              .format(servico2, servico_adicional, num_paginas-desconto, num_paginas*desconto/100))

    else:
        print('total a pagar R${:.2f}, quantidade de paginas: {}, extra: {}'
              .format(total, num_paginas-desconto, num_paginas*desconto/100))


if __name__ == "__main__":
    main()
