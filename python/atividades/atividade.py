
# 1. Perfil de Gamer: Peça o nick (nome) do jogador e o nível atual. Exiba: "O jogador [nick] está no nível [nível] e pronto para a partida!"
# 2. Calculadora de Mesada: Peça o valor que o aluno ganha por semana e multiplique por 4 para mostrar quanto ele terá no final do mês.

print("Olá jogador")
nick = (input("Qual é seu nome?:"))
nivel = (input("Qual é seu nível?:"))
print(f"O seu nome é {nick} e você esta no nivel {nivel} e pronto para a partida")
print("Bom jogo")

# 2. Calculadora de Mesada: Peça o valor que o aluno ganha por semana e multiplique por 4 para mostrar quanto ele terá no final do mês.

valormesada = float(input("digite o valor que você ganha por semana:"))
valormensal= valormesada * 4 
print(f"No final do mês,você tera o valor de {valormensal} se a caso não gastar")



