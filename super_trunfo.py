'''
Integrantes do Grupo:
Lucas Notargiacomo Mustaro - RA: 10434914
Pedro Henrique Bettega Trama - RA: 10769933

Turma 01D - L12
'''
import random

# gabarito dos atributos
# índices: 0=Nome, 1=Cilindradas, 2=Potência, 3=Torque, 4=RPM, 5=Peso 
gabarito = ["Nome", "Cilindradas", "Potência (hp)", "Torque (rpm)", "RPM", "Peso (kg)"]

# função que exibe o menu inicial
def menu_inicial(): #Opções de menu
    print("+" * 10, "SUPER TRUNFO", "+" * 10)
    print("1. Single Player")
    print("2. Multiplayer")
    print("3. Sair")

    opcao = int(input("Escolha uma opção: "))

    while opcao < 1 or opcao > 3: # Recurso de validação
        print("Opção inválida!")
        opcao = int(input("Escolha novamente: "))
    return opcao
    
# função que cria o baralho (lista de cartas)
def criar_baralho(): 

    baralho = [ 
    ["Bimota TESI 2D", 992, 92, 6000, 8000, 149],
    ["Ducati Monster", 1000, 98, 7700, 8800, 190],
    ["Yamaha Fazer 600", 600, 98, 6000, 12000, 187],
    ["BMW R 1100 S", 1085, 98, 3500, 7500, 229],
    ["Aprilia RST Futura", 1000, 10, 7500, 9500, 210],
    ["Honda Rc51", 1000, 160, 7000, 10000, 218],
    ["Kawazaki Ninja ZXR", 1200, 115, 8500, 9500, 240],
    ["Yamaha YZF-R1", 996, 130, 7500, 10500, 290],
    ["Ducati 999", 999, 124, 8000, 9500, 195],
    ["Hyosung GT 650", 650, 79, 6500, 9000, 189],
    ["Bimota Db5 Mille", 992, 92, 6500, 8500, 156],
    ["Yamaha Royal Star", 1300, 98, 4800, 6000, 366],
    ["Bimota Santamônica", 1000, 107, 7000, 9000, 236],
    ["Honda VTX 1800 Retro", 1800, 106, 3100, 5800, 290],
    ["BMW K 1200", 1200, 130, 4250, 8750, 285],
    ["Aprilia Tuono 1000", 1000, 126, 7500, 9500, 245]
    ]

    random.shuffle(baralho) # embaralha as cartas

    return baralho

def distribuir_cartas(baralho): # função que distribui as cartas entre os jogadores

    metade = len(baralho) // 2

    jogador1 = baralho[:metade]
    jogador2 = baralho[metade:]

    return jogador1, jogador2

def mostrar_carta(carta): # função que mostra a carta do topo do usuário 
    print("\n===== SUA CARTA =====")

    print(f"Nome:           {carta[0]}")
    print(f"Cilindradas:    {carta[1]}")
    print(f"Potência:       {carta[2]}")
    print(f"Torque:         {carta[3]}")
    print(f"RPM:            {carta[4]}")
    print(f"Peso:           {carta[5]}")

def escolher_atributo(): # função que escolhe o atributo da carta
    print("\nEscolha um atributo:")

    print("1. Cilindradas")
    print("2. Potência")
    print("3. Torque")
    print("4. RPM")
    print("5. Peso")

    atributo = int(input("Digite uma opção: "))

    while atributo < 1 or atributo > 5:
        atributo = int(input("Escolha inválida. Digite de 1 a 5: "))
    
    return atributo

def comparar_cartas(carta1, carta2, atributo): # função que compara as cartas dos jogadores
    if carta1[atributo] > carta2[atributo]:
        return 1
    elif carta1[atributo] < carta2[atributo]:
        return 2
    else:
        return 0

def jogar_rodada(jogador1, jogador2, descarte): # função que executa uma rodada
    carta1 = jogador1.pop(0)
    carta2 = jogador2.pop(0)

    mostrar_carta(carta1)

    atributo = escolher_atributo()

    atributos = ["", "Cilindradas", "Potência", "Torque", "RPM", "Peso"]

    print(f"\n=== CARTA DO JOGADOR 2 ===")
    print(f"Nome: {carta2[0]}")
    print(f"{atributos[atributo]}: {carta2[atributo]}")

    vencedor = comparar_cartas(carta1, carta2, atributo)

    if vencedor == 1: # vitória do jogador
        print("\nJogador 1 venceu a rodada!")
        jogador1.append(carta1)
        jogador1.append(carta2)

        if len(descarte) > 0:
            print("Jogador 1 as cartas do descarte!")
            jogador1.extend(descarte)
            descarte.clear()
    
    elif vencedor == 2: # vitória do adversário
        print("\nJogador 2 venceu a rodada!")
        jogador2.append(carta1)
        jogador2.append(carta2)

        if len(descarte) > 0:
            print("Jogador 2 ganhou as cartas do descarte!")
            jogador2.extend(descarte)
            descarte.clear()

    else: # empate
        print("\nEmpate!")
        print("As cartas vão para a pilha de descarte.")
        descarte.append(carta1)
        descarte.append(carta2)
    print("\nCartas restantes: ")
    print(f"Jogador 1: {len(jogador1)}")
    print(f"Jogador 2: {len(jogador2)}")

def single_player(): # usuário contra o computador 
    baralho = criar_baralho()
    mao_jogador1, mao_jogador2 = distribuir_cartas(baralho)
    descarte = []
    rodada = 1

    while len(mao_jogador1) > 0 and len(mao_jogador2) > 0:
        print("\n==========================")
        print(f"    {rodada}ª RODADA    ")
        print("==========================")

        jogar_rodada(mao_jogador1, mao_jogador2, descarte)

        rodada += 1

    print("\n--------------------------")
    print("        FIM DE JOGO        ")
    print("--------------------------")
    if len(mao_jogador1) > 0:
        print("Jogador 1 venceu o jogo!")

    else:
        print("Jogador 2 venceu o jogo!")
    print()
    main() # volta para o menu inicial


def multiplayer(): # usuário contra outro jogador
    baralho = criar_baralho()
    mao_jogador1, mao_jogador2 = distribuir_cartas(baralho)
    descarte = []
    rodada = 1

    while len(mao_jogador1) > 0 and len(mao_jogador2) > 0:
        print("\n--------------------------")
        print(f"    {rodada}ª RODADA    ")
        print("--------------------------")

        jogar_rodada(mao_jogador1, mao_jogador2, descarte)

        rodada += 1

    print("\n==========================")
    print("        FIM DE JOGO     ")
    print("==========================")
    if len(mao_jogador1) > 0:
        print("Vitória do Jogador 1")

    else:
        print("Vitória do Jogador 2!")
    print()
    main() # volta para o menu inicial

def sair():
    print("Saindo do jogo. Encerrando...")


def main(): # função principal

    opcao = menu_inicial()

    if opcao == 1:
        single_player()
    elif opcao == 2:
        multiplayer()
    elif opcao == 3:
        sair()

main()