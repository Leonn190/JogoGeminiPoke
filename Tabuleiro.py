import pygame
import random
from Visual.Sonoridade import tocar
import Visual.GeradoresVisuais as GV
import PygameAções as A
from Visual.GeradoresVisuais import (
    Fonte15, Fonte20, Fonte30, Fonte40, Fonte50,Fonte70,
    PRETO, BRANCO, CINZA, AZUL, AZUL_CLARO,AZUL_SUPER_CLARO,
    AMARELO, AMARELO_CLARO, VERMELHO,VERMELHO_CLARO, VERDE, VERDE_CLARO,
    LARANJA, ROXO, ROSA, DOURADO, PRATA,)

Area = [(3, 8), (3, 9), (3, 10), (3, 11), (3, 12), (3, 13), (3, 14), (3, 15), (3, 16),
        (4, 8), (4, 9), (4, 10), (4, 11), (4, 12), (4, 13), (4, 14), (4, 15), (4, 16),
        (5, 8), (5, 9), (5, 10), (5, 11), (5, 12), (5, 13), (5, 14), (5, 15), (5, 16),
        (6, 8), (6, 9), (6, 10), (6, 11), (6, 12), (6, 13), (6, 14), (6, 15), (6, 16),
        (7, 8), (7, 9), (7, 10), (7, 11), (7, 12), (7, 13), (7, 14), (7, 15), (7, 16),
        (8, 8), (8, 9), (8, 10), (8, 11), (8, 12), (8, 13), (8, 14), (8, 15), (8, 16),
        (9, 8), (9, 9), (9, 10), (9, 11), (9, 12), (9, 13), (9, 14), (9, 15), (9, 16),
        (10, 8), (10, 9), (10, 10), (10, 11), (10, 12), (10, 13), (10, 14), (10, 15), (10, 16),
        (11, 8), (11, 9), (11, 10), (11, 11), (11, 12), (11, 13), (11, 14), (11, 15), (11, 16)]


def desselecionae():
    pass

desseleciona = desselecionae

def Gerar_Mapa():

    Zona = []
    for i in range(15):  # 15 linhas
        linha = []
        for j in range(25):  # 20 colunas
            casa = {
                "id": (i, j),
                "ocupado": None  # Aqui futuramente pode ser um Pokémon ou outro objeto
            }
            linha.append(casa)
        Zona.append(linha)
    return Zona

def Desenhar_Casas_Disponiveis(tela, Mapa, player, inimigo, Fonte, eventos, seleciona_peça, desseleciona_peça, PeçaS, estadoTabuleiro):
    global desseleciona
    desseleciona = desseleciona_peça
    Zona = Mapa.Zona
    metros = Mapa.Metros
    casas_disponiveis = Mapa.area
    cores_zebragem = Mapa.cores
    tamanho_casa = 40
    tamanho_imagem = 38
    x_inicial = (1920 - 25 * tamanho_casa) // 2
    y_inicial = (1080 - 15 * tamanho_casa) // 2

    # Se nenhuma casa foi passada, desenhar o mapa todo
    if not casas_disponiveis:
        casas_disponiveis = [(linha, coluna) for linha in range(15) for coluna in range(25)]

    for pokemon in player.pokemons:
        if pokemon.local is not None:
            if pokemon.local["id"] not in casas_disponiveis:
                linha_antiga, coluna_antiga = pokemon.local["id"]
                Zona[linha_antiga][coluna_antiga]["ocupado"] = None
                pokemon.local = None
                pokemon.guardado = 3
    for pokemon in inimigo.pokemons:
        if pokemon.local is not None:
            if pokemon.local["id"] not in casas_disponiveis:
                linha_antiga, coluna_antiga = pokemon.local["id"]
                Zona[linha_antiga][coluna_antiga]["ocupado"] = None
                pokemon.local = None
                pokemon.guardado = 3

    for (linha, coluna) in casas_disponiveis:
        casa = Zona[linha][coluna]
        x = x_inicial + coluna * tamanho_casa
        y = y_inicial + linha * tamanho_casa
        espaco = pygame.Rect(x, y, tamanho_casa, tamanho_casa)

        if casa["ocupado"] is not None:
            id_ocupado = casa["ocupado"]
            pokemon_encontrado = None
            dono = None  # "player" ou "inimigo"

            for poke in player.pokemons:
                if poke.ID == id_ocupado:
                    pokemon_encontrado = poke
                    dono = "player"
                    break


            if not pokemon_encontrado:
                for poke in inimigo.pokemons:
                    if poke.ID == id_ocupado:
                        pokemon_encontrado = poke
                        dono = "inimigo"
                        break


            if pokemon_encontrado:
                cor_fundo = (0, 0, 255) if dono == "player" else (255, 0, 0)

                GV.Botao_Selecao(
                    tela=tela,
                    espaço=espaco,
                    texto="",
                    Fonte=Fonte,
                    cor_fundo=cor_fundo,
                    cor_borda_normal=PRETO,
                    cor_passagem=AMARELO,
                    cor_borda_esquerda=VERMELHO,
                    funcao_esquerdo=lambda p=pokemon_encontrado: seleciona_peça(p, dono, player),
                    desfazer_esquerdo=lambda: desseleciona_peça(),
                    estado_global=estadoTabuleiro,
                    eventos=eventos,
                    id_botao=id_ocupado,
                    grossura=2
                )

                x_img = x + (tamanho_casa - tamanho_imagem) // 2
                y_img = y + (tamanho_casa - tamanho_imagem) // 2
                tela.blit(pokemon_encontrado.icone, (x_img - 2, y_img - 3))

        else:
            cor_casa_disponivel = cores_zebragem[(linha + coluna) % 2]
            pygame.draw.rect(tela, cor_casa_disponivel, espaco)
            pygame.draw.rect(tela, (0, 0, 0), espaco, 2)

    if PeçaS is not None:
        Mover_casas(tela, eventos, PeçaS, casas_disponiveis, player, Zona, metros)

def Move(peça, L, C,Zona):

    if peça.local is not None:

        linha_antiga, coluna_antiga = peça.local["id"]
        Zona[linha_antiga][coluna_antiga]["ocupado"] = None

        # Atualizar a nova posição
    peça.local = Zona[L][C]
    Zona[L][C]["ocupado"] = peça.ID

    desseleciona()

def Inverter_Tabuleiro(player, inimigo, Zona):
    # Cria novo mapa espelhado verticalmente
    nova_Zona = []
    for i in range(15):
        linha = []
        for j in range(25):
            casa = {
                "id": (i, j),
                "ocupado": None
            }
            linha.append(casa)
        nova_Zona.append(linha)

    # Reposiciona todos os pokémons no novo mapa invertido
    for poke in player.pokemons + inimigo.pokemons:
        if poke.local is not None:
            antiga_linha, coluna = poke.local["id"]
            nova_linha = 14 - antiga_linha  # espelhamento vertical
            novo_local = nova_Zona[nova_linha][coluna]
            poke.local = novo_local
            novo_local["ocupado"] = poke.ID  # Corrigido para 'ID'

    return nova_Zona

def Mover_casas(tela, eventos, PeçaS, casas_disponiveis, player, Zona, metros=10):
    tamanho_casa = 40
    x_inicial = (1920 - 25 * tamanho_casa) // 2
    y_inicial = (1080 - 15 * tamanho_casa) // 2

    vel = PeçaS.vel

    if vel <= 0:
        return  # Pokémon imóvel

    alcance = int(vel / metros)
    if vel > 0 and alcance < 1:
        alcance = 1  # Pelo menos 1 movimento lateral garantido

    # Definir limites de movimento lateral e diagonal conforme escala personalizada
    if alcance == 1:
        alcance_lateral = 1
        alcance_diagonal = 1
    elif alcance == 2:
        alcance_lateral = 2
        alcance_diagonal = 1
    elif alcance == 3:
        alcance_lateral = 2
        alcance_diagonal = 2
    elif alcance == 4:
        alcance_lateral = 3
        alcance_diagonal = 2
    elif alcance == 5:
        alcance_lateral = 3
        alcance_diagonal = 3
    elif alcance == 6:
        alcance_lateral = 4
        alcance_diagonal = 3
    else:
        alcance_lateral = min(4 + (alcance - 6), 10)  # opcional: limitar para evitar exageros
        alcance_diagonal = min(3 + (alcance - 5), 10)

    linha_atual, coluna_atual = PeçaS.local["id"]
    movimentos_possiveis = []

    for dx in range(-alcance_lateral, alcance_lateral + 1):
        for dy in range(-alcance_lateral, alcance_lateral + 1):
            nova_linha = linha_atual + dy
            nova_coluna = coluna_atual + dx

            if (0 <= nova_linha < 15 and 0 <= nova_coluna < 25 and
                (nova_linha, nova_coluna) in casas_disponiveis and
                Zona[nova_linha][nova_coluna]["ocupado"] is None):

                # Verifica se é diagonal
                if dx != 0 and dy != 0:
                    if abs(dx) <= alcance_diagonal and abs(dy) <= alcance_diagonal:
                        movimentos_possiveis.append((nova_linha, nova_coluna))
                else:
                    movimentos_possiveis.append((nova_linha, nova_coluna))

    for linha, coluna in movimentos_possiveis:
        x = x_inicial + coluna * tamanho_casa
        y = y_inicial + linha * tamanho_casa
        espaco = pygame.Rect(x, y, tamanho_casa, tamanho_casa)

        GV.Botao(
            tela=tela,
            texto="",
            espaço=espaco,
            cor_normal=(100, 255, 100),
            cor_borda=BRANCO,
            cor_passagem=(150, 255, 150),
            acao=lambda linha=linha, coluna=coluna: Move(PeçaS, linha, coluna, Zona),
            Fonte=pygame.font.SysFont("arial", 16),
            estado_clique={"estado": False},
            grossura=2,
            eventos=eventos
        )

def GuardarPosicionar(pokemon,player,tempo,Zona):
    
    
    if pokemon.local is not None:
        linha_antiga, coluna_antiga = pokemon.local["id"]
        Zona[linha_antiga][coluna_antiga]["ocupado"] = None
        pokemon.local = None
        pokemon.guardado = tempo

    else:
        for i in range(len(Zona)):
            for tentativa in range(40):
                j = random.randint(0, 24)
                if Zona[14 - i][j]["ocupado"] is None:
                    if Zona[14 - i][j]["id"] in Area:
                        pokemon.local = Zona[14 - i][j]
                        Zona[14 - i][j]["ocupado"] = pokemon.ID
                        return





    