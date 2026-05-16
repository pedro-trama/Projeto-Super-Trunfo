'''
Integrantes do Grupo:
Lucas Notargiacomo Mustaro - RA: 10434914
Pedro Henrique Bettega Trama - RA: 10769933

Turma 01D - L12
'''
import random

baralho = [ # lista de cartas
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
    ["Aprilia Tuono 1000", 1000, 126, 7500, 9500, 245],

]

cartas = random.sample(baralho, k=len(baralho)) # embaralha as cartas do jogo

# divide a lista e distribui as cartas para cada jogador (sem repetições)
mao_jogador1 = cartas[:3] 
mao_jogador2 = cartas[3:]

descarte = [] # pílha de descarte (caso haja empate)

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
