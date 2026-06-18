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

print("Olá! Seja bem-vindo ao sistema de cadastro de treinamentos da empresa!")
nome = input("Qual é seu nome?(digite o nome completo): ")
setor = input("Digite o setor onde você trabalha:" "(elétrica/trabalho em altura)") 
if setor == "elétrica" :
    print("Você deve usar luvas de alta tensão e botas dielétricas")
elif setor == "trabalho em altura":
    print("Você deve usar o cinturão de segurança e talabarte")
treinamentos1 = input("Você ja realizou o treinamento NR-10? (sim/nao):")
treinamentos2 = input("Você ja realizou o treinamento NR-35? (sim/nao):")
treinamentos3 = input("Você ja realizou o treinamento da Brigada? (sim/nao):")
if treinamentos1 == "sim" and treinamentos2 == "sim" and treinamentos3 == "sim":
    brigada = int(input("Qual foi o ano que você realizou o treinamento da brigada?: "))
    ano = int(input("Qual é o ano atual?: "))
    total_anos = ano - brigada
    if total_anos >= 2:
        print("Você precisa renovar o treinamento da brigada")
    else:
        print("Seu treinamento da brigada está válido") 
        print(f"Cadastro realizado com sucesso, {nome}do setor de {setor} ")
else:
    print("Cadastro não realizado, por favor realize os treinamentos necessários")



    

