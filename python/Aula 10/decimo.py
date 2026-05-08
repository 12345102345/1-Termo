
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
while True:
    import time
    vaga = 500
    tag_vaga = 50
    print("Seja bem vindo ao shopping center")
    print("Selecione sua vaga")
    print("Opção 1 = Entrada via Ticket")
    print("Opção 2 = Entrada via Tag")
    opção = (input("Opção:"))
    time.sleep(1.0)
    if opção == "1":
            print("Você escolheu a opção vaga via tictek.")
            vaga__via_tictek = -1
            time.sleep(1.5)
            print("Verificando se há vagas diponiveis...")
            time.sleep(1.5)
            entrada = float(input("Digite a hora da entrada:"))
            saida = float(input("Digite o horario de saída:"))
            print("Calculando o tempo de saída...")
            time.sleep(1.5)
            print("Imprimindo seu ticket ")
            time.sleep(2.0)
            print("Tenha um bom passeio")
            tempo = (saida - entrada)
            resposta = input("Você pagou? (sim/não): ")
            if resposta == "não":
                print("Pagamento não realizado volte e faça seu pagamento!\nSe houve perda do ticket será cobrado uma taxa de R$50.00")
            if resposta == "sim":
                print("Pagamento confirmado!")
                time.sleep(1.5)
                if tempo <= 0.15:
                    valor = 0
                    time.sleep(1.5)
                    print("Você ficou menos que 15 min, não há custo")
                elif tempo <= 3:
                    valor = 15
                    time.sleep(2.0)
                    print("Você pagou 15,00")
                elif tempo >3:
                    valor_sem_extra = 15
                    valor_adicional = 3
                    pagamento =(tempo - 3)*valor_adicional
                    valor_total = pagamento + valor_sem_extra
                    time.sleep(1.5)
                    print("Você pagará:",valor_total,)
                time.sleep
                print("Volte sempre!")
    elif opção == "2":
        print("Você escolheu vaga via tag.")
        time.sleep(0.5)
        tag_vaga = -1
        print("O valor será descontado em seu cartão \n Liberando cancela...")



