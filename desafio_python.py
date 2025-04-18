# Aluna: Alex Vitoria Louveira Garcia
# DATA: 08/04/2025

# Bootcamp: Suzano - Python Developer - Desafio: Criando um Sistema Bancário com Python
# Estruturas de decisão e repetição (if, while);
# Manipulação de variáveis e entrada de dados;
# Criação e organização de funções;
# Utilização de boas práticas de codificação;

# O sistema permite ao usuário:

# Depositar valores em sua conta;
# Sacar valores, respeitando um limite de valor: R$500 e quantidade de saques diários: 3 saques;
# Visualizar o extrato bancário, com o histórico de operações e saldo atual;
# Encerrar o sistema com segurança;

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu).strip().lower()

    if not opcao:
        continue 

    elif opcao == "d":
        valor = input("Informe o valor do depósito: ").strip()

        if not valor.replace(".", "", 1).isdigit():
            print("Operação falhou! Valor inválido.")
            continue

        valor = float(valor)
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("Depósito realizado com sucesso!")
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = input("Informe o valor do saque: ").strip()

        if not valor.replace(".", "", 1).isdigit():
            print("Operação falhou! Valor inválido!")
            continue

        valor = float(valor)

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente!")
        
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite!")
       
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido!")
      
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print("Saque realizado com sucesso!")
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n=================== EXTRATO ====================")

        if not extrato:
            print("Não foram realizadas movimentações.")
        else:
            print(extrato)
        
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=================================================")

    elif opcao == "q":
        print("Obrigado por usar o sistema bancário!")
        break

    else:
        print("Operação inválida. Tente novamente!")