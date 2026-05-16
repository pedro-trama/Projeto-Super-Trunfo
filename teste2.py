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
mao_jogador1 = cartas[:2] 
mao_jogador2 = cartas[2:]

descarte = [] # pilha de descarte (em caso de empate)

# exibe a primeira carta do jogador 1 (nome e atributos)
print(f"Nome:           {mao_jogador1[0][0]}")
print(f"Cilindradas:    {mao_jogador1[0][1]}")
print(f"Potência (hp):  {mao_jogador1[0][2]}")
print(f"Torque (rpm):   {mao_jogador1[0][3]}")
print(f"RPM:            {mao_jogador1[0][4]}")
print(f"Peso (kg):      {mao_jogador1[0][5]}")
print()
atributo_jog1 = int(input("Digite qual atributo deseja: \n" \
"1. Cilindradas\n" \
"2. Potência\n" \
"3. Torque\n" \
"4. RPM\n" \
"5. Peso\n"))

while len(mao_jogador1) != 0:
    # se o atributo do jogador 1 for maior do que o do jogador 2
    if mao_jogador1[0][atributo_jog1] > mao_jogador2[0][atributo_jog1]:
        mao_jogador1.append(mao_jogador2[0])
        mao_jogador2.pop(0)
        print("Jogador 1 venceu a rodada")
    # se o atributo do jogador 2 for maior do que o do jogador 1
    elif mao_jogador1[0][atributo_jog1] < mao_jogador2[0][atributo_jog1]:
        mao_jogador2.append(mao_jogador1[0])
        mao_jogador1.pop(0)
        print("Jogador 2 venceu a rodada")