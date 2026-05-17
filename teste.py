# super trunfo de motos - apenas 6 cartas (testes)
import random

lista = [
    ["Hyosung GT 150", 650, 79, 6500, 9000, 189],
    ["Bimota Santamonica", 1000, 107, 7000, 9000, 236],
    ["Aprilia Tuono 1000", 1000, 126, 7500, 9500, 245],
    ["Bimota Db5 Mille", 992, 92, 6500, 8500, 156],
    ["BMW K 1200", 1200, 130, 4250, 8750, 285],
    ["Yamaha Royal Star", 1300, 98, 4800, 6000, 366]
]

cartas = random.sample(lista, k=len(lista)) # embaralha as cartas do jogo

# divide a lista e distribui as cartas para cada jogador (sem repetições)
mao_jogador1 = cartas[:3] 
mao_jogador2 = cartas[3:]

descarte = [] # pilha de descarte (caso haja empate)

print(f"Nome:           {mao_jogador1[0][0]}")
print(f"Cilindradas:    {mao_jogador1[0][1]}")
print(f"Potência (hp):  {mao_jogador1[0][2]}")
print(f"Torque (rpm):   {mao_jogador1[0][3]}")
print(f"RPM:            {mao_jogador1[0][4]}")
print(f"Peso (kg):      {mao_jogador1[0][5]}")
print()
atributo_j1 = int(input("1. Cilindradas \n" \
"2. Potência\n" \
"3. Torque\n" \
"4. RPM\n" \
"5. Peso\n" \
"Digite uma das opções: "))

def distribuir_cartas(baralho): # distribui as cartas entre os jogadores
    qtd_cartas = len(lista)
    cartas_player1 = qtd_cartas // 2
    cartas_player2 = qtd_cartas // 2
    cartas = random.sample(baralho, k=qtd_cartas)
    deck_player1 = cartas[:cartas_player1]
    deck_player2 = cartas[cartas_player2:]
    return deck_player1, deck_player2
    


def single_player(): # usuário contra o computador 
    distribuir_cartas(lista)



# função que exibe o menu inicial e as opções
def menu_inicial():
    print("+" * 10, "SUPER TRUNFO", "+" * 10)
    print("Opções: \n")
    print("1. Single Player")
    print("2. Multiplayer")
    print("3. Sair\n")
    opcao = int(input("Selecione uma opção: "))

    while opcao < 1 or opcao > 3:
        print("Opção inválida!")
        opcao = int(input("Selecione uma opção: "))
    
    if opcao == 1:
        print("Você escolheu: Single Player")
    elif opcao == 2:
        print("Você escolheu: Multiplayer")
    elif opcao == 3:
        print("Você escolheu: Sair\n Encerrando...")


menu_inicial() # função que executa o menu inicial do jogo