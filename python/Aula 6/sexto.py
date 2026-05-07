# # atividade de temperatura como fazer 
# Leituras = [70,75,82,98,110,85,80]

# for temp in Leituras:
#     if temp > 100:
#         print(f"CRITICO: {temp} °C detectado! Adicionando parada de emergencia.")
#         break # o loop para aqui e não le os proximos valores (85 e 80)
#     print(f"temperatura esta em {temp} °C. Operando normal.")

#     #cenario 2
#     # Adicionar um outra condiçao para temperatura abaixo de 50 e quando chegar ate 10 parar 
   
   
#     Leituras = [70,75,82,98,110,85,80]
#     baixos = [50,55,52,30,20,15,10]
# for temp in Leituras:
#     if temp > 100:
#         print(f"CRITICO: {temp} °C detectado! Adicionando parada de emergencia.")
#         break 
#     for temp in baixos:
#         print(f"temperatura esta em {temp} °C. Operando normal.")
#     if temp <50:
#         print(f"CRITICO: {temp} °C detectado! Adicionando parada de emergencia.")
#     break 
# else:
#     print(f"temperatura esta em {temp} °C. Operaçao com valores baixo.")
# print("Chegar o sistema. Aguardando manuntenção.")

    
# materiais = ["metal", "metal", "plastico", "metal", "vidro", "metal"]
# for peças in materiais:
#     if peças != "metal:":
#         print(f"Aviso: peça de {peças} detectada.Desviando para descarte...")
#         continue #pula o restante do codigo abaixo e vai para a proxima peça 

#     # Este codigo so roda se a peça for metal
#     print(f"Aviso: peça de {peças} detectada.Desviando para descarte...")

#     print("fim de lote de produção")

    #exercico 1
    # tente criar um codigo que conte de 1 a 10, mas use o continue para não imprimir o numero 5 (simulando uma falha do sensor especifica no item 5)



# from time import sleep
# for num in range(1,11):
#     if num == 5:
#         print(f"Falha ao imprimir o nº {num}")
#         sleep(1.8)
#         continue
#     print(f"Listando números {num}")
#     sleep(2)
#     print("Fim!")

#exercicio 2
#Simule um semafaro com parada para cada cor. determine um tempo que deseja para que quando mudar para tal cor ele represente uma pausa

# from time import sleep
# for i in range(1,11):
#     sleep(0.5)
#     print("verde")
# print("siga em frente")

# from time import sleep
# for i in range(1,11):
#     sleep(0.5)
#     print("amarelo")
# print("vai fechar ou se fica ou se vai")

# from time import sleep
# for i in range(1,11):
#     sleep(0.5)
#     print("vermelho")
# print("para né pfvr")

#exercico 3 
#Uma frabrica tem 5 maquinas. Peca ao usuario (via input dentro do loop) o consumo em kwh em cada uma das 5 maquinasAo final do loop, o progama deve exibir o condumo total da maquina 

# total = 0

# for i in range(1, 6):
#     consumo = float(input(f"Digite o consumo da máquina {i} em kWh: "))
#     total += consumo

# print(f"Consumo total das máquinas: {total} kWh")

# Exercicio 4 identificador de peças defeituosas (for+if)
# percorra uma lista de medidas de peça:
# medidas = [50.1, 49.8, 52.0 , 50.0 , 48.5]
# o padrão de qualidade aceita apenas peças com exatamente 50.0  






