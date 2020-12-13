from random import randint


def novo_jogo():
    global caminho_azul, caminho_verde, caminho_vermelho, caminho_amarelo, caminho_principal, casas_iniciais, vez, abrigos_posicoes, casas_saida, seis_count, ultimo_movimento, inicio_reta_final, caminho_principal_bar, caminho_principal_abrigo, caminhos_coloridos, houve_captura_na_jogada, chegou_peca_na_casa_final, ultimo_movimento

    vez = -1  # 1o turno começa com vermelho jogando o dado, se der 6, continua, se não próximo jogador joga o dado

    inicio_reta_final = [37, 24, 11, 50]

    abrigos_posicoes = [9, 22, 35, 48]

    casas_iniciais = [
        [-1, -1, -1, -1],  # vermelho
        [-2, -2, -2, -2],  # verde
        [-3, -3, -3, -3],  # amarelo
        [-4, -4, -4, -4]  # azul
    ]

    casas_saida = [0, 13, 26, 39]

    seis_count = 1

    ultimo_movimento = [0, 0]  # indica posicao aonde caiu a peca do ultimo movimento,

    # último elemento dessas listas representam o quadrado final do jogo,
    # para verificar vitória, basta verificar se no último elemento tem 4 peças
    # 1o elemento eh a casa anterior as coloridas
    caminho_vermelho = [0, 0, 0, 0, 0, []]
    caminho_verde = [0, 0, 0, 0, 0, []]
    caminho_amarelo = [0, 0, 0, 0, 0, []]
    caminho_azul = [0, 0, 0, 0, 0, []]

    caminho_final_bar = []

    # uso isso para verificar a vitória
    caminhos_coloridos = [caminho_vermelho, caminho_verde, caminho_amarelo, caminho_azul]

    # caminho possui 52 quadrados
    caminho_principal = [0, 0, 0, 0, 0, 0, 0, 0, 0, -100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -100, 0,
                         0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                         0, 0, -100, 0, 0, 0]

    caminho_principal_bar = []

    caminho_principal_abrigo = [[[0, 0], 9], [[0, 0], 22], [[0, 0], 35], [[0, 0], 48]]

    seis_count = 0

    houve_captura_na_jogada = False

    chegou_peca_na_casa_final = False


def get_caminho_vermelho():
    global caminho_vermelho
    return caminho_vermelho


def get_caminho_verde():
    global caminho_verde
    return caminho_verde


def get_caminho_amarelo():
    global caminho_amarelo
    return caminho_amarelo


def get_caminho_azul():
    global caminho_azul
    return caminho_azul


def get_caminho_principal():
    global caminho_principal
    return caminho_principal


def get_seis_count():
    global seis_count
    return seis_count


def get_casas_inicais():
    global casas_iniciais
    return casas_iniciais


def get_caminhos_coloridos():
    global caminhos_coloridos
    return caminhos_coloridos


def get_caminho_principal_abrigo():
    global caminho_principal_abrigo
    return caminho_principal_abrigo


def get_caminho_principal_bar():
    global caminho_principal_bar
    return caminho_principal_bar


def atualiza_vars(list_vars_global):
    # essa funcao muda as variaveis quando carrega um jogo
    global vez, casas_iniciais, caminhos_coloridos, caminho_principal, caminho_principal_bar, caminho_principal_abrigo, caminho_azul, caminho_verde, caminho_vermelho, caminho_amarelo

    vez = list_vars_global[0]
    casas_iniciais = list_vars_global[1]
    caminho_principal = list_vars_global[3]
    caminho_principal_bar = list_vars_global[4]
    caminho_principal_abrigo = list_vars_global[5]
    caminho_vermelho = list_vars_global[6]
    caminho_verde = list_vars_global[7]
    caminho_amarelo = list_vars_global[8]
    caminho_azul = list_vars_global[9]
    caminhos_coloridos = [caminho_vermelho, caminho_verde, caminho_amarelo, caminho_azul]


def get_vez():
    global vez
    return vez


def joga_dado():
    return randint(1, 6)


def pode_mover_casa_saida(vez):
    global caminho_principal, casas_iniciais
    # verifica casa de saida
    if caminho_principal[casas_saida[abs(vez) - 1]] == vez:
        return False
    # verifica se tem peca na casa inicial
    for i, peca in enumerate(casas_iniciais[abs(vez) - 1]):
        if peca < 0:
            break
        if i == 3:
            return False
    return True


def move_peca_casa_saida_1a_jogada(vez):
    global casas_iniciais, casas_saida, caminho_principal
    # caso ja tenha peca da mesma cor na casa de saida, nao sair com peca nova
    if caminho_principal[casas_saida[abs(vez) - 1]] == vez:
        return "NA CASA DE SAIDA TEM UMA PECA DA MESMA COR! NADA ACONTECE!"

    # botando a 1a peca encontrada na casa inicial na casa de saida de sua cor  [50, 24, -1, -1]
    for index, peca in enumerate(casas_iniciais[abs(vez) - 1]):
        if peca == vez:
            casas_iniciais[abs(vez) - 1][index] = casas_saida[abs(vez) - 1]
            break
    # botando a peca no caminho principal
    caminho_principal[casas_saida[abs(vez) - 1]] = vez


def tirou_5_no_dado(vez):
    move_peca_casa_saida_1a_jogada(vez)


def tem_pecas_no_tabuleiro(vez):
    # True se tem pecas da cor no tabuleiro, False se não
    global casas_iniciais
    for peca in casas_iniciais[abs(vez) - 1]:
        if peca >= 0 and peca != -100:
            return True
    return False


def muda_6_count():
    global seis_count
    seis_count += 1


def tirou_6_no_dado(vez, dado, pos_atual):
    # O jogador que obtiver um 6 poderá jogar o dado outra vez, após movimentar um de
    # seus peões. Se obtiver novamente 6, poderá realizar novo lançamento, após
    # movimentar um de seus peões. Se obtiver um 6 pela terceira vez consecutiva, o último
    # de seus peões que foi movimentado voltará para a casa inicial.
    global seis_count
    if dado == 6:
        seis_count += 1
    if seis_count != 3:
        move_peca(vez, dado, pos_atual)
    else:
        seis_tres_vezes_seguidas()
        seis_count = 0


def seis_tres_vezes_seguidas():
    global ultimo_movimento, caminho_principal, casas_iniciais
    pos = ultimo_movimento[0]
    vez = ultimo_movimento[1]
    caminho_principal[pos] = 0  # zerando posicao da peca que vai voltar pra casa inicial

    index_peca_pra_mudar_casa_incial = busca(casas_iniciais[abs(vez) - 1], pos)

    casas_iniciais[abs(vez) - 1][index_peca_pra_mudar_casa_incial] = vez  # botando a peca em sua casa de inicial


def move_peca(vez, dado, pos_atual_caminho_principal=None, pos_atual_reta_final=None):
    global caminho_azul, caminho_verde, caminho_vermelho, caminho_amarelo, caminho_principal, ultimo_movimento, casas_iniciais, inicio_reta_final, caminho_final_bar, caminho_principal_bar, abrigos_posicoes, caminho_principal_abrigo, chegou_peca_na_casa_final

    # determina posicao_da_captura da peca na sua lista de casa inicial
    if pos_atual_caminho_principal != None:
        indice_peca_casa_inicial = busca(casas_iniciais[abs(vez) - 1], pos_atual_caminho_principal)
    else:
        indice_peca_casa_inicial = busca(casas_iniciais[abs(vez) - 1], pos_atual_reta_final)

    # definindo caminho final para peça
    if vez == -1:
        caminho_final = caminho_azul
    elif vez == -2:
        caminho_final = caminho_vermelho
    elif vez == -3:
        caminho_final = caminho_verde
    elif vez == -4:
        caminho_final = caminho_amarelo

    # peca esta na reta final?
    # ESSA PARTE DO CODIGO LIDA APENAS COM O MOVIMENTO DE PEÇAS DENTRO DE SUA RETA FINAL
    if pos_atual_reta_final != None:
        pos_nova_dentro_reta_final = pos_atual_reta_final + dado
        if pos_nova_dentro_reta_final == 995:  # chegou na casa final
            caminho_final[-1].append(vez)
            casas_iniciais[abs(vez) - 1][indice_peca_casa_inicial] = 995
            caminho_final[pos_atual_reta_final - 990] = 0
            chegou_peca_na_casa_final = True
        else:
            return

    if pos_atual_caminho_principal == None:
        return

    pos_nova = pos_atual_caminho_principal + dado

    ultimo_movimento[0] = pos_nova
    ultimo_movimento[1] = vez

    entrou_na_reta_final = False  # vai ser usada para atualizar as casas_inciais

    # tem barreira no caminho? e entra na reta final?
    for posicao in range(pos_atual_caminho_principal + 1, pos_nova + 1):  # (8 + 1, 14) => 9,10,11,12,13,14
        # barreira
        for lista in caminho_principal_bar:
            if posicao == lista[-1]:  # tem barreira no caminho, logo acaba a jogada
                return

        # reta final
        if posicao == inicio_reta_final[vez] + 1:  # inicio_reta_final = [37, 24, 11, 50]
            entrou_na_reta_final = True
            distancia_inicio_reta_final = inicio_reta_final[vez] - pos_atual_caminho_principal
            posicao_dentro_reta_final = dado - distancia_inicio_reta_final
            if posicao_dentro_reta_final == 6:  # peca vai ganhar agora
                caminho_final[-1].append(vez)
                casas_iniciais[abs(vez) - 1][indice_peca_casa_inicial] = 995
                caminho_principal[pos_atual_caminho_principal] = 0
                return
            else:
                caminho_final[posicao_dentro_reta_final - 1] = vez
                casas_iniciais[abs(vez) - 1][
                    indice_peca_casa_inicial] = 990 + posicao_dentro_reta_final - 1  # 999 indica que entrou na reta final

    # caso de a volta no tabuleiro (passe da posicao_da_captura 51 para a 0)
    if pos_nova > 51:
        pos_nova = pos_atual_caminho_principal + dado - 52
        # Verificando barreira no caminho
        for posicao_ate_51 in range(pos_atual_caminho_principal, 52):
            for lista in caminho_principal_bar:
                if posicao == lista[-1]:  # tem barreira no caminho, logo acaba a jogada
                    return

        for posicao_de_0_ate_pos_nova in range(0, pos_nova + 1):
            for lista in caminho_principal_bar:
                if posicao == lista[-1]:  # tem barreira no caminho, logo acaba a jogada
                    return

    # movendo a peca
    # verificando se tem peca na posicao_da_captura nova
    # da mesma cor
    if caminho_principal[pos_nova] != 0:
        if caminho_principal[pos_nova] == vez:
            # cria barreira, caminho principal fica igual, mas o caminho_principal_bar muda, EX: [[-1, 42]]
            lista_com_vez_e_posicao_da_barreira = [vez, pos_nova]
            caminho_principal_bar.append(lista_com_vez_e_posicao_da_barreira)

        # verificando se eh abrigo  # caminho_principal_abrigo = [[[0, 0], 9],[[0, 0], 22],[[0, 0], 35],[[0, 0], 48]]
        # CRIANDO ABRIGO - caminho principal fica com 0 na posicao e atualizo caminho_principal_abrigo
        elif pos_nova in abrigos_posicoes:
            peca_que_ja_estava_no_abrigo = caminho_principal[pos_nova]
            lista_com_peca_a_ser_colocada_e_peca_que_ja_estava_no_abrigo = [peca_que_ja_estava_no_abrigo, vez]
            caminho_principal[pos_nova] = 0  # botando 0 no caminho principal

            # atualizando caminho_principal_abrigo
            if pos_nova == 9:
                caminho_principal_abrigo[0][0] = lista_com_peca_a_ser_colocada_e_peca_que_ja_estava_no_abrigo
            elif pos_nova == 22:
                caminho_principal_abrigo[1][0] = lista_com_peca_a_ser_colocada_e_peca_que_ja_estava_no_abrigo
            elif pos_nova == 35:
                caminho_principal_abrigo[2][0] = lista_com_peca_a_ser_colocada_e_peca_que_ja_estava_no_abrigo
            else:
                caminho_principal_abrigo[3][0] = lista_com_peca_a_ser_colocada_e_peca_que_ja_estava_no_abrigo

        # tem peca de outra cor, vou capturar
        else:
            captura(vez,
                    pos_nova)  # captura vai trocar o valor da peca na posicao_da_captura nova, e mudar o valor da casa inical da peca capturada

        casas_iniciais[abs(vez) - 1][indice_peca_casa_inicial] = pos_nova

    # posicao_da_captura nova esta VAZIA e a peça NÃO ENTROU no reta final
    if caminho_principal[pos_nova] == 0 and entrou_na_reta_final == False:
        caminho_principal[pos_nova] = vez
        casas_iniciais[abs(vez) - 1][indice_peca_casa_inicial] = pos_nova

    # posicao_da_captura nova esta VAZIA e a peça ENTROU no reta final
    elif caminho_principal[pos_nova] == 0 and entrou_na_reta_final == True:
        caminho_principal[pos_nova] = 0

    # MUDANCA NA POS_ATUAL
    # Se pos_atual_caminho_principal for uma barreira: manter caminho_principal igual, e apagar sub-lista que representa a barreira do caminho_principal_bar
    # caminho_principal_bar -> EX: [[-1, 42], [-4, 34], [-2, 0]]
    pos_barreiras = []  # EX: [42, 34, 0]
    for lista_barreira in caminho_principal_bar:
        pos_barreiras.append(lista_barreira[-1])
        if pos_atual_caminho_principal == lista_barreira[-1]:
            caminho_principal_bar.remove(lista_barreira)

    # verificando se posicao_da_captura atual da peça possui BARREIRA
    if pos_atual_caminho_principal not in pos_barreiras:
        caminho_principal[pos_atual_caminho_principal] = 0

    # verificando se posicao_da_captura atual da peça possui ABRIGO
    # LIBERANDO UM ABRIGO
    if pos_atual_caminho_principal in abrigos_posicoes:  # abrigos_posicoes = [9, 22, 35, 48]
        # vendo qual eh o indice da peca da vez na lista caminho_principal_abrigo, e botando 0 nessa posição
        if pos_atual_caminho_principal == 9:
            index_peca_da_vez_no_abrigo = busca(caminho_principal_abrigo[0][0], vez)
            caminho_principal_abrigo[0][0][index_peca_da_vez_no_abrigo] = 0
        elif pos_atual_caminho_principal == 22:
            index_peca_da_vez_no_abrigo = busca(caminho_principal_abrigo[1][0], vez)
            caminho_principal_abrigo[1][0][index_peca_da_vez_no_abrigo] = 0
        elif pos_atual_caminho_principal == 35:
            index_peca_da_vez_no_abrigo = busca(caminho_principal_abrigo[2][0], vez)
            caminho_principal_abrigo[2][0][index_peca_da_vez_no_abrigo] = 0
        else:
            index_peca_da_vez_no_abrigo = busca(caminho_principal_abrigo[3][0], vez)
            caminho_principal_abrigo[3][0][index_peca_da_vez_no_abrigo] = 0

    # ABRIGOS TAVAM COM -100 DENTRO, ISSO AQUI CONCERTA
    for abrigo_informacoes in caminho_principal_abrigo:
        for index, pecas in enumerate(abrigo_informacoes[0]):
            if pecas == -100:
                abrigo_informacoes[0][index] = 0


def captura(vez_da_peca_que_captura, posicao_da_captura):
    global caminho_principal, casas_iniciais, houve_captura_na_jogada

    houve_captura_na_jogada = True

    # movendo a peca pra casa nova
    peca_capturada = caminho_principal[posicao_da_captura]
    caminho_principal[posicao_da_captura] = vez_da_peca_que_captura

    # buscando qual o index_da_casa_inicial_da_peca_capturada
    index_da_casa_inicial_da_peca_capturada = busca(casas_iniciais[abs(peca_capturada) - 1], posicao_da_captura)

    # voltando peca capturada para a casa inicial de sua cor
    casas_iniciais[abs(peca_capturada) - 1][index_da_casa_inicial_da_peca_capturada] = peca_capturada


def get_houve_captura_na_jogada():
    global houve_captura_na_jogada
    return houve_captura_na_jogada


def muda_houve_captura_para_falso():
    global houve_captura_na_jogada, peca_chegou_na_casa_final
    houve_captura_na_jogada = False
    peca_chegou_na_casa_final = False


def get_chegou_peca_na_casa_final():
    global chegou_peca_na_casa_final
    return chegou_peca_na_casa_final


def busca(lista, elemento):
    """retorna índice de um elemento específico em um lista """
    for index, el in enumerate(lista):
        if el == elemento:
            return index
    return 0  # None


def vez_do_proximo():
    """passa a vez para a próxima cor"""
    global seis_count, vez
    cores_peca = ["blue", "yellow", "green", "red"]
    seis_count = 0
    if vez == -4:
        vez = -1
    else:
        vez -= 1
    return vez


def verifica_vitoria():
    """ se alguem ganhou, retorna lista com os jogadores na ordem crescente de vitória , se não retorna None"""
    global caminho_azul, caminho_verde, caminho_vermelho, caminho_amarelo, casas_iniciais
    lista_com_todos_os_caminhos = [caminho_azul, caminho_vermelho, caminho_verde, caminho_amarelo]
    vencedores_em_ordem_decrescente = []  # => [-2, -4, -1, -3]
    casas_de_saida = [0, 9, 22, 35]
    for caminho in lista_com_todos_os_caminhos:
        if len(caminho[-1]) == 4:
            vez_do_vencedor = caminho[-1][0]
            # adiciono em uma lista sublistas contendo [soma das posiscoes de cada peca de uma cor ajustadas, vez da cor],
            # depois faco sort e pego os segundos elementos desse lista e retorno esses valores em outra lista contedo
            # a vez dos vencedores do 1o lugar ate 4o.
            placares = []
            for index, caminho in enumerate(casas_iniciais):
                somatorio_placar = 0
                for pos_peca in caminho:
                    if pos_peca > 0:
                        somatorio_placar += abs(pos_peca - casas_de_saida[index])
                    vez_da_peca = (index + 1) * (-1)
                placares.append([somatorio_placar, vez_da_peca])
                sorted(placares, reverse=True)

            for index, placar in enumerate(sorted(placares, reverse=True)):
                if index <= 4:
                    vencedores_em_ordem_decrescente.append(placar[-1])

            return vencedores_em_ordem_decrescente

    return None


def jogo_acabou():
    if verifica_vitoria():
        return True
    return False
