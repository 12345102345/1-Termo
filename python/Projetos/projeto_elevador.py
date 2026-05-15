
#requisitos funcionais
#  O elevador deve se mover para cima e para baixo 
#  O elevador deve se dirigir no andar que a pessoa escolheu
#  O elevador deve informaas açoes
# O programa deve permitir várias chamadas do elevador.
# O sistema deve encerrar apenas quando o usuário escolher sair.
# Requisitos Não Funcionais

# O sistema deve ser fácil de usar.
# As mensagens exibidas devem ser claras.
# O programa deve responder rapidamente aos comandos.
# O sistema não deve permitir mais de 5 pessoas no elevador.
# O sistema não deve permitir andares menores que 0.
# O sistema não deve permitir andares maiores que 10.
# O programa deve funcionar continuamente até o usuário encerrar.
# O sistema deve evitar erros de entrada inválida.
# O código deve ser organizado e fácil de manter.



# Sistema de Elevador de predio 
# O predio possui 10 andares.sendo o terrio o andar 0.O elevador pode se mover para cima ou para baixo,e tem a capacidade de trasportar até 5 pessoas.
# o elevador começa a andar 0 e pode ser chamado de por qualqer pessoa andar
# O elevador deve ser mover para andar onde a pessoa chamou, e depois para andar destino da pessoa 
# O elevador deve abrir mensagens indicando o andar atual, o numero de pessoas do elevador, e as ações realizadas (subindo descendo,parando)
# O progama deve continuar rodando até que o ususario descida encerrar 
#o elevador deve impedir que mais de 5 pessoas entrem, e deve impedir que o elevador se mova para andares menores que 0 ou maiores que 10


import time
capacidade_pessoas = 5
andar = 0
andar_maximo = 10
andar_minimo = 0
while True:
        print("Elevador no andar:", andar)
    
        print ("O limite de pessoas no elevador é de 5 pessoas, certifique que está dentro do limite de pessoas")
        opção = input("Tem até 5 pessoas no elevador? (sim/nao): ")
    
        if opção == "sim":
            print("ok esta dentro do padrão")

        elif opção == "nao":
            print("por favor sair pessoas para segurança de todos")

        chamada = int(input("Qual andar você quer chamar (0,10)? "))
    
        if andar < chamada:
            for subir in range(chamada):
                 andar = andar + 1
                 time.sleep(1.0)
                 print("Subindo... Andar", andar)
            


        else: 
            andar > chamada
            for descer in range(chamada):
             andar = andar - 1
            print("Descendo... Andar", andar)
            time.sleep(2.0)
            print("Parou no andar", andar)

        destino = int(input("Qual o andar de destino? "))

   
        if andar < destino:
            for subir in range(destino):
                andar = andar + 1
                time.sleep(2.0)
                print("Subindo... Andar", andar)
            
    
        else:
            andar > destino
            for descer in range(destino):
                andar = andar - 1
                print("Descendo... Andar", andar)
                time.sleep(2.0)
            print("Chegou no destino:", andar)
