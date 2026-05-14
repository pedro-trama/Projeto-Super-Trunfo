'''
Integrantes do Grupo:
Lucas Notargiacomo Mustaro - RA: 10434914
Pedro Henrique Bettega Trama - RA: 10769933

Turma 01D - L12
'''

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
