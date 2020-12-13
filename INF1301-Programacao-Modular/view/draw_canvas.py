from model import game_rules
from tkinter import *
from tkinter import messagebox
from functools import partial
from tkinter import filedialog
from controller import event_handler


def create_circle(x, y, r, canvasName, cor):
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return canvasName.create_oval(x0, y0, x1, y1, fill=cor)


def desenha(my_canvas, root):
    global dado, img, vez, W, H, canvas_move_peca, root_move_peca, coordenadas_caminho_principal, coordenadas_caminhos_coloridos, cores_peca, canvas_opcoes

    caminho_principal = game_rules.get_caminho_principal()

    canvas_move_peca = my_canvas
    root_move_peca = root

    casas_iniciais = game_rules.get_casas_inicais()
    caminhos_coloridos = game_rules.get_caminhos_coloridos()
    caminho_principal_abrigos = game_rules.get_caminho_principal_abrigo()
    caminho_principal_bar = game_rules.get_caminho_principal_bar()
    vez = game_rules.get_vez()

    # Variáveis
    W = 600  # x
    H = 600  # y

    coordenadas_caminho_principal = [
        [13.5 * W // 15, 8.5 * H // 15], [12.5 * W // 15, 8.5 * H // 15], [11.5 * W // 15, 8.5 * H // 15],
        [10.5 * W // 15, 8.5 * H // 15], [9.5 * W // 15, 8.5 * H // 15],  # 0 - 5

        [8.5 * W // 15, 9.5 * H // 15], [8.5 * W // 15, 10.5 * H // 15], [8.5 * W // 15, 11.5 * H // 15],
        [8.5 * W // 15, 12.5 * H // 15], [8.5 * W // 15, 13.5 * H // 15], [8.5 * W // 15, 14.5 * H // 15],  # 5  - 10

        [7.5 * W // 15, 14.5 * H // 15],  # 11

        [6.5 * W // 15, 14.5 * H // 15], [6.5 * W // 15, 13.5 * H // 15], [6.5 * W // 15, 12.5 * H // 15],
        [6.5 * W // 15, 11.5 * H // 15], [6.5 * W // 15, 10.5 * H // 15], [6.5 * W // 15, 9.5 * H // 15],  # 12 - 17

        [5.5 * W // 15, 8.5 * H // 15], [4.5 * W // 15, 8.5 * H // 15], [3.5 * W // 15, 8.5 * H // 15],
        [2.5 * W // 15, 8.5 * H // 15], [1.5 * W // 15, 8.5 * H // 15], [0.5 * W // 15, 8.5 * H // 15],  # 18 - 22

        [0.5 * W // 15, 7.5 * H // 15],  # 24

        [0.5 * W // 15, 6.5 * H // 15], [1.5 * W // 15, 6.5 * H // 15], [2.5 * W // 15, 6.5 * H // 15],
        [3.5 * W // 15, 6.5 * H // 15], [4.5 * W // 15, 6.5 * H // 15], [5.5 * W // 15, 6.5 * H // 15],
        [6.5 * W // 15, 5.5 * H // 15], [6.5 * W // 15, 4.5 * H // 15], [6.5 * W // 15, 3.5 * H // 15],
        [6.5 * W // 15, 2.5 * H // 15], [6.5 * W // 15, 1.5 * H // 15], [6.5 * W // 15, 0.5 * H // 15],
        [7.5 * W // 15, 0.5 * H // 15],
        [8.5 * W // 15, 0.5 * H // 15], [8.5 * W // 15, 1.5 * H // 15], [8.5 * W // 15, 2.5 * H // 15],
        [8.5 * W // 15, 3.5 * H // 15], [8.5 * W // 15, 4.5 * H // 15], [8.5 * W // 15, 5.5 * H // 15],
        [9.5 * W // 15, 6.5 * H // 15], [10.5 * W // 15, 6.5 * H // 15], [11.5 * W // 15, 6.5 * H // 15],
        [12.5 * W // 15, 6.5 * H // 15], [13.5 * W // 15, 6.5 * H // 15], [14.5 * W // 15, 6.5 * H // 15],
        [14.5 * W // 15, 7.5 * H // 15],
        [14.5 * W // 15, 8.5 * H // 15]
    ]

    coordenadas_casas_iniciais = [
        [  # AMARELO
            [10.5 * W // 15, 1.5 * H // 15], [13.5 * W // 15, 1.5 * H // 15], [10.5 * W // 15, 4.5 * H // 15],
            [13.5 * W // 15, 4.5 * H // 15]
        ],
        [  # VERDE
            [1.5 * W // 15, 1.5 * H // 15], [4.5 * W // 15, 1.5 * H // 15], [1.5 * W // 15, 4.5 * H // 15],
            [4.5 * W // 15, 4.5 * H // 15]
        ],
        [  # VERMELHO
            [1.5 * W // 15, 10.5 * H // 15], [4.5 * W // 15, 10.5 * H // 15], [1.5 * W // 15, 13.5 * H // 15],
            [4.5 * W // 15, 13.5 * H // 15]
        ],
        [  # AZUL
            [10.5 * W // 15, 10.5 * H // 15], [13.5 * W // 15, 10.5 * H // 15], [10.5 * W // 15, 13.5 * H // 15],
            [13.5 * W // 15, 13.5 * H // 15]
        ]
    ]

    coordenadas_caminhos_coloridos = [
        [  # VERMELHO
            [13.5 * W // 15, 7.5 * H // 15], [12.5 * W // 15, 7.5 * H // 15], [11.5 * W // 15, 7.5 * H // 15],
            [10.5 * W // 15, 7.5 * H // 15], [9.5 * W // 15, 7.5 * H // 15], [8.5 * W // 15, 7.5 * H // 15]
        ],
        [  # VERDE
            [7.5 * W // 15, 1.5 * H // 15], [7.5 * W // 15, 2.5 * H // 15], [7.5 * W // 15, 3.5 * H // 15],
            [7.5 * W // 15, 4.5 * H // 15], [7.5 * W // 15, 5.5 * H // 15], [7.5 * W // 15, 6.5 * H // 15]
        ],
        [  # AMARELO
            [1.5 * W // 15, 7.5 * H // 15], [2.5 * W // 15, 7.5 * H // 15], [3.5 * W // 15, 7.5 * H // 15],
            [4.5 * W // 15, 7.5 * H // 15], [5.5 * W // 15, 7.5 * H // 15], [6.5 * W // 15, 7.5 * H // 15]
        ],
        [  # AZUL
            [7.5 * W // 15, 13.5 * H // 15], [7.5 * W // 15, 12.5 * H // 15], [7.5 * W // 15, 11.5 * H // 15],
            [7.5 * W // 15, 10.5 * H // 15], [7.5 * W // 15, 9.5 * H // 15], [7.5 * W // 15, 8.5 * H // 15]
        ]
    ]

    coordenadas_casa_final = [
        [7.5 * W // 15, 8.5 * H // 15],  # VERDE
        [6.5 * W // 15, 7.5 * H // 15],  # AMARELO
        [7.5 * W // 15, 6.5 * H // 15],  # AZUL
        [8.5 * W // 15, 7.5 * H // 15],  # VERMELHO
    ]

    coordenadas_abrigos = [
        [8.5 * W // 15, 13.5 * H // 15],  # LADO DO VERMELHO
        [1.5 * W // 15, 8.5 * H // 15],  # LADO DO VERDE
        [6.5 * W // 15, 1.5 * H // 15],  # LADO DO AMARELO
        [13.5 * W // 15, 6.5 * H // 15],  # LADO DO VERDE
    ]

    colors = ["red", "yellow", "green", "blue"]  # lista de cores em ordem alfabetica ingles

    cores_peca = ["blue", "yellow", "green", "red"]
    white_distance = W // 16  # para os quadrados brancos dentro dos cantos coloridos

    # Corredores com cor (1o quadrado isolado colorido, depois retangulo colorido)
    my_canvas.create_rectangle(13 * W // 15, 8 * H // 15, 14 * W // 15, 9 * H // 15, fill=colors[0])
    my_canvas.create_rectangle(9 * W // 15, 7 * H // 15, 14 * W // 15, 8 * H // 15, fill=colors[0])
    my_canvas.create_rectangle(W // 15, 6 * H // 15, 2 * W // 15, 7 * H // 15, fill=colors[1])
    my_canvas.create_rectangle(W // 15, 7 * H // 15, 6 * W // 15, 8 * H // 15, fill=colors[1])
    my_canvas.create_rectangle(6 * W // 15, 13 * H // 15, 7 * W // 15, 14 * H // 15, fill=colors[2])
    my_canvas.create_rectangle(7 * W // 15, 14 * H // 15, 8 * W // 15, 9 * H // 15, fill=colors[2])
    my_canvas.create_rectangle(8 * W // 15, 1 * H // 15, 9 * W // 15, 2 * H // 15, fill=colors[3])
    my_canvas.create_rectangle(7 * W // 15, 1 * H // 15, 8 * W // 15, 6 * H // 15, fill=colors[3])

    # Triangulos brancos nas casas de saida
    my_canvas.create_polygon(8.2 * W // 15, 1.2 * H // 15, 8.5 * W // 15, 1.8 * H // 15, 8.8 * W // 15, 1.2 * H // 15,
                             fill="white")
    my_canvas.create_polygon(1.2 * W // 15, 6.2 * H // 15, 1.8 * W // 15, 6.5 * H // 15, 1.2 * W // 15, 6.8 * H // 15,
                             fill="white")
    my_canvas.create_polygon(13.8 * W // 15, 8.2 * H // 15, 13.2 * W // 15, 8.5 * H // 15, 13.8 * W // 15,
                             8.8 * H // 15,
                             fill="white")
    my_canvas.create_polygon(6.2 * W // 15, 13.8 * H // 15, 6.5 * W // 15, 13.2 * H // 15, 6.8 * W // 15,
                             13.8 * H // 15,
                             fill="white")

    # Corredores sem cor
    for i in range(1, 15):
        my_canvas.create_line(i * (W // 15), 0, i * (W // 15), H, fill="black")  # retas verticais
        my_canvas.create_line(0, i * (H // 15), W, i * (H // 15), fill="black")  # retas horizontais

    # Azul Corner (canto superior direito)
    my_canvas.create_rectangle(9 * W // 15, 9 * H // 15, W, H, fill=colors[0])
    my_canvas.create_rectangle(9 * W // 15 + white_distance, 9 * H // 15 + white_distance, W - white_distance,
                               H - white_distance, fill="white")

    # Verde Corner (canto inferior esquerdo)
    my_canvas.create_rectangle(0, 0, 6 * W // 15, 6 * H // 15, fill=colors[1])
    my_canvas.create_rectangle(0 + white_distance, 0 + white_distance, 6 * W // 15 - white_distance,
                               6 * H // 15 - white_distance,
                               fill="white")

    # Vermelho Corner (canto inferior direito)
    my_canvas.create_rectangle(0, 9 * W // 15, 6 * W // 15, H, fill=colors[2])
    my_canvas.create_rectangle(0 + white_distance, 9 * W // 15 + white_distance, 6 * W // 15 - white_distance,
                               H - white_distance,
                               fill="white")

    # Amarelo Corner (canto superior esquerdo)
    my_canvas.create_rectangle(9 * W // 15, 0, W, 6 * H // 15, fill=colors[3])
    my_canvas.create_rectangle(9 * W // 15 + white_distance, 0 + white_distance, W - white_distance,
                               6 * H // 15 - white_distance,
                               fill="white")

    # Abrigos
    # Quadrados especias (cinzas)
    my_canvas.create_rectangle(1 * W // 15, 8 * H // 15, 2 * W // 15, 9 * H // 15, fill="gray")
    my_canvas.create_rectangle(8 * W // 15, 13 * H // 15, 9 * W // 15, 14 * H // 15, fill="gray")
    my_canvas.create_rectangle(13 * W // 15, 6 * H // 15, 14 * W // 15, 7 * H // 15, fill="gray")
    my_canvas.create_rectangle(6 * W // 15, 1 * H // 15, 7 * W // 15, 2 * H // 15, fill="gray")

    # Centro colorido (4 triangulos)
    my_canvas.create_polygon(9 * W // 15, 6 * H // 15, 9 * W // 15, 9 * H // 15, W // 2, H // 2, fill=colors[0])
    my_canvas.create_polygon(6 * W // 15, 6 * H // 15, 6 * W // 15, 9 * H // 15, W // 2, H // 2, fill=colors[1])
    my_canvas.create_polygon(6 * W // 15, 9 * H // 15, 9 * W // 15, 9 * H // 15, W // 2, H // 2, fill=colors[2])
    my_canvas.create_polygon(6 * W // 15, 6 * H // 15, 9 * W // 15, 6 * H // 15, W // 2, H // 2, fill=colors[3])

    # DESENHA PEÇAS NO CAMINHO PRINCIPAL
    # percorer caminho_principal e ver se tem peca
    for index, quadrado in enumerate(caminho_principal):
        if quadrado != 0 and quadrado != -100:
            x_centro_peca = coordenadas_caminho_principal[index][0]
            y_centro_peca = coordenadas_caminho_principal[index][1]
            create_circle(x_centro_peca, y_centro_peca, W // 30, my_canvas, cores_peca[quadrado])

    # DESENHA PEÇAS NAS CASAS INICIAIS
    for casa_inicial in casas_iniciais:
        for index_peca, quadrado in enumerate(casa_inicial):
            if quadrado < 0 and quadrado != -100:
                x_centro_peca = coordenadas_casas_iniciais[quadrado][index_peca][0]
                y_centro_peca = coordenadas_casas_iniciais[quadrado][index_peca][1]
                create_circle(x_centro_peca, y_centro_peca, W // 30, my_canvas, cores_peca[quadrado])

    # DESENHA PEÇAS NAS RETAS FINAIS
    for reta_final in caminhos_coloridos:
        for index_peca, quadrado in enumerate(reta_final[:5]):
            if quadrado < 0:
                x_centro_peca = coordenadas_caminhos_coloridos[quadrado + 1][index_peca][0]
                y_centro_peca = coordenadas_caminhos_coloridos[quadrado + 1][index_peca][1]
                create_circle(x_centro_peca, y_centro_peca, W // 30, my_canvas, cores_peca[quadrado])

    # DESENHA ABRIGOS
    for index, abrigo in enumerate(caminho_principal_abrigos):
        # caso a 1a posicao do abrigo esteja vazia e a 2a ocupada
        if abrigo[0][0] == 0 and abrigo[0][1] != 0:
            cor_da_peca = abrigo[0][1]
            x_centro_peca = coordenadas_abrigos[index][0]
            y_centro_peca = coordenadas_abrigos[index][1]
            create_circle(x_centro_peca, y_centro_peca, W // 30, my_canvas, cores_peca[cor_da_peca])

        # caso a 2a posicao do abrigo esteja vazia e a 1a ocupada
        elif abrigo[0][0] != 0 and abrigo[0][1] == 0:
            cor_da_peca = abrigo[0][0]
            x_centro_peca = coordenadas_abrigos[index][0]
            y_centro_peca = coordenadas_abrigos[index][1]
            create_circle(x_centro_peca, y_centro_peca, W // 30, my_canvas, cores_peca[cor_da_peca])

        # caso as 2 posicoes dos abrigos estejam ocupadas
        elif abrigo[0][0] != 0 and abrigo[0][1] != 0:
            # desenha peça 1
            cor_da_peca_1 = abrigo[0][0]
            x_centro_peca = coordenadas_abrigos[index][0]
            y_centro_peca = coordenadas_abrigos[index][1]
            create_circle(x_centro_peca, y_centro_peca, W // 30, my_canvas, cores_peca[cor_da_peca_1])

            # desenha peça 2
            cor_da_peca_2 = abrigo[0][1]
            x_centro_peca = coordenadas_abrigos[index][0]
            y_centro_peca = coordenadas_abrigos[index][1]
            create_circle(x_centro_peca, y_centro_peca, W // 30 - 5, my_canvas, cores_peca[cor_da_peca_2])

    # DESENHA BARREIRAS
    if caminho_principal_bar:  # caso a lista não esteja vazia (ou seja, existem barreiras no tabuleiro)
        for barreira in caminho_principal_bar:
            posicao_barreira = barreira[1]
            cor_barreira = barreira[0]
            x_centro_peca = coordenadas_caminho_principal[posicao_barreira][0]
            y_centro_peca = coordenadas_caminho_principal[posicao_barreira][1]
            create_circle(x_centro_peca, y_centro_peca, W // 30, my_canvas, cores_peca[cor_barreira])
            create_circle(x_centro_peca, y_centro_peca, W // 30 - 2, my_canvas, "white")
            create_circle(x_centro_peca, y_centro_peca, W // 30 - 5, my_canvas, cores_peca[cor_barreira])

    # DESENHA PEÇA CASA FINAL
    for index, reta_final in enumerate(caminhos_coloridos):
        if reta_final[-1]:  # se tem peca na casa final
            x_texto_final = coordenadas_casa_final[index][0]
            y_texto_final = coordenadas_casa_final[index][1]
            numero_pecas_casa_final = len(reta_final[-1])
            my_canvas.create_text(x_texto_final, y_texto_final, text=numero_pecas_casa_final,
                                  font="Times 20 italic bold")

    # desabilita o botao do dado qnd o jogo acaba
    if game_rules.jogo_acabou() == True:
        dado_button["state"] = DISABLED

    # se houve captura a pessoa anda 6 com alguma peca
    if game_rules.get_houve_captura_na_jogada() == True:
        event_handler.click_joga_dado(canvas_opcoes, my_canvas, houve_captura=True)

    # se peca chegou na casa final
    if game_rules.get_chegou_peca_na_casa_final() == True:
        event_handler.click_joga_dado(canvas_opcoes, my_canvas, peca_chegou_na_casa_final=True)


def get_root():
    global root_move_peca
    return root_move_peca


def get_canvas():
    global canvas_move_peca
    return canvas_move_peca


def get_dado_button():
    global dado_button
    return dado_button


def get_salvar_jogo_button():
    global salvar_jogo_button
    return salvar_jogo_button


def desenha_1a_vez(my_canvas, root):
    global dado, img, vez, W, H, canvas_move_peca, root_move_peca, coordenadas_caminho_principal, coordenadas_caminhos_coloridos, cores_peca, canvas_opcoes, dado_button, salvar_jogo_button

    caminho_principal = game_rules.get_caminho_principal()

    canvas_move_peca = my_canvas
    root_move_peca = root

    casas_iniciais = game_rules.get_casas_inicais()
    caminhos_coloridos = game_rules.get_caminhos_coloridos()
    caminho_principal_abrigos = game_rules.get_caminho_principal_abrigo()
    caminho_principal_bar = game_rules.get_caminho_principal_bar()
    vez = game_rules.get_vez()

    # Variáveis
    W = 600  # x
    H = 600  # y

    coordenadas_caminho_principal = [
        [13.5 * W // 15, 8.5 * H // 15], [12.5 * W // 15, 8.5 * H // 15], [11.5 * W // 15, 8.5 * H // 15],
        [10.5 * W // 15, 8.5 * H // 15], [9.5 * W // 15, 8.5 * H // 15],  # 0 - 5

        [8.5 * W // 15, 9.5 * H // 15], [8.5 * W // 15, 10.5 * H // 15], [8.5 * W // 15, 11.5 * H // 15],
        [8.5 * W // 15, 12.5 * H // 15], [8.5 * W // 15, 13.5 * H // 15], [8.5 * W // 15, 14.5 * H // 15],  # 5  - 10

        [7.5 * W // 15, 14.5 * H // 15],  # 11

        [6.5 * W // 15, 14.5 * H // 15], [6.5 * W // 15, 13.5 * H // 15], [6.5 * W // 15, 12.5 * H // 15],
        [6.5 * W // 15, 11.5 * H // 15], [6.5 * W // 15, 10.5 * H // 15], [6.5 * W // 15, 9.5 * H // 15],  # 12 - 17

        [5.5 * W // 15, 8.5 * H // 15], [4.5 * W // 15, 8.5 * H // 15], [3.5 * W // 15, 8.5 * H // 15],
        [2.5 * W // 15, 8.5 * H // 15], [1.5 * W // 15, 8.5 * H // 15], [0.5 * W // 15, 8.5 * H // 15],  # 18 - 22

        [0.5 * W // 15, 7.5 * H // 15],  # 24

        [0.5 * W // 15, 6.5 * H // 15], [1.5 * W // 15, 6.5 * H // 15], [2.5 * W // 15, 6.5 * H // 15],
        [3.5 * W // 15, 6.5 * H // 15], [4.5 * W // 15, 6.5 * H // 15], [5.5 * W // 15, 6.5 * H // 15],
        [6.5 * W // 15, 5.5 * H // 15], [6.5 * W // 15, 4.5 * H // 15], [6.5 * W // 15, 3.5 * H // 15],
        [6.5 * W // 15, 2.5 * H // 15], [6.5 * W // 15, 1.5 * H // 15], [6.5 * W // 15, 0.5 * H // 15],
        [7.5 * W // 15, 0.5 * H // 15],
        [8.5 * W // 15, 0.5 * H // 15], [8.5 * W // 15, 1.5 * H // 15], [8.5 * W // 15, 2.5 * H // 15],
        [8.5 * W // 15, 3.5 * H // 15], [8.5 * W // 15, 4.5 * H // 15], [8.5 * W // 15, 5.5 * H // 15],
        [9.5 * W // 15, 6.5 * H // 15], [10.5 * W // 15, 6.5 * H // 15], [11.5 * W // 15, 6.5 * H // 15],
        [12.5 * W // 15, 6.5 * H // 15], [13.5 * W // 15, 6.5 * H // 15], [14.5 * W // 15, 6.5 * H // 15],
        [14.5 * W // 15, 7.5 * H // 15],
        [14.5 * W // 15, 8.5 * H // 15]
    ]

    coordenadas_casas_iniciais = [
        [  # AMARELO
            [10.5 * W // 15, 1.5 * H // 15], [13.5 * W // 15, 1.5 * H // 15], [10.5 * W // 15, 4.5 * H // 15],
            [13.5 * W // 15, 4.5 * H // 15]
        ],
        [  # VERDE
            [1.5 * W // 15, 1.5 * H // 15], [4.5 * W // 15, 1.5 * H // 15], [1.5 * W // 15, 4.5 * H // 15],
            [4.5 * W // 15, 4.5 * H // 15]
        ],
        [  # VERMELHO
            [1.5 * W // 15, 10.5 * H // 15], [4.5 * W // 15, 10.5 * H // 15], [1.5 * W // 15, 13.5 * H // 15],
            [4.5 * W // 15, 13.5 * H // 15]
        ],
        [  # AZUL
            [10.5 * W // 15, 10.5 * H // 15], [13.5 * W // 15, 10.5 * H // 15], [10.5 * W // 15, 13.5 * H // 15],
            [13.5 * W // 15, 13.5 * H // 15]
        ]
    ]

    coordenadas_caminhos_coloridos = [
        [  # VERMELHO
            [13.5 * W // 15, 7.5 * H // 15], [12.5 * W // 15, 7.5 * H // 15], [11.5 * W // 15, 7.5 * H // 15],
            [10.5 * W // 15, 7.5 * H // 15], [9.5 * W // 15, 7.5 * H // 15], [8.5 * W // 15, 7.5 * H // 15]
        ],
        [  # VERDE
            [7.5 * W // 15, 1.5 * H // 15], [7.5 * W // 15, 2.5 * H // 15], [7.5 * W // 15, 3.5 * H // 15],
            [7.5 * W // 15, 4.5 * H // 15], [7.5 * W // 15, 5.5 * H // 15], [7.5 * W // 15, 6.5 * H // 15]
        ],
        [  # AMARELO
            [1.5 * W // 15, 7.5 * H // 15], [2.5 * W // 15, 7.5 * H // 15], [3.5 * W // 15, 7.5 * H // 15],
            [4.5 * W // 15, 7.5 * H // 15], [5.5 * W // 15, 7.5 * H // 15], [6.5 * W // 15, 7.5 * H // 15]
        ],
        [  # AZUL
            [7.5 * W // 15, 13.5 * H // 15], [7.5 * W // 15, 12.5 * H // 15], [7.5 * W // 15, 11.5 * H // 15],
            [7.5 * W // 15, 10.5 * H // 15], [7.5 * W // 15, 9.5 * H // 15], [7.5 * W // 15, 8.5 * H // 15]
        ]
    ]

    coordenadas_casa_final = [
        [7.5 * W // 15, 8.5 * H // 15],  # VERDE
        [6.5 * W // 15, 7.5 * H // 15],  # AMARELO
        [7.5 * W // 15, 6.5 * H // 15],  # AZUL
        [8.5 * W // 15, 7.5 * H // 15],  # VERMELHO
    ]

    coordenadas_abrigos = [
        [8.5 * W // 15, 13.5 * H // 15],  # LADO DO VERMELHO
        [1.5 * W // 15, 8.5 * H // 15],  # LADO DO VERDE
        [6.5 * W // 15, 1.5 * H // 15],  # LADO DO AMARELO
        [13.5 * W // 15, 6.5 * H // 15],  # LADO DO VERDE
    ]

    # colors = ["blue", "green", "red", "yellow"]  # lista de cores em ordem alfabetica ingles
    colors = ["red", "yellow", "green", "blue"]  # lista de cores em ordem alfabetica ingles

    cores_peca = ["blue", "yellow", "green", "red"]
    white_distance = W // 16  # para os quadrados brancos dentro dos cantos coloridos

    # Corredores com cor (1o quadrado isolado colorido, depois retangulo colorido)
    my_canvas.create_rectangle(13 * W // 15, 8 * H // 15, 14 * W // 15, 9 * H // 15, fill=colors[0])
    my_canvas.create_rectangle(9 * W // 15, 7 * H // 15, 14 * W // 15, 8 * H // 15, fill=colors[0])
    my_canvas.create_rectangle(W // 15, 6 * H // 15, 2 * W // 15, 7 * H // 15, fill=colors[1])
    my_canvas.create_rectangle(W // 15, 7 * H // 15, 6 * W // 15, 8 * H // 15, fill=colors[1])
    my_canvas.create_rectangle(6 * W // 15, 13 * H // 15, 7 * W // 15, 14 * H // 15, fill=colors[2])
    my_canvas.create_rectangle(7 * W // 15, 14 * H // 15, 8 * W // 15, 9 * H // 15, fill=colors[2])
    my_canvas.create_rectangle(8 * W // 15, 1 * H // 15, 9 * W // 15, 2 * H // 15, fill=colors[3])
    my_canvas.create_rectangle(7 * W // 15, 1 * H // 15, 8 * W // 15, 6 * H // 15, fill=colors[3])

    # Triangulos brancos nas casas de saida
    my_canvas.create_polygon(8.2 * W // 15, 1.2 * H // 15, 8.5 * W // 15, 1.8 * H // 15, 8.8 * W // 15, 1.2 * H // 15,
                             fill="white")
    my_canvas.create_polygon(1.2 * W // 15, 6.2 * H // 15, 1.8 * W // 15, 6.5 * H // 15, 1.2 * W // 15, 6.8 * H // 15,
                             fill="white")
    my_canvas.create_polygon(13.8 * W // 15, 8.2 * H // 15, 13.2 * W // 15, 8.5 * H // 15, 13.8 * W // 15,
                             8.8 * H // 15,
                             fill="white")
    my_canvas.create_polygon(6.2 * W // 15, 13.8 * H // 15, 6.5 * W // 15, 13.2 * H // 15, 6.8 * W // 15,
                             13.8 * H // 15,
                             fill="white")

    # Corredores sem cor
    for i in range(1, 15):
        my_canvas.create_line(i * (W // 15), 0, i * (W // 15), H, fill="black")  # retas verticais
        my_canvas.create_line(0, i * (H // 15), W, i * (H // 15), fill="black")  # retas horizontais

    # Azul Corner (canto superior direito)
    my_canvas.create_rectangle(9 * W // 15, 9 * H // 15, W, H, fill=colors[0])
    my_canvas.create_rectangle(9 * W // 15 + white_distance, 9 * H // 15 + white_distance, W - white_distance,
                               H - white_distance, fill="white")

    # Verde Corner (canto inferior esquerdo)
    my_canvas.create_rectangle(0, 0, 6 * W // 15, 6 * H // 15, fill=colors[1])
    my_canvas.create_rectangle(0 + white_distance, 0 + white_distance, 6 * W // 15 - white_distance,
                               6 * H // 15 - white_distance,
                               fill="white")

    # Vermelho Corner (canto inferior direito)
    my_canvas.create_rectangle(0, 9 * W // 15, 6 * W // 15, H, fill=colors[2])
    my_canvas.create_rectangle(0 + white_distance, 9 * W // 15 + white_distance, 6 * W // 15 - white_distance,
                               H - white_distance,
                               fill="white")

    # Amarelo Corner (canto superior esquerdo)
    my_canvas.create_rectangle(9 * W // 15, 0, W, 6 * H // 15, fill=colors[3])
    my_canvas.create_rectangle(9 * W // 15 + white_distance, 0 + white_distance, W - white_distance,
                               6 * H // 15 - white_distance,
                               fill="white")

    # Abrigos
    # Quadrados especias (cinzas)
    my_canvas.create_rectangle(1 * W // 15, 8 * H // 15, 2 * W // 15, 9 * H // 15, fill="gray")
    my_canvas.create_rectangle(8 * W // 15, 13 * H // 15, 9 * W // 15, 14 * H // 15, fill="gray")
    my_canvas.create_rectangle(13 * W // 15, 6 * H // 15, 14 * W // 15, 7 * H // 15, fill="gray")
    my_canvas.create_rectangle(6 * W // 15, 1 * H // 15, 7 * W // 15, 2 * H // 15, fill="gray")

    # Centro colorido (4 triangulos)
    my_canvas.create_polygon(9 * W // 15, 6 * H // 15, 9 * W // 15, 9 * H // 15, W // 2, H // 2, fill=colors[0])
    my_canvas.create_polygon(6 * W // 15, 6 * H // 15, 6 * W // 15, 9 * H // 15, W // 2, H // 2, fill=colors[1])
    my_canvas.create_polygon(6 * W // 15, 9 * H // 15, 9 * W // 15, 9 * H // 15, W // 2, H // 2, fill=colors[2])
    my_canvas.create_polygon(6 * W // 15, 6 * H // 15, 9 * W // 15, 6 * H // 15, W // 2, H // 2, fill=colors[3])

    # DESENHA PEÇAS NO CAMINHO PRINCIPAL
    # percorer caminho_principal e ver se tem peca
    for index, quadrado in enumerate(caminho_principal):
        if quadrado != 0 and quadrado != -100:
            x_centro_peca = coordenadas_caminho_principal[index][0]
            y_centro_peca = coordenadas_caminho_principal[index][1]
            create_circle(x_centro_peca, y_centro_peca, W // 30, my_canvas, cores_peca[quadrado])

    # DESENHA PEÇAS NAS CASAS INICIAIS
    for casa_inicial in casas_iniciais:
        for index_peca, quadrado in enumerate(casa_inicial):
            if quadrado < 0 and quadrado != -100:
                x_centro_peca = coordenadas_casas_iniciais[quadrado][index_peca][0]
                y_centro_peca = coordenadas_casas_iniciais[quadrado][index_peca][1]
                create_circle(x_centro_peca, y_centro_peca, W // 30, my_canvas, cores_peca[quadrado])

    # DESENHA PEÇAS NAS RETAS FINAIS
    for reta_final in caminhos_coloridos:
        for index_peca, quadrado in enumerate(reta_final[:5]):
            if quadrado < 0:
                x_centro_peca = coordenadas_caminhos_coloridos[quadrado + 1][index_peca][0]
                y_centro_peca = coordenadas_caminhos_coloridos[quadrado + 1][index_peca][1]
                create_circle(x_centro_peca, y_centro_peca, W // 30, my_canvas, cores_peca[quadrado])

    # DESENHA ABRIGOS
    for index, abrigo in enumerate(caminho_principal_abrigos):
        # caso a 1a posicao do abrigo esteja vazia e a 2a ocupada
        if abrigo[0][0] == 0 and abrigo[0][1] != 0:
            cor_da_peca = abrigo[0][1]
            x_centro_peca = coordenadas_abrigos[index][0]
            y_centro_peca = coordenadas_abrigos[index][1]
            create_circle(x_centro_peca, y_centro_peca, W // 30, my_canvas, cores_peca[cor_da_peca])

        # caso a 2a posicao do abrigo esteja vazia e a 1a ocupada
        elif abrigo[0][0] != 0 and abrigo[0][1] == 0:
            cor_da_peca = abrigo[0][0]
            x_centro_peca = coordenadas_abrigos[index][0]
            y_centro_peca = coordenadas_abrigos[index][1]
            create_circle(x_centro_peca, y_centro_peca, W // 30, my_canvas, cores_peca[cor_da_peca])

        # caso as 2 posicoes dos abrigos estejam ocupadas
        elif abrigo[0][0] != 0 and abrigo[0][1] != 0:
            # desenha peça 1
            cor_da_peca_1 = abrigo[0][0]
            x_centro_peca = coordenadas_abrigos[index][0]
            y_centro_peca = coordenadas_abrigos[index][1]
            create_circle(x_centro_peca, y_centro_peca, W // 30, my_canvas, cores_peca[cor_da_peca_1])

            # desenha peça 2
            cor_da_peca_2 = abrigo[0][1]
            x_centro_peca = coordenadas_abrigos[index][0]
            y_centro_peca = coordenadas_abrigos[index][1]
            create_circle(x_centro_peca, y_centro_peca, W // 30 - 5, my_canvas, cores_peca[cor_da_peca_2])

    # DESENHA BARREIRAS
    if caminho_principal_bar:  # caso a lista não esteja vazia (ou seja, existem barreiras no tabuleiro)
        for barreira in caminho_principal_bar:
            posicao_barreira = barreira[1]
            cor_barreira = barreira[0]
            x_centro_peca = coordenadas_caminho_principal[posicao_barreira][0]
            y_centro_peca = coordenadas_caminho_principal[posicao_barreira][1]
            create_circle(x_centro_peca, y_centro_peca, W // 30, my_canvas, cores_peca[cor_barreira])
            create_circle(x_centro_peca, y_centro_peca, W // 30 - 2, my_canvas, "white")
            create_circle(x_centro_peca, y_centro_peca, W // 30 - 5, my_canvas, cores_peca[cor_barreira])

    # DESENHA PEÇA CASA FINAL
    for index, reta_final in enumerate(caminhos_coloridos):
        if reta_final[-1]:  # se tem peca na casa final
            x_texto_final = coordenadas_casa_final[index][0]
            y_texto_final = coordenadas_casa_final[index][1]
            numero_pecas_casa_final = len(reta_final[-1])
            my_canvas.create_text(x_texto_final, y_texto_final, text=numero_pecas_casa_final,
                                  font="Times 20 italic bold")

    # CANVAS DE OPÇÕES
    canvas_opcoes = Canvas(height=200)
    canvas_opcoes.pack(side=RIGHT)
    canvas_opcoes.create_text(200, 20, text="À JOGAR:")

    # BOTÕES
    dado_button = Button(root, text="Lançar Dado", activeforeground="cyan", activebackground="dark cyan")
    dado_button["command"] = partial(event_handler.click_joga_dado,
                                     canvas_ops=canvas_opcoes,
                                     canvas_tabuleiro=my_canvas)  # maneira de passar parametros (canvas_ops no caso) no evento do click
    dado_button.place(x=762, y=400)

    novo_jogo_button = Button(root, text="Novo Jogo", activeforeground="cyan", activebackground="dark cyan",
                              command=event_handler.click_novo_jogo)
    novo_jogo_button.place(x=762, y=30)

    carregar_jogo_button = Button(root, text="Carregar Jogo", activeforeground="cyan", activebackground="dark cyan",
                                  command=event_handler.carrega_arquivo)
    carregar_jogo_button.place(x=762, y=80)

    salvar_jogo_button = Button(root, text="Salvar", activeforeground="cyan", activebackground="dark cyan",
                                command=event_handler.salva_arquivo
                                )
    salvar_jogo_button.place(x=762, y=130)

    # BOTÕES PARA ESOLHER O VALOR DO DADO
    um_no_dado = Button(root, text="Dado=1", activeforeground="cyan", activebackground="dark cyan")
    um_no_dado["command"] = partial(event_handler.dado_vale_1,
                                    canvas_ops=canvas_opcoes,
                                    canvas_tabuleiro=my_canvas)  # maneira de passar parametros (canvas_ops no caso) no evento do click
    um_no_dado.place(x=720, y=460)

    dois_no_dado = Button(root, text="Dado=2", activeforeground="cyan", activebackground="dark cyan")
    dois_no_dado["command"] = partial(event_handler.dado_vale_2,
                                      canvas_ops=canvas_opcoes,
                                      canvas_tabuleiro=my_canvas)  # maneira de passar parametros (canvas_ops no caso) no evento do click
    dois_no_dado.place(x=720, y=500)

    tres_no_dado = Button(root, text="Dado=3", activeforeground="cyan", activebackground="dark cyan")
    tres_no_dado["command"] = partial(event_handler.dado_vale_3,
                                      canvas_ops=canvas_opcoes,
                                      canvas_tabuleiro=my_canvas)  # maneira de passar parametros (canvas_ops no caso) no evento do click
    tres_no_dado.place(x=720, y=540)

    quatro_no_dado = Button(root, text="Dado=4", activeforeground="cyan", activebackground="dark cyan")
    quatro_no_dado["command"] = partial(event_handler.dado_vale_4,
                                        canvas_ops=canvas_opcoes,
                                        canvas_tabuleiro=my_canvas)  # maneira de passar parametros (canvas_ops no caso) no evento do click
    quatro_no_dado.place(x=820, y=460)

    cinco_no_dado = Button(root, text="Dado=5", activeforeground="cyan", activebackground="dark cyan")
    cinco_no_dado["command"] = partial(event_handler.dado_vale_5,
                                       canvas_ops=canvas_opcoes,
                                       canvas_tabuleiro=my_canvas)  # maneira de passar parametros (canvas_ops no caso) no evento do click
    cinco_no_dado.place(x=820, y=500)

    seis_no_dado = Button(root, text="Dado=6", activeforeground="cyan", activebackground="dark cyan")
    seis_no_dado["command"] = partial(event_handler.dado_vale_6,
                                      canvas_ops=canvas_opcoes,
                                      canvas_tabuleiro=my_canvas)  # maneira de passar parametros (canvas_ops no caso) no evento do click
    seis_no_dado.place(x=820, y=540)


def desenha_quadrado(my_canvas, pos_peca, tipo_de_casa, cor_de_mudanca=None):
    global coordenadas_caminho_principal, vez
    raio = W // 30
    x_canto_sup = coordenadas_caminho_principal[pos_peca][0] - raio
    y_canto_sup = coordenadas_caminho_principal[pos_peca][1] - raio
    x_canto_inf = coordenadas_caminho_principal[pos_peca][0] + raio
    y_canto_inf = coordenadas_caminho_principal[pos_peca][1] + raio
    if tipo_de_casa == "CASA NORMAL":
        my_canvas.create_rectangle(x_canto_inf, y_canto_inf, x_canto_sup, y_canto_sup, fill="white")

    elif tipo_de_casa == "ABRIGO" or tipo_de_casa == "BARREIRA":
        x_peca = coordenadas_caminho_principal[pos_peca][0]
        y_peca = coordenadas_caminho_principal[pos_peca][1]
        create_circle(x_peca, y_peca, r=raio, canvasName=my_canvas, cor=cor_de_mudanca)


def limpa_tabuleiro(my_canvas, root):
    # redesenha o tabuleiro limpo
    my_canvas.create_rectangle(0, 0, 600, 600, fill="white")
    desenha(my_canvas, root)
