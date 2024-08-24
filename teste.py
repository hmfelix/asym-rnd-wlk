from matplotlib import pyplot as plt
import random as rnd
import statistics as stats


# funcao que realiza uma caminhada aleatoria
# e retorna a sequencia de passos realizados
def caminhada(q = 1/2, s_0 = 0, inf = -15, sup = 8):
    # q eh a probabilidade de A doar para B
    # s_0 eh a posicao inicial
    # inf eh a posicao em que A vai a falencia
    # sup eh a posicao em que B vai a falencia

    # condicoes iniciais
    s = s_0
    t = 0
    
    # variavel que registra os passos percorridos
    seq_passos = []

    # loop da caminhada
    while s > inf and s < sup:
        if rnd.random() <= q:
            s -= 1
        else:
            s += 1
        seq_passos.append(s)
        t += 1

    return seq_passos




# funcao que realiza uma sequencia de caminhadas aleatórias
# e retorna a seq_passos (resultado da funcao caminhada)
# de cada caminhada
def seq_caminhadas(n, q = 1/2):
    # n eh o numero de sequencias a serem geradas
    # q eh a probabilidade de A doar para B
    #   (argumento passado a funcao caminhada)
    caminhadas = []

    # loop da funcao
    for i in range(n):
        caminhadas.append(caminhada(q = q))

    return caminhadas




# funcao que plota uma sequencia de caminhadas
def plot_caminhadas(caminhadas):
    #
    
    #
    for caminhada in caminhadas:
        plt.plot(caminhada)

    plt.ylim(-17,10)
    plt.axhline(y=-15, color='r', linestyle='--')
    plt.axhline(y=8, color='r', linestyle='--')
    plt.show()
    plt.close()




# funcao que resume as estatisticas basicas de
# uma sequencia de caminhadas
def resumo_caminhadas(caminhadas):
    #

    #
    N = len(caminhadas)
    tempos = []
    jogadores = []

    #
    for caminhada in caminhadas:
        T = len(caminhada) # tempo total
        ultimo = caminhada[-1] # indica qual jogador faliu (-15 = jogador A, 8 = jogador B)
        tempos.append(T)
        jogadores.append(ultimo)
    
    #
    tempos_A = [tempos[indice] for indice, jogador in enumerate(jogadores) if jogador == -15]
    tempos_B = [tempos[indice] for indice, jogador in enumerate(jogadores) if jogador == 8]
    T_med_A = sum(tempos_A) / len(tempos_A)
    T_med_B = sum(tempos_B) / len(tempos_B)


    resultado = {
        "N": N,
        "T_max": max(tempos),
        "T_min": min(tempos),
        "T_med": stats.mean(tempos),
        "P(A)": jogadores.count(-15) / N,
        "P(B)": jogadores.count(8) / N,
        "T_med_A": T_med_A,
        "T_med_B": T_med_B
    }

    return resultado



plot_caminhadas(seq_caminhadas(15, q=0.514))

resumo_caminhadas(seq_caminhadas(100000, q=0.6))

q = 0.499999
p = 1 - q
P_A = ( (p/q)**8 - 1 )  /  ( (p/q)**23 - 1 )
P_A
T = ( -15*P_A + 8*(1 - P_A) )  /  ( 2*p - 1 )
T

# caso q = 1/2
q=1/2
p = 1 - q
P_A_sim = 8/23
T_sim = ( -15*P_A_sim + 8*(1 - P_A_sim) )
T_sim