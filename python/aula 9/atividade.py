# #atividade 1 
 
# #probelma de idade 01 ..................................... 
# #problema errado 
# # idade = input("Digite sua idade:")
# # if idade >=18:
# #      print("Você é maior de idade.")

# #correção 
# idade = int(input("Digite sua idade:"))
# if idade >=18:
#     print("Você e maior de idade")
# else:
#      print("Você e menor de idade")

# #A escrita fiel 02 .....................................
# #problema errado
# # nome = "Mariana"
# # print("seja bem-vinda,nome!")

# #correção
# nome = "Mariana"
# print("seja bem-vinda", nome)

# #falta de Espaço 03 .....................................
# #problema errado
# # numero =10
# # if numero >5:
# #      print("O número é maior que cinco.")
# # else:
# #      print("O número é menor ou igual a cinco.")

# #correção
# numero = float(input("digite o numero"))
# if numero >5:
#      print("O número é maior que cinco.")
# else:
#      print("O número é menor ou igual a cinco.")

# #esquecimento fatal 04 .....................................
# #problema errado
# # usuario = "aluno123"
# # if usuario == "aluno123"
# #     print("login realizado com sucesso.")

# #correção
# usuario = "aluno123"
# if usuario == "aluno123":
#     print("login realizado com sucesso.")

# # Atribuição vs. Comparação 05 .....................................
# #problema errado
# # clima = "ensolarado"
# # if clima = "chuvoso":
# # print("Leve um guarda-chuva!")

# #correção
# clima = "ensolarado"
# if clima == "chuvoso":
#      print("Leve um guarda-chuva!")


# # Misturando Alhos com Bugalhos 06  .....................................
# #problema errado
# # pontos = 50
# # print("Parabéns! Você fez " + pontos + " pontos.")

# #correção
# pontos =50
# print(f"Parabéns! Você fez",pontos," pontos.")

# #A Ordem dos Fatores 07 .....................................
# #problema errado

# # O sistema deve dar "Excelente" para notas 9 ou 10.
# # nota = 9.5
# # if nota >= 7:
# #  print("Aprovado")
# # elif nota >= 9:
# #  print("Excelente!")

# # correção
# nota = 9.5
# if nota >= 9:
#      print("Excelente!")
# elif nota >= 7:
#           print("Aprovado")  


# # O Contador de 1 a 5 08.....................................
# #problema errado
# # for i in range(5):
# # print(i)

#   #correção
# for i in range(1,6):
#      print(i)


# # O Loop Eterno 09.....................................
# #problema errado
# # tentativas = 1
# # while tentativas <= 3:
# #      print("Tentando conectar...")

# #correção
# import time
# tentativas = 1
# while tentativas <= 3:
#      time.sleep(1)
#      tentativas += 1
#      print("Tentando conectar...")
    
# A Senha Teimosa 10.....................................
#problema errado
# senha = ""
# while senha == "python123":
#      senha = input("Digite a senha secreta: ")
# print("Acesso concedido!")

#correção

# senha = ""
# while senha != "python123":
#      senha = input("Digite a senha secreta: ")
# print("Acesso concedido!")