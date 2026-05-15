
# Exercicio 01

# print("Olá iremos pedir seu modelo do veiculo e a sua placa")
# modelo=(input("Informe o modelo do seu veiculo: \n"))
# placa= int (input("Informe sua placa: \n"))
# print("Veiculo",modelo,"de placa",placa,"registado no sistema boa viagem!")

#exercico 02

# capacidadetanque = float(input(f"digíte a capacidade do tanque de combustivel:"))
# consumo = float(input(f"Digite o consumo da máquina:"))
# distanciatotal= (capacidadetanque / consumo ) 
# print ("O resultado é:", distanciatotal,)

# exercicio 03
# print("Leitor do frete em dolar")
# dolar= float(input(f"digite o valor em dolar:"))
# dolaratual= float(input(f"digite o valor atual do dolar:"))
# conversão = dolar * dolaratual
# print("esse e seu valor em real :",conversão)

# exercicio 04
# print("Olá entregador, vamos calcular seu tempo de entrega!")
# entrega1 = float(input(f"digite o tempo da sua primeira entrega:"))
# entrega2 = float(input(f"digite o tempo da sua segunda entrega:"))
# entrega3 = float(input(f"digite o valor da sua terceira entrega:"))
# média = (entrega1 + entrega2 + entrega3) /3
# print("Sua média de entregas por hora é:", média)

#exercicio 05

# peso=int(input("Digite seu peso dos caminhões(toneladas):"))
# if peso >=10: 
#      print("Carga leve")
# elif peso <= 25:
#      print("Carga leve")
# else:
#      print("ALERTA: Excesso do peso!")

    #exercicio 06

# destino = input("Digite o codigo do distino (N/S):")
# if destino == "N":
#      print ("Região Norte")
# elif destino == "S":
#      print ("Região sul")
# else:
#      print("Região internacional")


#exercicio 07

# crecklist = (input("crecklist concluido?(sim/não):"))
# motorista = (input("Motorista indentificado? (sim/não"))
# if crecklist == "sim" and motorista == "sim":
#     print("Saida autorizada!")
# else:
#     print("Saída não autorizada")

#exercicio 08

# entregasagendadas = (input("qual é o total de de entregas agentadas?:"))
# entregasatrasadas = (input("Qual e o total de entregas atrasadas?:"))

# if entregasagendadas > entregasatrasadas * 10:
#     print ("Necessario otimizar rotas")
# else:
#     print("Logistica eficiente")

#exercicio 09 

# pressão = int(input("digite a carga do seu peneu:"))
# if pressão <= 110:
#     print ("não esta dentro do padrão")
# elif pressão >= 100:
#     print("Naõ esta dentro do padrão")
# else:
#     print("Pressão correta")

#    10.Contagem de Embarque: Use um for para fazer uma contagem regressiva de 5
# até 1 para o fechamento do portão de embarque e finalize com "Portão Trancado!".
# 11. Somatório de Fretes (Acumulador): Use um while para pedir o valor do frete de
# vários pedidos.
# ○ O loop para quando o usuário digitar 0. No fim, mostre o faturamento total
# acumulado.

# 12.Monitoramento de Frota: Use um for para pedir a quilometragem de 5 veículos
# diferentes.
# ○ Ao final, mostre qual foi a maior quilometragem registrada.
# 13.Sistema de Rastreio: Crie um while que peça o código de acesso do rastreador
# ("track99").
# ○ Enquanto o usuário errar, diga "Acesso Negado". Ele tem 3 tentativas. Se
# esgotar, exiba "Rastreamento Bloqueado".


#exercicio 10
 
for i in range(1,6):
    print(i)
    print("Portão trancado!")

    #exercicio 11

    total = 0 
    while True:
        valor = float(input("Digite o valor do frete(0 para parar)"))
        if valor == 0:
            break
        total += valor
        print("Total faturado:", total)


        #exercicio 12


    maior = 0 
    for i in range(5):
        km = float(input("Digite a quiometragem:"))

        if km > maior:
            maior = km 

print("Maior quilometragem:", maior)


#exercicio 13
 
tentativa = 0 
while tentativa < 3 :
    codigo = input("Digite o codigo de acesso:")
if codigo == "track99":
    print("Acesso permitido")
    break

else:
    print("Acesso negado")
tentativa += 1
if tentativa == 3:
    print("Rastreamento rastreado")