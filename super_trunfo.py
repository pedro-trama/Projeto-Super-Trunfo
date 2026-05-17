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
mao_jogador1 = cartas[:8] 
mao_jogador2 = cartas[8:]

descarte = [] # pílha de descarte (caso haja empate)

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

# verificação da opção escolhida pelo usuário
while atributo_j1 < 1 or atributo_j1 > 5:
    print("Opção inválida!")
    atributo_j1 = int(input("1. Cilindradas \n" \
    "2. Potência\n" \
    "3. Torque\n" \
    "4. RPM\n" \
    "5. Peso\n" \
    "Digite uma das opções: "))