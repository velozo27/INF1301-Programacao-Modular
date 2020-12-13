from model import game_rules
from view import draw_canvas
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askdirectory, asksaveasfilename
import ast

H = 600
W = 600
cores_peca = ["blue", "yellow", "green", "red"]
esperando_jogada = False


def clica(e):
    global dado, canvas_move_peca, root_move_peca, cores_peca, vez, seis_count, esperando_jogada, dado_button

    caminho_prin = game_rules.get_caminho_principal()
    pos_peca = calcula_posicao_tabuleiro(e.x, e.y)
    seis_count = game_rules.get_seis_count()
    canvas_move_peca = draw_canvas.get_canvas()
    root_move_peca = draw_canvas.get_root()
    if type(pos_peca) is not tuple:  # se for tupla, peca está na casa final
        if pos_peca != None and tem_peca_na_posicao(pos_peca) == True:
            if cor_da_peca_na_posicao_clicada_igual_a_vez(pos_peca, vez) == True:  # so pode mexer peca da cor da vez
                game_rules.move_peca(vez=vez, dado=dado, pos_atual_caminho_principal=pos_peca)

                # verifica o que fica na casa que a peca saiu
                tipo_de_casa = qual_tipo_de_casa(pos_peca)

                if tipo_de_casa == "CASA NORMAL":
                    draw_canvas.desenha_quadrado(canvas_move_peca, pos_peca, tipo_de_casa)
                if tipo_de_casa == "ABRIGO":
                    cor_de_mudanca = qual_outra_cor_abrigo(pos_peca)
                    draw_canvas.desenha_quadrado(canvas_move_peca, pos_peca, tipo_de_casa,
                                                 cor_de_mudanca=cores_peca[cor_de_mudanca])
                if tipo_de_casa == "BARREIRA":
                    draw_canvas.desenha_quadrado(canvas_move_peca, pos_peca, tipo_de_casa,
                                                 cor_de_mudanca=cores_peca[vez])
                draw_canvas.desenha(canvas_move_peca, root_move_peca)

                if dado != 6:
                    vez = game_rules.vez_do_proximo()
                else:
                    game_rules.muda_6_count()
                    if seis_count == 2:
                        game_rules.seis_tres_vezes_seguidas()
                        vez = game_rules.vez_do_proximo()
                        draw_canvas.limpa_tabuleiro(canvas_move_peca, root_move_peca)
                        draw_canvas.desenha(canvas_move_peca, root_move_peca)

            # permite apertar o botao de lancar o dado
            dado_button = draw_canvas.get_dado_button()
            dado_button["state"] = NORMAL

            salvar_jogo_button = draw_canvas.get_salvar_jogo_button()
            salvar_jogo_button["state"] = NORMAL


    elif type(pos_peca) is tuple:  # peça está na reta final
        game_rules.move_peca(vez=pos_peca[-1], dado=dado, pos_atual_reta_final=pos_peca[0])

        draw_canvas.desenha(canvas_move_peca, root_move_peca)

        dado_button = draw_canvas.get_dado_button()
        dado_button["state"] = NORMAL

        salvar_jogo_button = draw_canvas.get_salvar_jogo_button()
        salvar_jogo_button["state"] = NORMAL

        # Passando a vez para o proximo
        vez = game_rules.vez_do_proximo()

    # MOSTRA QUEM GANHOU
    if game_rules.verifica_vitoria():
        list_vencedor = game_rules.verifica_vitoria()
        draw_canvas.messagebox.showinfo("{} GANHOU".format(cores_peca[list_vencedor[0]].upper()),
                                        "1o - {}\n2o - {}\n3o - {}\n4o - {}".format(
                                            cores_peca[list_vencedor[0]].upper(),
                                            cores_peca[list_vencedor[1]].upper(),
                                            cores_peca[list_vencedor[2]].upper(),
                                            cores_peca[list_vencedor[3]].upper()))


def get_esperando_jogada():
    global esperando_jogada
    return esperando_jogada


def cor_da_peca_na_posicao_clicada_igual_a_vez(pos_peca, vez):
    caminho_prin = game_rules.get_caminho_principal()
    lista_abrigos = game_rules.get_caminho_principal_abrigo()
    # caso nao seja abrigo

    if caminho_prin[pos_peca] != 0 and caminho_prin[pos_peca] != -100:
        if caminho_prin[pos_peca] == vez:
            return True
    # caso seja abrigo
    elif caminho_prin[pos_peca] == -100:
        mapea_pos_abrigo_index_lista_abrigos = {9: 0, 22: 1, 35: 2, 48: 3}
        for peca in lista_abrigos[mapea_pos_abrigo_index_lista_abrigos[pos_peca]][0]:
            if peca == vez:
                return True
    return False


def qual_outra_cor_abrigo(pos):
    # retorna a cor da peca que nao vai sair do abrigo
    caminho_principal_abrigo = game_rules.get_caminho_principal_abrigo()
    if pos == 9:
        abrigo = caminho_principal_abrigo[0][0]
    elif pos == 22:
        abrigo = caminho_principal_abrigo[1][0]
    elif pos == 35:
        abrigo = caminho_principal_abrigo[2][0]
    else:
        abrigo = caminho_principal_abrigo[3][0]
    if vez == abrigo[0]:
        return abrigo[1]
    return abrigo[0]


def qual_tipo_de_casa(pos):
    global caminho_principal
    caminho_principal_bar = game_rules.get_caminho_principal_bar()
    abrigos_posicoes = [9, 22, 35, 48]
    casas_saida = [0, 13, 26, 39]
    if pos in abrigos_posicoes:
        return "ABRIGO"
    if pos in caminho_principal_bar:
        return "BARREIRA"
    if pos in casas_saida:
        return "CASA DE SAIDA"
    return "CASA NORMAL"


def tem_peca_na_posicao(pos_peca):
    caminho_prin = game_rules.get_caminho_principal()
    lista_abrigos = game_rules.get_caminho_principal_abrigo()
    # verifica casa normal
    if caminho_prin[pos_peca] != 0 and caminho_prin[pos_peca] != -100:
        return True

    elif caminho_prin[pos_peca] == -100:
        mapea_pos_abrigo_index_lista_abrigos = {9: 0, 22: 1, 35: 2, 48: 3}
        for index, abrigo in enumerate(lista_abrigos):
            if abrigo[1] == pos_peca:
                for peca in lista_abrigos[mapea_pos_abrigo_index_lista_abrigos[pos_peca]][0]:
                    if peca != 0:
                        return True

    return False


def calcula_posicao_tabuleiro(x, y):
    # retorna o valor da posicao da peca no caminho principal
    global W, H, coordenadas_caminhos_coloridos
    for i in range(5):  # pos 0 - 5    i = 0,1,2,3,4
        if y in range(8 * H // 15, 9 * H // 15):
            if x in range(14 * W // 15 - i * W // 15, 9 * W // 15 + (4 - i) * W // 15, -1):
                return i

    for i in range(6):  # pos 6 - 11    i = 0,1,2,3,4,5,6
        if x in range(8 * W // 15, 9 * W // 15):
            if y in range(360 + i * 40, 600 - (5 - i) * 40, 1):
                return i + 5

    # pos 11
    if x in range(7 * W // 15, 8 * W // 15) and y in range(14 * H // 15, H):
        return 11

    for i in range(6):  # pos 12 - 17    i = 0,1,2,3,4,5,6
        if x in range(6 * W // 15, 7 * W // 15):
            if y in range(600 - i * 40, 360 + (5 - i) * 40, -1):
                return i + 12

    for i in range(6):  # pos 18 - 23
        if y in range(8 * H // 15, 9 * H // 15):
            if x in range(240 - i * 40, (5 - i) * 40, -1):
                return i + 18

    # pos 24
    if x in range(0, W // 15) and y in range(7 * H // 15, 8 * H // 15):
        return 24

    for i in range(6):  # pos 25 - 30
        if y in range(6 * H // 15, 7 * H // 15):
            if x in range(i * 40, (i + 1) * 40, 1):
                return i + 25

    for i in range(6):  # pos 31 - 36
        if x in range(6 * W // 15, 7 * W // 15):
            if y in range(240 - i * 40, 240 - (1 + i) * 40, -1):
                return i + 31

    # pos 37
    if x in range(7 * W // 15, 8 * W // 15) and y in range(0, H // 15):
        return 37

    for i in range(6):  # pos 38 - 43
        if x in range(8 * W // 15, 9 * W // 15):
            if y in range(i * 40, (i + 1) * 40, 1):
                return i + 38

    for i in range(6):  # pos 44 - 49
        if y in range(6 * W // 15, 7 * W // 15):
            if x in range(360 + i * 40, 360 + (i + 1) * 40, 1):
                return i + 44

    # pos 50
    if x in range(14 * W // 15, W) and y in range(7 * H // 15, 8 * H // 15):
        return 50

    # pos 51
    if x in range(14 * W // 15, W) and y in range(8 * H // 15, 9 * H // 15):
        return 51

    # MAPEAMENTO DO
    # CAMINHO PRINCIPAL TERMINA AQUI

    for i in range(5):  # pos na reta final vermelha    i = 0,1,2,3,4
        if y in range(7 * H // 15, 8 * H // 15):
            if x in range(14 * W // 15 - i * W // 15, 9 * W // 15 + (4 - i) * W // 15, -1):
                return (i + 990, -1)

    for i in range(5):  # pos na reta final verde    i = 0,1,2,3,4
        if x in range(7 * W // 15, 8 * W // 15):
            if y in range(560 - i * 40, 360 + (4 - i) * 40, -1):
                return (i + 990, -2)

    for i in range(5):  # pos na reta final amarela    i = 0,1,2,3,4
        if y in range(7 * H // 15, 8 * H // 15):
            if x in range(W // 15 + i * W // 15, 6 * W // 15 - (4 - i) * W // 15, 1):
                return (i + 990, -3)

    for i in range(5):  # pos na reta final azul    i = 0,1,2,3,4
        if x in range(7 * W // 15, 8 * W // 15):
            if y in range(40 + i * 40, 80 + i * 40, 1):
                return (i + 990, -4)

    return None


def click_joga_dado(canvas_ops, canvas_tabuleiro, houve_captura=False, peca_chegou_na_casa_final=False):
    global vez, my_canvas, dado, seis_count, dado_button, esperando_jogada

    dado_button = draw_canvas.get_dado_button()
    salvar_jogo_button = draw_canvas.get_salvar_jogo_button()
    canvas_move_peca = draw_canvas.get_canvas()
    root_move_peca = draw_canvas.get_root()

    dado = game_rules.joga_dado()

    # BLOQUEIA O BOTÃO DE LANÇAR O DADO ATE MEXER UMA PEÇA
    vez = game_rules.get_vez()
    if game_rules.tem_pecas_no_tabuleiro(vez):
        dado_button["state"] = DISABLED
        salvar_jogo_button["state"] = DISABLED

    vez = game_rules.get_vez()

    # desenha cor de fundo do dado
    cores_peca = ["blue", "yellow", "green", "red"]
    canvas_ops.create_rectangle(150, 80, 240, 160, fill=cores_peca[vez])

    dado = game_rules.joga_dado()

    # se houve captura a pessoa joga de novo com 6 no dado
    if houve_captura == True or peca_chegou_na_casa_final == True:
        dado = 6
        houve_captura == False
        game_rules.muda_houve_captura_para_falso()
        canvas_tabuleiro.bind("<Button-1>", clica)

    if dado != 5:
        esperando_jogada = True

    label_img = Label()
    label_img.config(image='')

    if dado == 1:
        label_img.image = PhotoImage(file="dado_1.png")
    elif dado == 2:
        label_img.image = PhotoImage(file="dado_2.png")
    elif dado == 3:
        label_img.image = PhotoImage(file="dado_3.png")
    elif dado == 4:
        label_img.image = PhotoImage(file="dado_4.png")
    elif dado == 5:
        label_img.image = PhotoImage(file="dado_5.png")
    else:
        label_img.image = PhotoImage(file="dado_6.png")

    a = label_img.image
    label_img.config(image="")
    label_img.image = a
    canvas_ops.create_image(180, 100, image=label_img.image, anchor=NW)

    # se tirou 6 no dado
    seis_count = game_rules.get_seis_count()
    if dado == 6:
        if seis_count < 3:
            seis_count += 1
            canvas_tabuleiro.bind("<Button-1>", clica)
        else:
            game_rules.seis_tres_vezes_seguidas()
            vez = game_rules.vez_do_proximo()
            draw_canvas.limpa_tabuleiro(canvas_move_peca, root_move_peca)
            draw_canvas.desenha(canvas_move_peca, root_move_peca)

    # se dado for 5 mover peca pra casa de saida
    if dado == 5:
        # pode mover para casa de saida
        if game_rules.pode_mover_casa_saida(vez) == True:
            game_rules.tirou_5_no_dado(vez)
            vez = game_rules.vez_do_proximo()

            root_move_peca = draw_canvas.get_root()

            dado_button["state"] = NORMAL  # ativo o botao do dado novamente

            draw_canvas.desenha(canvas_tabuleiro, root_move_peca)

        # nao pode mover para casa de saída e nao tem peca no tabuleiro
        elif game_rules.tem_pecas_no_tabuleiro(vez) == False:
            vez = game_rules.vez_do_proximo()

        # nao pode mover para casa de saída, mas tem peça no tabuleiro
        else:
            canvas_tabuleiro.bind("<Button-1>", clica)

    # TIROU UM NUMERO DIFERENTE DE 5 E NÃO TEM PEÇAS NO TABULEIRO PARA MOVER
    elif game_rules.tem_pecas_no_tabuleiro(vez) == False:
        vez = game_rules.vez_do_proximo()

    else:
        canvas_tabuleiro.bind("<Button-1>", clica)


def dado_vale_1(canvas_ops, canvas_tabuleiro):
    global vez, my_canvas, dado
    vez = game_rules.get_vez()
    # desenha cor de fundo do dado
    cores_peca = ["blue", "yellow", "green", "red"]
    canvas_ops.create_rectangle(150, 80, 240, 160, fill=cores_peca[vez])
    dado = 1
    label_img = Label()
    label_img.config(image='')
    label_img.image = PhotoImage(file="dado_1.png")
    a = label_img.image
    label_img.config(image="")
    label_img.image = a
    canvas_ops.create_image(180, 100, image=label_img.image, anchor=NW)
    if game_rules.tem_pecas_no_tabuleiro(vez) == False:
        vez = game_rules.vez_do_proximo()
    else:
        canvas_tabuleiro.bind("<Button-1>", clica)


def dado_vale_2(canvas_ops, canvas_tabuleiro):
    global vez, my_canvas, dado
    vez = game_rules.get_vez()
    # desenha cor de fundo do dado
    cores_peca = ["blue", "yellow", "green", "red"]
    canvas_ops.create_rectangle(150, 80, 240, 160, fill=cores_peca[vez])
    dado = 2
    label_img = Label()
    label_img.config(image='')
    label_img.image = PhotoImage(file="dado_2.png")
    a = label_img.image
    label_img.config(image="")
    label_img.image = a
    canvas_ops.create_image(180, 100, image=label_img.image, anchor=NW)
    if game_rules.tem_pecas_no_tabuleiro(vez) == False:
        vez = game_rules.vez_do_proximo()
    else:
        canvas_tabuleiro.bind("<Button-1>", clica)


def dado_vale_3(canvas_ops, canvas_tabuleiro):
    global vez, my_canvas, dado
    vez = game_rules.get_vez()
    cores_peca = ["blue", "yellow", "green", "red"]
    canvas_ops.create_rectangle(150, 80, 240, 160, fill=cores_peca[vez])
    dado = 3
    label_img = Label()
    label_img.config(image='')
    label_img.image = PhotoImage(file="dado_3.png")
    a = label_img.image
    label_img.config(image="")
    label_img.image = a
    canvas_ops.create_image(180, 100, image=label_img.image, anchor=NW)
    if game_rules.tem_pecas_no_tabuleiro(vez) == False:
        vez = game_rules.vez_do_proximo()
    else:
        canvas_tabuleiro.bind("<Button-1>", clica)


def dado_vale_4(canvas_ops, canvas_tabuleiro):
    global vez, my_canvas, dado
    vez = game_rules.get_vez()
    cores_peca = ["blue", "yellow", "green", "red"]
    canvas_ops.create_rectangle(150, 80, 240, 160, fill=cores_peca[vez])
    dado = 4
    label_img = Label()
    label_img.config(image='')
    label_img.image = PhotoImage(file="dado_4.png")
    a = label_img.image
    label_img.config(image="")
    label_img.image = a
    canvas_ops.create_image(180, 100, image=label_img.image, anchor=NW)
    if game_rules.tem_pecas_no_tabuleiro(vez) == False:
        vez = game_rules.vez_do_proximo()
    else:
        canvas_tabuleiro.bind("<Button-1>", clica)


def dado_vale_5(canvas_ops, canvas_tabuleiro):
    global vez, my_canvas, root_move_peca, dado
    vez = game_rules.get_vez()
    cores_peca = ["blue", "yellow", "green", "red"]
    canvas_ops.create_rectangle(150, 80, 240, 160, fill=cores_peca[vez])
    dado = 5
    label_img = Label()
    label_img.config(image='')
    label_img.image = PhotoImage(file="dado_5.png")
    a = label_img.image
    label_img.config(image="")
    label_img.image = a
    canvas_ops.create_image(180, 100, image=label_img.image, anchor=NW)

    if dado == 5:
        if game_rules.pode_mover_casa_saida(vez) == True:
            game_rules.tirou_5_no_dado(vez)
            vez = game_rules.vez_do_proximo()
            canvas_tabuleiro = draw_canvas.get_canvas()
            root_move_peca = draw_canvas.get_root()
            draw_canvas.desenha(canvas_tabuleiro, root_move_peca)
        # nao pode mover para casa de saída e nao tem peca no tabuleiro
        # elif game_rules_certo_tlvz.tem_pecas_na_casaInicial(vez) == False:
        elif game_rules.tem_pecas_no_tabuleiro(vez) == False:
            vez = game_rules.vez_do_proximo()
        # nao pode mover para casa de saída, mas tem peça no tabuleiro
        else:
            canvas_tabuleiro.bind("<Button-1>", clica)

    elif game_rules.tem_pecas_no_tabuleiro(vez) == False:
        vez = game_rules.vez_do_proximo()

    else:
        canvas_tabuleiro.bind("<Button-1>", clica)


def dado_vale_6(canvas_ops, canvas_tabuleiro):
    global vez, my_canvas, dado
    vez = game_rules.get_vez()
    cores_peca = ["blue", "yellow", "green", "red"]
    canvas_ops.create_rectangle(150, 80, 240, 160, fill=cores_peca[vez])
    dado = 6
    label_img = Label()
    label_img.config(image='')
    label_img.image = PhotoImage(file="dado_6.png")
    a = label_img.image
    label_img.config(image="")
    label_img.image = a
    canvas_ops.create_image(180, 100, image=label_img.image, anchor=NW)

    seis_count = game_rules.get_seis_count()
    if seis_count < 3:
        game_rules.muda_6_count()
        canvas_tabuleiro.bind("<Button-1>", clica)
    else:
        game_rules.seis_tres_vezes_seguidas()
        vez = game_rules.vez_do_proximo()
        draw_canvas.limpa_tabuleiro(canvas_move_peca, root_move_peca)
        draw_canvas.desenha(canvas_move_peca, root_move_peca)

    if game_rules.tem_pecas_no_tabuleiro(vez) == False:
        vez = game_rules.vez_do_proximo()

    else:
        canvas_tabuleiro.bind("<Button-1>", clica)


def carrega_arquivo():
    input = filedialog.askopenfile(initialdir=".", title="Abrir arquivo",
                                   filetype=[('Text files', '*.txt'), ('All files', '.*')])
    lista_variaveis_globais = []
    if input:  # esse if eh para não dar erro caso o usuario cancele a operação
        for linha in input:
            lista_variaveis_globais.append(linha.strip())
        lista_variaveis_globais[0] = int(
            lista_variaveis_globais[0])  # convertendo a linha pra int, ja que ela contem a vez

        i = 1
        for var in lista_variaveis_globais[1:]:
            lista_variaveis_globais[i] = ast.literal_eval(var)  # literal_eval converte string de lista para lista
            i += 1

        canvas = draw_canvas.get_canvas()
        root = draw_canvas.get_root()
        game_rules.novo_jogo()
        draw_canvas.limpa_tabuleiro(canvas, root)
        game_rules.atualiza_vars(lista_variaveis_globais)
        canvas = draw_canvas.get_canvas()
        root = draw_canvas.get_root()
        draw_canvas.desenha(canvas, root)


def salva_arquivo():
    data = [('Text files', '*.txt'), ('All files', '.*')]
    # file_path tem o caminho do diretorio q vai salvar
    file_name = asksaveasfilename()
    if file_name:
        complete_file_path = file_name + '.txt'

        arq = open(complete_file_path, 'w')
        arq.write("%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n"
                  % (game_rules.get_vez(),
                     game_rules.get_casas_inicais(),
                     game_rules.get_caminhos_coloridos(),
                     game_rules.get_caminho_principal(),
                     game_rules.get_caminho_principal_bar(),
                     game_rules.get_caminho_principal_abrigo(),
                     game_rules.get_caminho_vermelho(),
                     game_rules.get_caminho_verde(),
                     game_rules.get_caminho_amarelo(),
                     game_rules.get_caminho_azul()
                     ))


def click_novo_jogo():
    canvas = draw_canvas.get_canvas()
    root = draw_canvas.get_root()
    game_rules.novo_jogo()
    draw_canvas.limpa_tabuleiro(canvas, root)
