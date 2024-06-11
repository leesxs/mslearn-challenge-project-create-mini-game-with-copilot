import random

def jogar_pedra_papel_tesoura():
    opcoes = ['pedra', 'papel', 'tesoura']
    estatisticas = {'vitorias': 0, 'derrotas': 0, 'empates': 0}
    
    while True:
        computador = random.choice(opcoes)
        jogador = input("Escolha pedra, papel ou tesoura: ").lower()

        if jogador not in opcoes:
            print("Opção inválida. Tente novamente.")
            continue

        print(f"Computador escolheu {computador}")
        if jogador == computador:
            print("Empate!")
            estatisticas['empates'] += 1
        elif (jogador == "pedra" and computador == "tesoura") or \
            (jogador == "tesoura" and computador == "papel") or \
            (jogador == "papel" and computador == "pedra"):
            print("Você ganhou!")
            estatisticas['vitorias'] += 1
        else:
            print("Você perdeu!")
            estatisticas['derrotas'] += 1

        continuar = input("Deseja jogar novamente? (sim/não): ").lower()
        if continuar != "sim":
            print(f"\nEstatísticas finais:\nVitórias: {estatisticas['vitorias']}\nDerrotas: {estatisticas['derrotas']}\nEmpates: {estatisticas['empates']}\nTotal de partidas: {estatisticas['vitorias'] + estatisticas['derrotas'] + estatisticas['empates']}")
            break

jogar_pedra_papel_tesoura()