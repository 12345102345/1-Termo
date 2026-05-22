# 1. Utilizar tomada de decisão para elaboração do algoritmo
# 2. Utilizar estruturas condicionais para executar instruções com base em uma
# condição
# 3. Criar estruturas de repetição para executar um conjunto de instruções várias
# vezes
# 4. Aplicar operadores lógicos para avaliar e combinar condições booleanas
# 5. Utilizar lógica de programação para a resolução de problemas


# Armazene o nome, setor e o status dos treinamentos (NR-10, NR-35 e
# Brigada).


# Verificação de EPI (NR-6):
# ○ O sistema deve receber o setor do funcionário.
# ○ Se o setor for "Elétrica", liste a obrigatoriedade de luvas de alta tensão e
# botas dielétricas.
# ○ Se o setor for "Trabalho em Altura", liste o cinturão de segurança e
# # talabarte.

print("Ola, seja bem-vindo ao sistema de cadastro de treinamentos da empresa!")
nome = input("Qual é seu nome? ( digite o nome completo ) ")
setor = input("Digite o setor onde você trabalha:" "(eletrica/Trabalho em altura)")
eletrica = print("você deve usar luvas de alta tensão e botas dielétricas")
trabalho_altura = print("você deve usar liste o cinturão de segurança e talabarte")
treinamentos = input("você ja realizou algum dos treinamento a seguir? (NR-10, NR-35 e Brigada) (responda com sim ou nao)")

if treinamentos == "sim":
    print("ok!")
    treinamento_realizado = input("Qual foi o treinamento realizado?")
    print("verificando os dados cadastrados...")
    opcao = input("você você possui mais de 2 anos de treinamento? (sim/não)")
    if opcao == "sim":
        print("Treinamento vencido! encaminhar para reciclagem.")

if opcao == "nao" :
    print("Treinamento Valido")

    


opcao = "nao"