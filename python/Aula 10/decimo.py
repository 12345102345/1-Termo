
# Levantamento de requisitos
# 1.	Requisitos Funcionais (RF) Eles representam as ações que o sistema precisa desempenhar.
# Controle de Vagas: O sistema acompanhará o total de 500 vagas, diferenciando o acesso por esgotamento de lotação.
# Entrada via TAG: Detectar Tags ativas e autorizar a entrada automática ignorando a lotação tradicional (reservado para VIP/Mensalistas).
# Entrada via Ticket: Gerar ticket com timestamp somente se houver vagas (vagas ocupadas< 500).
# Cálculo Estadia: Basear o preço no tempo
# Taxa pela Aplicação: Dê um desconto de 10% automaticamente para usuários TAG. -Penalidade por Sumir com o Ticket: Curso de R$ 50,00 se você perder os registros dele.
# RF07 Validação de Saída: Abrir a cancela de saída somente após com câmbio do pagamento no sistema.
# 2.	Requisitos Não Funcionais (RNF) eles representariam propriedades e constrangimentos para o sistema.
# Disponibilidade: O sistema deve funcionar 24/7, pois o controle das cancelas não deve falhar com carros no pátio.
# Performance: O tempo de processamento entre a leitura da TAG/botão e a abertura da cancela não pode ultrapassar 2 segundos.
# Segurança: Um log de todas as entradas e saídas deve ser gravado no banco de dados para fins de auditoria financeira. - Confiança: Senha de vagas deve ser sincronizado em tempo para a segurança, a fim de garantir que dois carros não tomaram a última vaga ao mesmo tempo


# O estacionamento possui um total de 500 vagas.
# O sistema deve manter um contador de vagas ocupadas. Se o estacionamento estiver lotado, a
# cancela de entrada não deve abrir para novos clientes (exceto para quem possui Tag de Acesso
# Rápido, pois estes têm vagas reservadas).

vaga_sem_reserva = 500
print("seja bem vindo ao shopping center")
print("selecione sua vaga")
print("opção 1 = venho sem reserva")
print("opção 2 = vaga_sem_reserva")

opção = (input("Opção:"))
if opção == "1":
    print("Você escolheu vaga sem reserva.")
    vaga_sem_reserva = -1
    print("Verificando se a vagas diponiveis...")
    entrada = int(input("dígite a hora da estrada:"))
    saida = int(input("Dígite o horario de saída:"))
    print("Calculando o tempo de saída...")
print("imprimindo seu ticket ")
print("tenha um bom passeio")


tempo = (saida - entrada)
if tempo <= 0.15:
    valor = 0
    print("voçê ficou somente 15 min não a custo")
elif tempo <= 3:
    valor = 15
    print("você pagará 15,00")

else:
    valor_mais_Extra = 15
    valor_adicional = 3
   
    pagamento =(tempo + 3)
valor_total = (valor_mais_Extra * valor_adicional)
print("você pagará:",valor_total,)
print("Volte sempre")
resposta = input("Você pagou? (sim/não): ")
if resposta == "sim":
    print("Pagamento confirmado!")
elif resposta == "nao":
    print("pagamento realizado não liberado!")

elif:
opção == "2"

print("Você escolheu vaga com reserva.")
print("Sua vaga esta reservada")
entrada_vip = int(input("dígite o horario de entrada!:"))
saída_vip = int(input("Dígite o horario de saída:"))
print("muito obrigada o valor a ser pago sera descontado no seu ticket")
ticket = 0 
