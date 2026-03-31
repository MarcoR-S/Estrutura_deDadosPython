pontos_minimos = (0, 1000, 3000, 6000, 10000)
niveis = ("Iniciante", "Bronze", "Prata", "Ouro", "Lendário")
faixa = 0
pontos = float(input("[PONTUAÇÃO]: "))

for i in range(len(pontos_minimos)):
    if pontos > pontos_minimos[i]:
        faixa = i

niveis = niveis[faixa]
print(niveis) 
