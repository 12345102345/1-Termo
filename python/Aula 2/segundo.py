# # # tipos de dados
# # # int
# # # float

# # x = 10 
# # y = 5.15

# # # numeros e valores
# # print ('10')
# # print(5.15)

# # # textos = string
# # print ("meu nome é Isabella")

# # # concatenar
# # print ("Eu gosto de progamar \n"  + "python \n ")

# # # contas
# # n1 = 10
# # n2 = 5 
# # print ("O valores são", n1 + n2 ) 

# # # Operadoes matematicos
# # # + = soma
# # # - = subtração 
# # # * = multiplicação 
# # # / = divisão 
# # # ^ = expoente 

# # # exemplo 2 
# # n1 = 20 
# # n2 = 10 
# # print ("os valores", n1 * n2)

# # # exemplo 3
# # n2=input("Digite o seu primeiro número: \n")
# # print("seu primeiro foi : \n" , n2 )

# # # exemplo 4
# # nome=input('Qual e seu nome? \n')
# # print('Seu nome é: \n', nome ) #Aqui ficaria mais completo 
# # print(nome) #Aqui mais simples 

# # # exemplo 5 
# # curso=input ('Qual é seu curso? \n')
# # print("Seu curso é \n" , curso)     

# # base = 10 
# # altura = 5
# # area = (base * altura) /2
# # print(area)

# # # esxemplo 6B 
# # # com informações

# # base = input("informe o valor da base \n"  )
# # altura = input("informe o valor da altura \n" )
# # area = (base * altura) /2
# # print ("Os calculos são" , int (area))

# # base = int(input("informe o valor da base \n"))
# # altura=int(input("Informe o valor da altura \n"))
# # area = (area * altura) /2
# # print ("Os cálculos são:" , int (area))

# # # Exercício 1
# # # criar uma calculadora com os operadores soma , subtrair
# # print ('Boas vindas a minha calcularora')


# print ("Vamos subtrair")
# n1=int(input("Informe o primeiro valor: \n"))
# n2= int (input("Informe o segundo valor: \n"))
# subtração= (n1 - n2)
# print ("valor é:", int (subtração))
 
 #exercício 2
 
# print ("Vamos calcular")
# n1=float(input("Informe o primeiro valor: \n"))
# n2=float(input("Informe o segundo valor"))
 
#continuação 
 
nome = input ("Digite seu nome")
idade = int (input("digite sua idade"))
prof = input ("Digite sua profissão")


print("teste",nome + "ola",idade)

# Tempo total em minutos
tempo = (saida - entrada) * 60

# Cliente possui TAG?
tag = input("Possui TAG? (s/n): ").lower()

# Regras de cobrança
if tempo <= 15:
    valor = 0
elif tempo <= 180:  # até 3 horas
    valor = 15
else:
    horas_extras = math.ceil((tempo - 180) / 60)
    valor = 15 + (horas_extras * 3)

# Desconto para TAG
if tag == "s":
    valor = valor * 0.90

print(f"Valor a pagar: R$ {valor:.2f}")