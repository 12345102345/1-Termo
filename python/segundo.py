#1.  O laço "for" (repetiçoes determinadas)
#Use o "for" quando voçê sabe exatamentre quantas vezes algo deve acontecer (como ler 10 sensores ou processar uma lista de peças).
#Exemplo: Relatorio de produção díaria 
#Imagine que voçê tem uma meta de produzir 5 lotes e quer numerar cada um: 

# #exemplo 1 
# for lote in range(1,6):
#     print(f"Processando lote númerico {lote}...")
#     print("Qualidade verificada. [OK]")
#     print("Produção do dia finalizada")

#     # Imagine que você queira atingir  uma meta de prudução de carros e númeralos 
#     for carros in range (1,6):
#         print ("Produção de carros díaria {carros}...")

#         #Exemplo 2
#         #Contar até 4
#         for i in range (5)
#         print (i)

        #exemplo de 3
# pecas = ["Engrenagem", "Eixo", "Rolamento", "Parafuso" "Martelo"]
# tipospecas = ["Barra dentada", "Porca do Eixo" , "Anel Externo", "Parafuso phillips" , "Martelo cabeça chata"]

# for item in pecas:
#  print(f"Item em estoque: {item} + {tipospecas}")
#   # ou 
# for tipos in tipospecas:
#   print(f"Minha lista de pecas {tiposdepecas}")

  #exemplo 4 
  #Imagine a segunte situaçao gostaria de ter um menu onde pudesse perguntar qual opção você deseja e a partir de seleção ele listar os produtos 

#   print ("Loja de peças da isabella")
#   print("Bem-vindo ao nosso sistema")
#   print ("escolha uma das opçoes")
#   print ("1 - peças")
#   print("2 -  tipos de peças")


#   opcao = int(inbut("Digite sua opcao de pesquisa:"))

#   if opcao ==1:
#    for item in pecas:
#     print(f"Item em estoque: {item}")
#     print ("Fim da lista")
#   elif opcao ==2:
#    for item in pecas:
#     print(f"Item em estoque: {Item2}")
#     print("Fim da lista")
 
 #Exercicio 1 
#  1. contador de produção (for)
# uma esteira processa 10 peças por ciclo. Crie um progama que use um for para conta de 1 a 10 e, para cada número,
#  imprima: "peça n X processada com sucesso". No final,
# exiba "Ciclo de produção concluido"

# for ciclo in range(1,11):
#  print(f"peça nº {ciclo} processando com sucesso...")

 #exercico 2 
 #Imagine a produção de frutas em uma feira. Desejo apresentar as frutas 10 bananas, 5 mangas, 10 melancias e 13 abacaxi.


# for banana in range(1,11):
#     print(f" quantidade de bananas {banana} processando com sucesso...")
 
# for manga in range(1,6):
#     print(f" quantidade de mangas {manga} processando com sucesso...")

# for melancia in range(1,11):
#     print(f" quantidade de melancias {melancia} processando com sucesso...")
 
# for abacaxi in range(1,14):
#     print(f" quantidade de abacaxi {abacaxi} processando com sucesso...")


#exercico 3
#Montar uma tabuada inicialmente pode ser usado com um valor fixo e depois usar a pergunta 
# numero = int(input("digite o valor"))

# print(f"tabuada do {numero}:")
# for tabuada in range(1,11):
#     resultado =("numero * {tabuada} = {resultado}")

    # 2. O laço while (repetiçãp indeterminadas)
    #     use o while quando não sabe quando vai parar. Ele depende de uma condição (como um sensor de segurança ou um botão de emergencia).
    #     exemplo: monitor de temperatura (loop infinito controlado)

    #     repete enquanto a temperatura estiver segura 
    #     inicio 

# import time 
# temperatura= 25
# while temperatura <= 40:
#     print (f"temperatyra atual: {temperatura} °C. Sistema Operando...")
#     time.sleep(2)
#     temperatura +- 3 #Simulando o aquecimento da maquina
#     print ("ALERTA! temperatura atindiu o limite.desligando o motor...")

# exemplo : menu de Interação 
# opcao = ""
    
# while opcao != "sair" and "SAIR":
#     opcao = input("Digite a leitura do sensor ou 'sair'para fechar:").lower()
# if opcao != "sair"and "SAIR":
#     print(f"dado'{opcao}'registrando no banco de dados.")
# print("sistema encerrado.") 


# and e or 
# and comparaçoes verdadeiras e iguais
# or comparaçoes verdadeiras e não iguais 

# Exercico 5
# monitor de pressão critica (while)
# crie um simulador onde o usuario deve digitar a pressaão
# atual de um compressor.
# enquanto a pressão for menor que 100 psi, o progama continua pedindo a nova leitura
#     Assim que o usuario digitar um valor maior pu igual a 100, o loop para de exibir a mensagem: "ALERTA": pressão critica atingida 
# !
# desligando o sistema

pressao = int(input("digite o valor da pressao"))
while pressao <=100:
    print(f"temperatyra atual: {pressao} °C Sistem operando...")
    time.sleep(2)
print ("ALERTA! temperatura atindiu o limite.desligando o motor...")

# exercicio 5 
# criar um menu de opçoes com 4 itens ex: escolher series 
# apresente sua escolha de series das outras três. 
# qualquer opçao diferente sair do menu






