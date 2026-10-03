import os
import sys
import pygame
from pygame.locals import *

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def ruta_imatges(subcarpeta, archivo):
    return os.path.join(BASE_DIR, "Imatges", subcarpeta, archivo)

def ruta_sons(subcarpeta, archivo):
    return os.path.join(BASE_DIR, "Sons", subcarpeta, archivo)

pygame.init()
pygame.display.set_caption('P.R.A.I.L.')
pygame.mouse.set_visible(False)

AMPLADA = 889
ALCADA = 500
es_pantalla_gran = False

PANTALLA = pygame.display.set_mode((AMPLADA, ALCADA), pygame.SCALED)
pygame.display.toggle_fullscreen()

icona = pygame.image.load(ruta_imatges("Jugador", "Alex_icona.png"))
pygame.display.set_icon(icona)

alex_quiet_esquerra = pygame.image.load(ruta_imatges("Jugador", "Alex_quiet.png")).convert_alpha()
alex_quiet_dreta = pygame.transform.flip(alex_quiet_esquerra, True, False)
alex_frame1_esquerra = pygame.image.load(ruta_imatges("Jugador", "Alex_frame1.png")).convert_alpha()
alex_frame1_dreta = pygame.transform.flip(alex_frame1_esquerra, True, False)
alex_frame2_esquerra = pygame.image.load(ruta_imatges("Jugador", "Alex_frame2.png")).convert_alpha()
alex_frame2_dreta = pygame.transform.flip(alex_frame2_esquerra, True, False)
alex_salt_esquerra = pygame.image.load(ruta_imatges("Jugador", "Alex_salt.png")).convert_alpha()
alex_salt_dreta = pygame.transform.flip(alex_salt_esquerra, True, False)

alex_estado_quiet_esquerra = pygame.image.load(ruta_imatges("Jugador", "Alex_estado_quiet.png")).convert_alpha()
alex_estado_quiet_dreta = pygame.transform.flip(alex_estado_quiet_esquerra, True, False)
alex_estado_frame1_esquerra = pygame.image.load(ruta_imatges("Jugador", "Alex_estado_frame1.png")).convert_alpha()
alex_estado_frame1_dreta = pygame.transform.flip(alex_estado_frame1_esquerra, True, False)
alex_estado_frame2_esquerra = pygame.image.load(ruta_imatges("Jugador", "Alex_estado_frame2.png")).convert_alpha()
alex_estado_frame2_dreta = pygame.transform.flip(alex_estado_frame2_esquerra, True, False)
alex_estado_salt_esquerra = pygame.image.load(ruta_imatges("Jugador", "Alex_estado_salt.png")).convert_alpha()
alex_estado_salt_dreta = pygame.transform.flip(alex_estado_salt_esquerra, True, False)

fons = pygame.image.load(ruta_imatges("Fons", "portada.png"))
fons_tutorial = pygame.image.load(ruta_imatges("Fons", "portada_tut.png"))
fons_museu = pygame.image.load(ruta_imatges("Fons", "portada_mus.png"))
fons_banc = pygame.image.load(ruta_imatges("Fons", "portada_banc.png"))
fons_banc2 = pygame.image.load(ruta_imatges("Fons", "portada_banc2.png"))
fons_banc3 = pygame.image.load(ruta_imatges("Fons", "portada_banc3.png"))
fons_banc4 = pygame.image.load(ruta_imatges("Fons", "portada_banc4.png"))
fons_casa = pygame.image.load(ruta_imatges("Fons", "portada_casa.png"))
fons_casa2 = pygame.image.load(ruta_imatges("Fons", "portada_casa2.png"))

img_mur = pygame.image.load(ruta_imatges("Entorn", "murs.png")).convert_alpha()
img_prestatg = pygame.image.load(ruta_imatges("Entorn", "prestatg.png")).convert_alpha()
img_estant = pygame.image.load(ruta_imatges("Entorn", "estant.png")).convert_alpha()
img_repisa = pygame.image.load(ruta_imatges("Entorn", "repisa.png")).convert_alpha()
boto_img = pygame.image.load(ruta_imatges("Entorn", "boto.png")).convert_alpha()

tutorial2_copa = pygame.image.load(ruta_imatges("Tresor", "copa.png")).convert_alpha()
nivell1_quadre = pygame.image.load(ruta_imatges("Tresor", "quadre.png")).convert_alpha()
nivell1_quadre2 = pygame.image.load(ruta_imatges("Tresor", "quadre2.png")).convert_alpha()
nivell1_quadre3 = pygame.image.load(ruta_imatges("Tresor", "quadre3.png")).convert_alpha()
nivell1_quadre4 = pygame.image.load(ruta_imatges("Tresor", "quadre4.png")).convert_alpha()
nivell2_clau = pygame.image.load(ruta_imatges("Tresor", "clau.png")).convert_alpha()
nivell2_or = pygame.image.load(ruta_imatges("Tresor", "or.png")).convert_alpha()
nivell2_or2 = pygame.image.load(ruta_imatges("Tresor", "or.png")).convert_alpha()
nivell2_or3 = pygame.image.load(ruta_imatges("Tresor", "or.png")).convert_alpha()
nivell2_or4 = pygame.image.load(ruta_imatges("Tresor", "or.png")).convert_alpha()
nivell3_gerro = pygame.image.load(ruta_imatges("Tresor", "gerro.png")).convert_alpha()
nivell3_diamant = pygame.image.load(ruta_imatges("Tresor", "diamant.png")).convert_alpha()
nivell3_clau2 = pygame.image.load(ruta_imatges("Tresor", "clau2.png")).convert_alpha()

camara_img = pygame.image.load(ruta_imatges("Enemic", "camara.png")).convert_alpha()

agente_img_base = pygame.image.load(ruta_imatges("Enemic", "agente.png")).convert_alpha()
agente_img_esquerra = agente_img_base
agente_img_dreta = pygame.transform.flip(agente_img_base, True, False)

deteccio_img_base = pygame.image.load(ruta_imatges("Enemic", "deteccio.png")).convert_alpha()
deteccio_img_esquerra = deteccio_img_base
deteccio_img_dreta = pygame.transform.flip(deteccio_img_base, True, False)

clock = pygame.time.Clock()

NEGRE = (20, 20, 20)
BLANC = (255, 255, 255)
VERD = (0, 255, 0)
VERMELL = (255, 50, 50)
TARONJA = (255, 150, 0)
GROC = (255, 255, 0)
CIBER_BLAU = (0, 255, 255)
GRIS = (128, 128, 128)

font_gran = pygame.font.SysFont("roboto mono", 60, bold=True)
font_petita = pygame.font.SysFont("roboto mono", 25)
font_mes_petita = pygame.font.SysFont("roboto mono", 20)

volum_musica = 1.0
volum_sfx = 1.0
arrossegar_musica = False
arrossegar_sfx = False
musica_actual = None

so_recollit = pygame.mixer.Sound(ruta_sons("SFX", "recollit.mp3"))

def canviar_musica(nom_arxiu):
    global musica_actual
    if musica_actual != nom_arxiu or not pygame.mixer.music.get_busy():
        try:
            ruta = ruta_sons("musica", nom_arxiu)
            pygame.mixer.music.load(ruta)
            pygame.mixer.music.set_volume(volum_musica)
            pygame.mixer.music.play(-1)
            musica_actual = nom_arxiu
        except Exception as e:
            print(f"No s'ha pogut carregar la música: {nom_arxiu}. Error: {e}")
canviar_musica("inici.mp3")

estat_transicio = None
cortina_y = -ALCADA
velocitat_cortina = 20
temps_inici_espera = 0

def iniciar_transicio(aturar_musica=False):
    global estat_transicio, cortina_y, musica_actual

    if aturar_musica:
        pygame.mixer.music.fadeout(400)
        musica_actual = None

    fons_vell = PANTALLA.copy()
    cortina_y = -ALCADA

    while cortina_y < 0:
        PANTALLA.blit(fons_vell, (0, 0))
        cortina_y += velocitat_cortina
        if cortina_y >= 0:
            cortina_y = 0
        pygame.draw.rect(PANTALLA, NEGRE, (0, cortina_y, AMPLADA, ALCADA))
        pygame.display.update()
        clock.tick(60)

    pygame.time.wait(300)
    estat_transicio = "SORTINT_PER_BAIX"

def actualitzar_pantalla_amb_transicio():
    global estat_transicio, cortina_y

    if estat_transicio == "SORTINT_PER_BAIX":
        fons_nou = PANTALLA.copy()
        while cortina_y < ALCADA:
            PANTALLA.blit(fons_nou, (0, 0))
            cortina_y += velocitat_cortina
            pygame.draw.rect(PANTALLA, NEGRE, (0, cortina_y, AMPLADA, ALCADA))
            pygame.display.update()
            clock.tick(60)
        cortina_y = -ALCADA
        estat_transicio = None
        return

    pygame.display.update()

def mostrar_text(text, font, color, x, y):
    superficie = font.render(text, True, color)
    rect = superficie.get_rect(center=(x, y))
    PANTALLA.blit(superficie, rect)

def pantalla_inici():
    esperant = True
    opcio_seleccionada = 0

    boto_jugar = pygame.Rect(369, 280, 150, 50)
    boto_ajustaments = pygame.Rect(369, 360, 150, 50)
    boto_sortir = pygame.Rect(369, 440, 150, 50)

    botons = [boto_jugar, boto_ajustaments, boto_sortir]

    while esperant:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                iniciar_transicio()
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key in (K_UP, K_LEFT):
                    opcio_seleccionada = (opcio_seleccionada - 1) % len(botons)
                elif event.key in (K_DOWN, K_RIGHT):
                    opcio_seleccionada = (opcio_seleccionada + 1) % len(botons)
                elif event.key in (K_RETURN, K_KP_ENTER):
                    iniciar_transicio()
                    if opcio_seleccionada == 0:
                        return "SELECCIÓ NIVELLS"
                    elif opcio_seleccionada == 1:
                        return "AJUSTAMENTS"
                    elif opcio_seleccionada == 2:
                        pygame.quit()
                        sys.exit()

        PANTALLA.blit(fons, (0, 0))
        mostrar_text("P . R . A . I . L .", font_gran, BLANC, AMPLADA // 2, ALCADA // 4)

        for i, boto in enumerate(botons):
            color_boto = TARONJA if i == opcio_seleccionada else CIBER_BLAU
            pygame.draw.rect(PANTALLA, color_boto, boto)

        mostrar_text("JUGAR", font_petita, NEGRE, boto_jugar.centerx, boto_jugar.centery)
        mostrar_text("AJUSTAMENTS", font_petita, NEGRE, boto_ajustaments.centerx, boto_ajustaments.centery)
        mostrar_text("SORTIR", font_petita, NEGRE, boto_sortir.centerx, boto_sortir.centery)

        actualitzar_pantalla_amb_transicio()

def pantalla_nivells():
    global nivells_completats
    en_nivells = True
    opcio_seleccionada = 0

    boto_tutorial = pygame.Rect(165, 200, 100, 100)
    boto_nivell1 = pygame.Rect(315, 200, 100, 100)
    boto_nivell2 = pygame.Rect(465, 200, 100, 100)
    boto_nivell3 = pygame.Rect(615, 200, 100, 100)
    boto_tornar1 = pygame.Rect(369, 350, 150, 50)

    botons = [boto_tutorial, boto_nivell1, boto_nivell2, boto_nivell3, boto_tornar1]

    while en_nivells:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                iniciar_transicio()
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key in (K_LEFT, K_UP):
                    opcio_seleccionada = (opcio_seleccionada - 1) % len(botons)
                elif event.key in (K_RIGHT, K_DOWN):
                    opcio_seleccionada = (opcio_seleccionada + 1) % len(botons)
                elif event.key in (K_RETURN, K_KP_ENTER):
                    iniciar_transicio()
                    if opcio_seleccionada == 0:
                        iniciar_transicio(aturar_musica=True)
                        return "TUTORIAL"
                    elif opcio_seleccionada == 1:
                        iniciar_transicio(aturar_musica=True)
                        return "NIVELL1"
                    elif opcio_seleccionada == 2:
                        if nivells_completats["nivell1"]:
                            iniciar_transicio(aturar_musica=True)
                            return "NIVELL2"
                    elif opcio_seleccionada == 3:
                        if nivells_completats["nivell1"] and nivells_completats["nivell2"]:
                            iniciar_transicio(aturar_musica=True)
                            return "NIVELL3"
                    elif opcio_seleccionada == 4:
                        return "TORNAR"
                elif event.key in (K_RETURN, K_ESCAPE):
                    iniciar_transicio()
                    return "TORNAR"

        PANTALLA.fill(NEGRE)
        mostrar_text("SELECCIONA NIVELL", font_gran, BLANC, AMPLADA // 2, 100)

        for i, boto in enumerate(botons):
            color_boto = TARONJA if i == opcio_seleccionada else CIBER_BLAU
            pygame.draw.rect(PANTALLA, color_boto, boto)

        mostrar_text("TUTORIAL", font_petita, NEGRE, boto_tutorial.centerx, boto_tutorial.centery)
        mostrar_text("NIVELL 1", font_petita, NEGRE, boto_nivell1.centerx, boto_nivell1.centery)

        if nivells_completats["nivell1"]:
            mostrar_text("NIVELL 2", font_petita, NEGRE, boto_nivell2.centerx, boto_nivell2.centery)
        else:
            mostrar_text("Bloquejat", font_petita, NEGRE, boto_nivell2.centerx, boto_nivell2.centery)
        if nivells_completats["nivell1"] and nivells_completats["nivell2"]:
            mostrar_text("NIVELL 3", font_petita, NEGRE, boto_nivell3.centerx, boto_nivell3.centery)
        else:
            mostrar_text("Bloquejat", font_petita, NEGRE, boto_nivell3.centerx, boto_nivell3.centery)

        mostrar_text("TORNAR", font_petita, NEGRE, boto_tornar1.centerx, boto_tornar1.centery)

        actualitzar_pantalla_amb_transicio()

def pantalla_ajustaments():
    en_ajustaments = True
    opcio_seleccionada = 0

    boto_controls = pygame.Rect(369, 150, 150, 50)
    boto_so = pygame.Rect(369, 230, 150, 50)
    boto_pantalla_gran = pygame.Rect(369, 310, 150, 50)
    boto_tornar2 = pygame.Rect(369, 390, 150, 50)

    botons = [boto_controls, boto_so, boto_pantalla_gran, boto_tornar2]

    while en_ajustaments:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == QUIT:
                iniciar_transicio()
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key in (K_UP, K_LEFT):
                    opcio_seleccionada = (opcio_seleccionada - 1) % len(botons)
                elif event.key in (K_DOWN, K_RIGHT):
                    opcio_seleccionada = (opcio_seleccionada + 1) % len(botons)
                elif event.key in (K_RETURN, K_KP_ENTER):
                    iniciar_transicio()
                    if opcio_seleccionada == 0:
                        return "CONTROLS"
                    elif opcio_seleccionada == 1:
                        return "SO"
                    elif opcio_seleccionada == 2:
                        return "PANTALLA"
                    elif opcio_seleccionada == 3:
                        return "TORNAR"
                elif event.key in (K_RETURN, K_ESCAPE):
                    iniciar_transicio()
                    return "TORNAR"

        PANTALLA.fill(NEGRE)
        mostrar_text("AJUSTAMENTS", font_gran, BLANC, AMPLADA // 2, 100)

        for i, boto in enumerate(botons):
            color_boto = TARONJA if i == opcio_seleccionada else CIBER_BLAU
            pygame.draw.rect(PANTALLA, color_boto, boto)

        mostrar_text("CONTROLS", font_petita, NEGRE, boto_controls.centerx, boto_controls.centery)
        mostrar_text("SO", font_petita, NEGRE, boto_so.centerx, boto_so.centery)
        mostrar_text("PANTALLA", font_petita, NEGRE, boto_pantalla_gran.centerx, boto_pantalla_gran.centery)
        mostrar_text("TORNAR", font_petita, NEGRE, boto_tornar2.centerx, boto_tornar2.centery)

        actualitzar_pantalla_amb_transicio()

def pantalla_ajustaments2():
    en_ajustaments2 = True
    opcio_seleccionada = 0

    boto_controls = pygame.Rect(369, 150, 150, 50)
    boto_so = pygame.Rect(369, 230, 150, 50)
    boto_pantalla_gran = pygame.Rect(369, 310, 150, 50)
    boto_tornar6 = pygame.Rect(369, 390, 150, 50)

    botons = [boto_controls, boto_so, boto_pantalla_gran, boto_tornar6]

    while en_ajustaments2:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == QUIT:
                iniciar_transicio()
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key in (K_UP, K_LEFT):
                    opcio_seleccionada = (opcio_seleccionada - 1) % len(botons)
                elif event.key in (K_DOWN, K_RIGHT):
                    opcio_seleccionada = (opcio_seleccionada + 1) % len(botons)
                elif event.key in (K_RETURN, K_KP_ENTER):
                    iniciar_transicio()
                    if opcio_seleccionada == 0:
                        return "CONTROLS"
                    elif opcio_seleccionada == 1:
                        return "SO"
                    elif opcio_seleccionada == 2:
                        return "PANTALLA"
                    elif opcio_seleccionada == 3:
                        return "TORNAR2"
                elif event.key in (K_RETURN, K_ESCAPE):
                    iniciar_transicio()
                    return "TORNAR2"

        PANTALLA.fill(NEGRE)
        mostrar_text("AJUSTAMENTS", font_gran, BLANC, AMPLADA // 2, 100)

        for i, boto in enumerate(botons):
            color_boto = TARONJA if i == opcio_seleccionada else CIBER_BLAU
            pygame.draw.rect(PANTALLA, color_boto, boto)

        mostrar_text("CONTROLS", font_petita, NEGRE, boto_controls.centerx, boto_controls.centery)
        mostrar_text("SO", font_petita, NEGRE, boto_so.centerx, boto_so.centery)
        mostrar_text("PANTALLA", font_petita, NEGRE, boto_pantalla_gran.centerx, boto_pantalla_gran.centery)
        mostrar_text("TORNAR", font_petita, NEGRE, boto_tornar6.centerx, boto_tornar6.centery)

        actualitzar_pantalla_amb_transicio()

def pantalla_controls():
    en_controls = True

    boto_mov = pygame.Rect(144, 130, 200, 30)
    boto_salt = pygame.Rect(144, 170, 200, 30)
    boto_gadg = pygame.Rect(144, 210, 200, 30)
    boto_canvi = pygame.Rect(144, 250, 200, 30)
    boto_inter = pygame.Rect(144, 290, 200, 30)
    boto_tornar3 = pygame.Rect(344, 450, 200, 30)

    boto_mov2 = pygame.Rect(544, 130, 200, 30)
    boto_salt2 = pygame.Rect(544, 170, 200, 30)
    boto_gadg2 = pygame.Rect(544, 210, 200, 30)
    boto_canvi2 = pygame.Rect(544, 250, 200, 30)
    boto_inter2 = pygame.Rect(544, 290, 200, 30)

    while en_controls:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == QUIT:
                iniciar_transicio()
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key in (K_RETURN, K_KP_ENTER, K_ESCAPE):
                    iniciar_transicio()
                    return "TORNAR"

        PANTALLA.fill(NEGRE)
        mostrar_text("CONTROLS", font_gran, BLANC, AMPLADA // 2, 50)

        pygame.draw.rect(PANTALLA, CIBER_BLAU, boto_mov)
        pygame.draw.rect(PANTALLA, CIBER_BLAU, boto_salt)
        pygame.draw.rect(PANTALLA, CIBER_BLAU, boto_gadg)
        pygame.draw.rect(PANTALLA, CIBER_BLAU, boto_canvi)
        pygame.draw.rect(PANTALLA, CIBER_BLAU, boto_inter)

        pygame.draw.rect(PANTALLA, TARONJA, boto_tornar3)

        pygame.draw.rect(PANTALLA, CIBER_BLAU, boto_mov2)
        pygame.draw.rect(PANTALLA, CIBER_BLAU, boto_salt2)
        pygame.draw.rect(PANTALLA, CIBER_BLAU, boto_gadg2)
        pygame.draw.rect(PANTALLA, CIBER_BLAU, boto_canvi2)
        pygame.draw.rect(PANTALLA, CIBER_BLAU, boto_inter2)

        mostrar_text("MOVIMENT", font_mes_petita, NEGRE, boto_mov.centerx, boto_mov.centery)
        mostrar_text("SALT", font_mes_petita, NEGRE, boto_salt.centerx, boto_salt.centery)
        mostrar_text("GADGET", font_mes_petita, NEGRE, boto_gadg.centerx, boto_gadg.centery)
        mostrar_text("CANVI DE MANS", font_mes_petita, NEGRE, boto_canvi.centerx, boto_canvi.centery)
        mostrar_text("INTERACCIO AMB COSES", font_mes_petita, NEGRE, boto_inter.centerx, boto_inter.centery)

        mostrar_text("TORNAR", font_mes_petita, NEGRE, boto_tornar3.centerx, boto_tornar3.centery)

        mostrar_text("A/D", font_mes_petita, NEGRE, boto_mov2.centerx, boto_mov2.centery)
        mostrar_text("BARRA D'ESPAI", font_mes_petita, NEGRE, boto_salt2.centerx, boto_salt2.centery)
        mostrar_text("Q", font_mes_petita, NEGRE, boto_gadg2.centerx, boto_gadg2.centery)
        mostrar_text("F", font_mes_petita, NEGRE, boto_canvi2.centerx, boto_canvi2.centery)
        mostrar_text("E", font_mes_petita, NEGRE, boto_inter2.centerx, boto_inter2.centery)

        actualitzar_pantalla_amb_transicio()

def dibuixar_barra_volum(barra, volum):
    pygame.draw.rect(PANTALLA, GRIS, barra)
    amplada_farcida = int(barra.width * volum)
    barra_farcida = pygame.Rect(barra.x, barra.y, amplada_farcida, barra.height)
    pygame.draw.rect(PANTALLA, CIBER_BLAU, barra_farcida)

def pantalla_so():
    global volum_musica, volum_sfx, arrossegar_musica, arrossegar_sfx
    en_so = True

    boto_musica = pygame.Rect(144, 150, 150, 50)
    barra_musica = pygame.Rect(320, 160, 200, 30)
    boto_SFX = pygame.Rect(144, 230, 150, 50)
    barra_SFX = pygame.Rect(320, 240, 200, 30)
    boto_tornar4 = pygame.Rect(369, 390, 150, 50)

    while en_so:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == QUIT:
                iniciar_transicio()
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key in (K_RETURN, K_KP_ENTER, K_ESCAPE):
                    iniciar_transicio()
                    return "TORNAR"

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    if barra_musica.collidepoint(event.pos):
                        arrossegar_musica = True
                        pos_relativa = event.pos[0] - barra_musica.x
                        volum_musica = max(0.0, min(1.0, pos_relativa / barra_musica.width))
                        pygame.mixer.music.set_volume(volum_musica)
                    elif barra_SFX.collidepoint(event.pos):
                        arrossegar_sfx = True
                        pos_relativa = event.pos[0] - barra_SFX.x
                        volum_sfx = max(0.0, min(1.0, pos_relativa / barra_SFX.width))

            elif event.type == MOUSEBUTTONUP:
                if event.button == 1:
                    arrossegar_musica = False
                    arrossegar_sfx = False

            elif event.type == MOUSEMOTION:
                if arrossegar_musica:
                    pos_relativa = event.pos[0] - barra_musica.x
                    volum_musica = max(0.0, min(1.0, pos_relativa / barra_musica.width))
                    pygame.mixer.music.set_volume(volum_musica)
                elif arrossegar_sfx:
                    pos_relativa = event.pos[0] - barra_SFX.x
                    volum_sfx = max(0.0, min(1.0, pos_relativa / barra_SFX.width))

        PANTALLA.fill(NEGRE)
        mostrar_text("SO", font_gran, BLANC, AMPLADA // 2, 100)

        pygame.draw.rect(PANTALLA, CIBER_BLAU, boto_musica)
        pygame.draw.rect(PANTALLA, CIBER_BLAU, boto_SFX)
        pygame.draw.rect(PANTALLA, TARONJA, boto_tornar4)

        mostrar_text("MUSICA", font_petita, NEGRE, boto_musica.centerx, boto_musica.centery)
        mostrar_text("SFX", font_petita, NEGRE, boto_SFX.centerx, boto_SFX.centery)
        mostrar_text("TORNAR", font_petita, NEGRE, boto_tornar4.centerx, boto_tornar4.centery)

        dibuixar_barra_volum(barra_musica, volum_musica)
        dibuixar_barra_volum(barra_SFX, volum_sfx)

        actualitzar_pantalla_amb_transicio()

def pantalla_pantalla():
    pygame.display.toggle_fullscreen()
    return "TORNAR"

def pantalla_pausa_tutorial():
    en_pantalla_pausa_tutorial = True
    opcio_seleccionada = 0

    boto_ajustaments2 = pygame.Rect(369, 150, 150, 50)
    boto_tornar5 = pygame.Rect(369, 230, 150, 50)
    boto_sortir = pygame.Rect(369, 310, 150, 50)

    botons = [boto_ajustaments2, boto_tornar5, boto_sortir]

    while en_pantalla_pausa_tutorial:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == QUIT:
                iniciar_transicio()
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    iniciar_transicio()
                    return "JUGANT_TUTORIAL"
                elif event.key in (K_UP, K_LEFT):
                    opcio_seleccionada = (opcio_seleccionada - 1) % len(botons)
                elif event.key in (K_DOWN, K_RIGHT):
                    opcio_seleccionada = (opcio_seleccionada + 1) % len(botons)
                elif event.key in (K_RETURN, K_KP_ENTER):
                    iniciar_transicio()
                    if opcio_seleccionada == 0:
                        return "AJUSTAMENTS3"
                    elif opcio_seleccionada == 1:
                        return "JUGANT_TUTORIAL"
                    elif opcio_seleccionada == 2:
                        iniciar_transicio(aturar_musica=True)
                        return "INICI"

        PANTALLA.fill(NEGRE)
        mostrar_text("PAUSA", font_gran, BLANC, AMPLADA // 2, 50)

        for i, boto in enumerate(botons):
            if i == opcio_seleccionada:
                color_boto = TARONJA
            elif boto == boto_sortir:
                color_boto = VERMELL
            else:
                color_boto = CIBER_BLAU
            pygame.draw.rect(PANTALLA, color_boto, boto)

        mostrar_text("AJUSTAMENTS", font_petita, NEGRE, boto_ajustaments2.centerx, boto_ajustaments2.centery)
        mostrar_text("TORNAR", font_petita, NEGRE, boto_tornar5.centerx, boto_tornar5.centery)
        mostrar_text("MENÚ PRINCIPAL", font_petita, NEGRE, boto_sortir.centerx, boto_sortir.centery)

        actualitzar_pantalla_amb_transicio()

def pantalla_pausa_nivell1():
    en_pantalla_pausa_nivell1 = True
    opcio_seleccionada = 0

    boto_ajustaments2 = pygame.Rect(369, 150, 150, 50)
    boto_tornar5 = pygame.Rect(369, 230, 150, 50)
    boto_sortir = pygame.Rect(369, 310, 150, 50)

    botons = [boto_ajustaments2, boto_tornar5, boto_sortir]

    while en_pantalla_pausa_nivell1:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == QUIT:
                iniciar_transicio()
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    iniciar_transicio()
                    return "JUGANT_NIVELL1_PANTALLA1"
                elif event.key in (K_UP, K_LEFT):
                    opcio_seleccionada = (opcio_seleccionada - 1) % len(botons)
                elif event.key in (K_DOWN, K_RIGHT):
                    opcio_seleccionada = (opcio_seleccionada + 1) % len(botons)
                elif event.key in (K_RETURN, K_KP_ENTER):
                    iniciar_transicio()
                    if opcio_seleccionada == 0:
                        return "AJUSTAMENTS3"
                    elif opcio_seleccionada == 1:
                        return "JUGANT_NIVELL1_PANTALLA1"
                    elif opcio_seleccionada == 2:
                        iniciar_transicio(aturar_musica=True)
                        return "INICI"

        PANTALLA.fill(NEGRE)
        mostrar_text("PAUSA", font_gran, BLANC, AMPLADA // 2, 50)

        for i, boto in enumerate(botons):
            if i == opcio_seleccionada:
                color_boto = TARONJA
            elif boto == boto_sortir:
                color_boto = VERMELL
            else:
                color_boto = CIBER_BLAU
            pygame.draw.rect(PANTALLA, color_boto, boto)

        mostrar_text("AJUSTAMENTS", font_petita, NEGRE, boto_ajustaments2.centerx, boto_ajustaments2.centery)
        mostrar_text("TORNAR", font_petita, NEGRE, boto_tornar5.centerx, boto_tornar5.centery)
        mostrar_text("MENÚ PRINCIPAL", font_petita, NEGRE, boto_sortir.centerx, boto_sortir.centery)

        actualitzar_pantalla_amb_transicio()

def pantalla_pausa_nivell2():
    en_pantalla_pausa_nivell2 = True
    opcio_seleccionada = 0

    boto_ajustaments2 = pygame.Rect(369, 150, 150, 50)
    boto_tornar5 = pygame.Rect(369, 230, 150, 50)
    boto_sortir = pygame.Rect(369, 310, 150, 50)

    botons = [boto_ajustaments2, boto_tornar5, boto_sortir]

    while en_pantalla_pausa_nivell2:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == QUIT:
                iniciar_transicio()
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    iniciar_transicio()
                    return "JUGANT_NIVELL2_PANTALLA1"
                elif event.key in (K_UP, K_LEFT):
                    opcio_seleccionada = (opcio_seleccionada - 1) % len(botons)
                elif event.key in (K_DOWN, K_RIGHT):
                    opcio_seleccionada = (opcio_seleccionada + 1) % len(botons)
                elif event.key in (K_RETURN, K_KP_ENTER):
                    iniciar_transicio()
                    if opcio_seleccionada == 0:
                        return "AJUSTAMENTS3"
                    elif opcio_seleccionada == 1:
                        return "JUGANT_NIVELL2_PANTALLA1"
                    elif opcio_seleccionada == 2:
                        iniciar_transicio(aturar_musica=True)
                        return "INICI"

        PANTALLA.fill(NEGRE)
        mostrar_text("PAUSA", font_gran, BLANC, AMPLADA // 2, 50)

        for i, boto in enumerate(botons):
            if i == opcio_seleccionada:
                color_boto = TARONJA
            elif boto == boto_sortir:
                color_boto = VERMELL
            else:
                color_boto = CIBER_BLAU
            pygame.draw.rect(PANTALLA, color_boto, boto)

        mostrar_text("AJUSTAMENTS", font_petita, NEGRE, boto_ajustaments2.centerx, boto_ajustaments2.centery)
        mostrar_text("TORNAR", font_petita, NEGRE, boto_tornar5.centerx, boto_tornar5.centery)
        mostrar_text("MENÚ PRINCIPAL", font_petita, NEGRE, boto_sortir.centerx, boto_sortir.centery)

        actualitzar_pantalla_amb_transicio()

def pantalla_pausa_nivell3():
    en_pantalla_pausa_nivell3 = True
    opcio_seleccionada = 0

    boto_ajustaments2 = pygame.Rect(369, 150, 150, 50)
    boto_tornar5 = pygame.Rect(369, 230, 150, 50)
    boto_sortir = pygame.Rect(369, 310, 150, 50)

    botons = [boto_ajustaments2, boto_tornar5, boto_sortir]

    while en_pantalla_pausa_nivell3:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == QUIT:
                iniciar_transicio()
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    iniciar_transicio()
                    return "JUGANT_NIVELL3_PANTALLA1"
                elif event.key in (K_UP, K_LEFT):
                    opcio_seleccionada = (opcio_seleccionada - 1) % len(botons)
                elif event.key in (K_DOWN, K_RIGHT):
                    opcio_seleccionada = (opcio_seleccionada + 1) % len(botons)
                elif event.key in (K_RETURN, K_KP_ENTER):
                    iniciar_transicio()
                    if opcio_seleccionada == 0:
                        return "AJUSTAMENTS3"
                    elif opcio_seleccionada == 1:
                        return "JUGANT_NIVELL3_PANTALLA1"
                    elif opcio_seleccionada == 2:
                        iniciar_transicio(aturar_musica=True)
                        return "INICI"

        PANTALLA.fill(NEGRE)
        mostrar_text("PAUSA", font_gran, BLANC, AMPLADA // 2, 50)

        for i, boto in enumerate(botons):
            if i == opcio_seleccionada:
                color_boto = TARONJA
            elif boto == boto_sortir:
                color_boto = VERMELL
            else:
                color_boto = CIBER_BLAU
            pygame.draw.rect(PANTALLA, color_boto, boto)

        mostrar_text("AJUSTAMENTS", font_petita, NEGRE, boto_ajustaments2.centerx, boto_ajustaments2.centery)
        mostrar_text("TORNAR", font_petita, NEGRE, boto_tornar5.centerx, boto_tornar5.centery)
        mostrar_text("MENÚ PRINCIPAL", font_petita, NEGRE, boto_sortir.centerx, boto_sortir.centery)

        actualitzar_pantalla_amb_transicio()

jugador_rect = None
mirant_dreta = True
vel_y = 0
en_terra = True

FRAMES_CAMINAR_DURADA = 150
frame_caminar_index = 0
temps_ultim_canvi_frame = 0

def carregar_animacio_jugador(fitxer_quiet, fitxer_frame1, fitxer_frame2, fitxer_salt, amplada, alcada):
    fitxers = {
        "quiet": fitxer_quiet,
        "frame1": fitxer_frame1,
        "frame2": fitxer_frame2,
        "salt": fitxer_salt,
    }
    dreta = {}
    esquerra = {}

    for clau, fitxer in fitxers.items():
        ruta_completa = ruta_imatges("Jugador", fitxer)
        img = pygame.image.load(ruta_completa).convert_alpha()

        img_escalada = pygame.transform.scale(img, (amplada, alcada))
        dreta[clau] = img_escalada
        esquerra[clau] = pygame.transform.flip(img_escalada, True, False)

    return dreta, esquerra

PUNT_MA_DRETA = {
    "quiet":  (33.5, 48.0),
    "frame1": (31.8, 45.4),
    "frame2": (30.1, 43.7),
    "salt":   (30.3, 40.1),
}

def obtenir_clau_frame_jugador(caminant, en_terra_actual):
    global frame_caminar_index, temps_ultim_canvi_frame

    if not en_terra_actual:
        return "salt"

    if caminant:
        temps_actual = pygame.time.get_ticks()
        if temps_actual - temps_ultim_canvi_frame > FRAMES_CAMINAR_DURADA:
            frame_caminar_index = 1 - frame_caminar_index
            temps_ultim_canvi_frame = temps_actual
        return "frame1" if frame_caminar_index == 0 else "frame2"

    frame_caminar_index = 0
    return "quiet"

def obtenir_frame_jugador(imatges, caminant, en_terra_actual):
    clau = obtenir_clau_frame_jugador(caminant, en_terra_actual)
    return imatges[clau]

def punt_origen_laser(jugador_rect_actual, mirant_dreta_actual, clau_frame):
    ma_x, ma_y = PUNT_MA_DRETA.get(clau_frame, PUNT_MA_DRETA["quiet"])
    if not mirant_dreta_actual:
        ma_x = 40 - ma_x
    return (jugador_rect_actual.left + ma_x, jugador_rect_actual.top + ma_y)

moment_pausa_inici = None
temps_pausa_acumulat = 0

def temps_joc():
    return pygame.time.get_ticks() - temps_pausa_acumulat

def nivell_tutorial(reiniciar=False, pos_x_inici=100):
    global jugador_rect, mirant_dreta, vel_y, en_terra, textos_vistos
    jugant_tutorial = True
    canviar_musica("tut.mp3")

    amplada_jugador, alcada_jugador = 40, 80
    jugador_img_dreta, jugador_img_esquerra = carregar_animacio_jugador(
        "Alex_quiet.png", "Alex_frame1.png", "Alex_frame2.png", "Alex_salt.png",
        amplada_jugador, alcada_jugador
    )

    if reiniciar or jugador_rect is None:
        jugador_rect = jugador_img_dreta["quiet"].get_rect(topleft=(pos_x_inici, 444))
        if pos_x_inici > 400:
            mirant_dreta = False
        else:
            mirant_dreta = True
        vel_y = 0
        en_terra = True

    GRAVETAT = 0.8
    FORCA_SALT = -14
    ALTURA_SOL = 390
    LIMIT_ESQUERRA = 20
    LIMIT_DRETA = 870
    PORTA_SORTIDA = pygame.Rect(840, 333, 50, 100)

    missatge_1 = "BENVINGUT  AL  TUTORIAL  DE  P . R . A . I . L ."
    missatge_2 = "AQUÍ  APRENDRÀS  LES  MECÀNIQUES  BÀSIQUES  PER  SABER  JUGAR"

    if textos_vistos["tutorial"]:
        text_mostrat_1 = missatge_1
        text_mostrat_2 = missatge_2
        index_1 = len(missatge_1)
        index_2 = len(missatge_2)
    else:
        text_mostrat_1 = ""
        text_mostrat_2 = ""
        index_1 = 0
        index_2 = 0

    velocitat_text = 40
    ultim_temps_text = pygame.time.get_ticks()

    while jugant_tutorial:
        clock.tick(60)
        en_porta = jugador_rect.colliderect(PORTA_SORTIDA)

        for event in pygame.event.get():
            if event.type == QUIT:
                iniciar_transicio()
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    return "PAUSAT"
                if event.key == K_e and en_porta:
                    iniciar_transicio()
                    return "JUGANT_TUTORIAL2"

        tecles = pygame.key.get_pressed()
        if tecles[K_a]:
            jugador_rect.x -= 5
            mirant_dreta = False
        elif tecles[K_d]:
            jugador_rect.x += 5
            mirant_dreta = True
        if (tecles[K_w]) and en_terra:
            vel_y = FORCA_SALT
            en_terra = False

        vel_y += GRAVETAT
        jugador_rect.y += vel_y

        if jugador_rect.y >= ALTURA_SOL:
            jugador_rect.y = ALTURA_SOL
            vel_y = 0
            en_terra = True

        if jugador_rect.x <= LIMIT_ESQUERRA:
            jugador_rect.x = LIMIT_ESQUERRA
        if jugador_rect.right >= LIMIT_DRETA:
            jugador_rect.right = LIMIT_DRETA

        temps_actual = pygame.time.get_ticks()
        if temps_actual - ultim_temps_text > velocitat_text:
            if index_1 < len(missatge_1):
                text_mostrat_1 += missatge_1[index_1]
                index_1 += 1
                ultim_temps_text = temps_actual
            elif index_2 < len(missatge_2):
                text_mostrat_2 += missatge_2[index_2]
                index_2 += 1
                ultim_temps_text = temps_actual
            else:
                textos_vistos["tutorial"] = True

        PANTALLA.blit(fons_tutorial, (0, 0))
        text_benvinguda = pygame.Rect(444, 150, 0, 0)
        text_benvinguda2 = pygame.Rect(444, 175, 0, 0)

        if len(text_mostrat_1) > 0:
            mostrar_text(text_mostrat_1, font_petita, NEGRE, text_benvinguda.centerx, text_benvinguda.centery)
        if len(text_mostrat_2) > 0:
            mostrar_text(text_mostrat_2, font_petita, NEGRE, text_benvinguda2.centerx, text_benvinguda2.centery)

        if en_porta:
            mostrar_text("E", font_petita, NEGRE, PORTA_SORTIDA.centerx, PORTA_SORTIDA.top - 20)

        imatges_jugador_actuals = jugador_img_dreta if mirant_dreta else jugador_img_esquerra
        caminant = tecles[K_a] or tecles[K_d]
        PANTALLA.blit(obtenir_frame_jugador(imatges_jugador_actuals, caminant, en_terra), jugador_rect)

        actualitzar_pantalla_amb_transicio()


def nivell_tutorial2(reiniciar=False, pos_x_inici=50):
    global jugador_rect, mirant_dreta, vel_y, en_terra, textos_vistos, tresors_recollits
    jugant = True

    amplada_jugador, alcada_jugador = 40, 80
    jugador_img_dreta, jugador_img_esquerra = carregar_animacio_jugador(
        "Alex_quiet.png", "Alex_frame1.png", "Alex_frame2.png", "Alex_salt.png",
        amplada_jugador, alcada_jugador
    )

    amplada_mur = img_mur.get_width()
    alcada_mur = img_mur.get_height()

    amplada_prestatg = img_prestatg.get_width()
    alcada_prestatg = img_prestatg.get_height()

    rect_tresor = tutorial2_copa.get_rect(topleft=(150, 150))

    if reiniciar or jugador_rect is None:
        jugador_rect = jugador_img_dreta["quiet"].get_rect(topleft=(pos_x_inici, 444))
        if pos_x_inici > 400:
            mirant_dreta = False
        else:
            mirant_dreta = True
        vel_y = 0
        en_terra = True

    GRAVETAT = 0.8
    FORCA_SALT = -14
    ALTURA_SOL = 390
    LIMIT_ESQUERRA = 20
    LIMIT_DRETA = 870
    PORTA_SORTIDA = pygame.Rect(840, 333, 50, 100)
    PORTA_SORTIDA2 = pygame.Rect(0, 333, 50, 100)

    murs = [
        pygame.Rect(300, 400, amplada_mur, alcada_mur),
        pygame.Rect(500, 350, amplada_mur, alcada_mur),
        pygame.Rect(700, 300, amplada_mur, alcada_mur),
        pygame.Rect(500, 220, amplada_mur, alcada_mur),
    ]
    prestatgs = [
        pygame.Rect(150, 200, amplada_prestatg, alcada_prestatg),
    ]

    missatge_1 = "EN  AQUEST  JOC  EL  TEU  OBJECTIU  ÉS  CONSEGUIR"
    missatge_2 = "TOTS  ELS  OBJECTES  DE  VALOR  DE  DIFERENTS  LLOCS."
    missatge_3 = "I  PER  AIXÒ  MATEIX,  HAS  DE  FER  PARKOUR..."

    if textos_vistos["tutorial2"]:
        text_mostrat_1 = missatge_1
        text_mostrat_2 = missatge_2
        text_mostrat_3 = missatge_3
        index_1 = len(missatge_1)
        index_2 = len(missatge_2)
        index_3 = len(missatge_3)
    else:
        text_mostrat_1 = ""
        text_mostrat_2 = ""
        text_mostrat_3 = ""
        index_1 = 0
        index_2 = 0
        index_3 = 0

    velocitat_text = 40
    ultim_temps_text = pygame.time.get_ticks()

    while jugant:
        clock.tick(60)
        en_porta = jugador_rect.colliderect(PORTA_SORTIDA)
        en_porta2 = jugador_rect.colliderect(PORTA_SORTIDA2)

        if not tresors_recollits["tutorial2_copa"]:
            if jugador_rect.colliderect(rect_tresor):
                tresors_recollits["tutorial2_copa"] = True
                if so_recollit:
                    so_recollit.set_volume(volum_sfx)
                    so_recollit.play()

        for event in pygame.event.get():
            if event.type == QUIT:
                iniciar_transicio()
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    return "PAUSAT2"
                if event.key == K_e and en_porta and tresors_recollits["tutorial2_copa"]:
                    iniciar_transicio()
                    return "JUGANT_TUTORIAL3"
                if event.key == K_e and en_porta2:
                    iniciar_transicio()
                    return "JUGANT_TUTORIAL"

        tecles = pygame.key.get_pressed()
        dx = 0
        if tecles[K_a]:
            dx = -5
            mirant_dreta = False
        elif tecles[K_d]:
            dx = 5
            mirant_dreta = True

        jugador_rect.x += dx

        if jugador_rect.x <= LIMIT_ESQUERRA:
            jugador_rect.x = LIMIT_ESQUERRA
        if jugador_rect.right >= LIMIT_DRETA:
            jugador_rect.right = LIMIT_DRETA

        for mur in murs:
            if jugador_rect.colliderect(mur):
                if dx > 0:
                    jugador_rect.right = mur.left
                elif dx < 0:
                    jugador_rect.left = mur.right

        for prestatg in prestatgs:
            if jugador_rect.colliderect(prestatg):
                if dx > 0:
                    jugador_rect.right = prestatg.left
                elif dx < 0:
                    jugador_rect.left = prestatg.right

        if (tecles[K_w]) and en_terra:
            vel_y = FORCA_SALT
            en_terra = False

        vel_y += GRAVETAT

        jugador_rect.y += vel_y
        en_terra = False

        for mur in murs:
            if jugador_rect.colliderect(mur):
                if vel_y > 0:
                    jugador_rect.bottom = mur.top
                    vel_y = 0
                    en_terra = True
                elif vel_y < 0:
                    jugador_rect.top = mur.bottom
                    vel_y = 0

        for prestatg in prestatgs:
            if jugador_rect.colliderect(prestatg):
                if vel_y > 0:
                    jugador_rect.bottom = prestatg.top
                    vel_y = 0
                    en_terra = True
                elif vel_y < 0:
                    jugador_rect.top = prestatg.bottom
                    vel_y = 0

        if jugador_rect.y >= ALTURA_SOL:
            jugador_rect.y = ALTURA_SOL
            vel_y = 0
            en_terra = True

        temps_actual = pygame.time.get_ticks()
        if temps_actual - ultim_temps_text > velocitat_text:
            if index_1 < len(missatge_1):
                text_mostrat_1 += missatge_1[index_1]
                index_1 += 1
                ultim_temps_text = temps_actual
            elif index_2 < len(missatge_2):
                text_mostrat_2 += missatge_2[index_2]
                index_2 += 1
                ultim_temps_text = temps_actual
            elif index_3 < len(missatge_3):
                text_mostrat_3 += missatge_3[index_3]
                index_3 += 1
                ultim_temps_text = temps_actual
            else:
                textos_vistos["tutorial2"] = True

        PANTALLA.blit(fons_tutorial, (0, 0))

        for mur in murs:
            PANTALLA.blit(img_mur, (mur.x, mur.y))
        for prestatg in prestatgs:
            PANTALLA.blit(img_prestatg, (prestatg.x, prestatg.y))

        if not tresors_recollits["tutorial2_copa"]:
            PANTALLA.blit(tutorial2_copa, rect_tresor)

        text_parkour = pygame.Rect(580, 100, 0, 0)
        text_parkour2 = pygame.Rect(580, 125, 0, 0)
        text_parkour3 = pygame.Rect(580, 150, 0, 0)

        if len(text_mostrat_1) > 0:
            mostrar_text(text_mostrat_1, font_petita, NEGRE, text_parkour.centerx, text_parkour.centery)
        if len(text_mostrat_2) > 0:
            mostrar_text(text_mostrat_2, font_petita, NEGRE, text_parkour2.centerx, text_parkour2.centery)
        if len(text_mostrat_3) > 0:
            mostrar_text(text_mostrat_3, font_petita, NEGRE, text_parkour3.centerx, text_parkour3.centery)

        if en_porta:
            if tresors_recollits["tutorial2_copa"]:
                mostrar_text("E", font_petita, NEGRE, PORTA_SORTIDA.centerx, PORTA_SORTIDA.top - 20)
            else:
                mostrar_text("Falta tresor", font_petita, VERMELL, PORTA_SORTIDA.centerx -100, PORTA_SORTIDA.top)

        if en_porta2:
            mostrar_text("E", font_petita, NEGRE, PORTA_SORTIDA2.centerx, PORTA_SORTIDA2.top - 20)

        imatges_jugador_actuals = jugador_img_dreta if mirant_dreta else jugador_img_esquerra
        caminant = tecles[K_a] or tecles[K_d]
        PANTALLA.blit(obtenir_frame_jugador(imatges_jugador_actuals, caminant, en_terra), jugador_rect)

        actualitzar_pantalla_amb_transicio()


def nivell_tutorial3(reiniciar=False, pos_x_inici=50):
    global jugador_rect, mirant_dreta, vel_y, en_terra, textos_vistos, moment_pausa_inici, temps_pausa_acumulat
    if moment_pausa_inici is not None:
        temps_pausa_acumulat += pygame.time.get_ticks() - moment_pausa_inici
        moment_pausa_inici = None
    jugant = True
    game_over = False

    amplada_jugador, alcada_jugador = 40, 80
    jugador_img_dreta, jugador_img_esquerra = carregar_animacio_jugador(
        "Alex_quiet.png", "Alex_frame1.png", "Alex_frame2.png", "Alex_salt.png",
        amplada_jugador, alcada_jugador
    )

    amplada_mur = img_mur.get_width()
    alcada_mur = img_mur.get_height()

    if reiniciar or jugador_rect is None:
        jugador_rect = jugador_img_dreta["quiet"].get_rect(topleft=(pos_x_inici, 444))
        if pos_x_inici > 400:
            mirant_dreta = False
        else:
            mirant_dreta = True
        vel_y = 0
        en_terra = True

    rect_agente = agente_img_base.get_rect(topleft=(450, 390))
    rect_deteccio = deteccio_img_base.get_rect()

    agente_mirant_dreta = False
    ultim_canvi_agente = temps_joc()

    GRAVETAT = 0.8
    FORCA_SALT = -14
    ALTURA_SOL = 390
    LIMIT_ESQUERRA = 20
    LIMIT_DRETA = 870
    PORTA_SORTIDA = pygame.Rect(840, 333, 50, 100)
    PORTA_SORTIDA2 = pygame.Rect(0, 333, 50, 100)

    murs = [
        pygame.Rect(300, 380, amplada_mur, alcada_mur),
        pygame.Rect(445, 350, amplada_mur, alcada_mur),
        pygame.Rect(590, 380, amplada_mur, alcada_mur),
    ]

    missatge_1 = "ESQUIVAR  A  GUÀRDIES..."

    if textos_vistos["tutorial3"]:
        text_mostrat_1 = missatge_1
        index_1 = len(missatge_1)
    else:
        text_mostrat_1 = ""
        index_1 = 0

    velocitat_text = 40
    ultim_temps_text = pygame.time.get_ticks()

    while jugant:
        clock.tick(60)
        en_porta = jugador_rect.colliderect(PORTA_SORTIDA)
        en_porta2 = jugador_rect.colliderect(PORTA_SORTIDA2)

        for event in pygame.event.get():
            if event.type == QUIT:
                iniciar_transicio()
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if game_over:
                    if event.key in (K_RETURN, K_KP_ENTER):
                        iniciar_transicio()
                        return "REINICIAR"
                else:
                    if event.key == K_ESCAPE:
                        moment_pausa_inici = pygame.time.get_ticks()
                        iniciar_transicio()
                        return "PAUSAT3"
                    if event.key == K_e and en_porta:
                        iniciar_transicio()
                        return "JUGANT_TUTORIAL4"
                    if event.key == K_e and en_porta2:
                        iniciar_transicio()
                        return "JUGANT_TUTORIAL2"

        if not game_over:
            temps_actual = temps_joc()
            if temps_actual - ultim_canvi_agente >= 7000:
                agente_mirant_dreta = not agente_mirant_dreta
                ultim_canvi_agente = temps_actual

            altura_ojos = rect_agente.top + int(rect_agente.height * 0.22)

            if agente_mirant_dreta:
                rect_deteccio.left = rect_agente.right - 5
                rect_deteccio.centery = altura_ojos
            else:
                rect_deteccio.right = rect_agente.left + 5
                rect_deteccio.centery = altura_ojos

            tecles = pygame.key.get_pressed()
            dx = 0
            if tecles[K_a]:
                jugador_rect.x -= 5
                mirant_dreta = False
            elif tecles[K_d]:
                jugador_rect.x += 5
                mirant_dreta = True
            if tecles[K_w] and en_terra:
                vel_y = FORCA_SALT
                en_terra = False

            vel_y += GRAVETAT
            jugador_rect.y += vel_y

            for mur in murs:
                if jugador_rect.colliderect(mur):
                    if dx > 0:
                        jugador_rect.right = mur.left
                    elif dx < 0:
                        jugador_rect.left = mur.right

            if jugador_rect.y >= ALTURA_SOL:
                jugador_rect.y = ALTURA_SOL
                vel_y = 0
                en_terra = True

            temps_actual = pygame.time.get_ticks()
            if temps_actual - ultim_temps_text > velocitat_text:
                if index_1 < len(missatge_1):
                    text_mostrat_1 += missatge_1[index_1]
                    index_1 += 1
                    ultim_temps_text = temps_actual
                else:
                    textos_vistos["tutorial3"] = True

            if jugador_rect.x <= LIMIT_ESQUERRA:
                jugador_rect.x = LIMIT_ESQUERRA
            if jugador_rect.right >= LIMIT_DRETA:
                jugador_rect.right = LIMIT_DRETA

            if jugador_rect.colliderect(rect_deteccio):
                game_over = True

            for mur in murs:
                if jugador_rect.colliderect(mur):
                    if vel_y > 0:
                        jugador_rect.bottom = mur.top
                        vel_y = 0
                        en_terra = True
                    elif vel_y < 0:
                        jugador_rect.top = mur.bottom
                        vel_y = 0

        PANTALLA.blit(fons_tutorial, (0, 0))

        for mur in murs:
            PANTALLA.blit(img_mur, (mur.x, mur.y))

        text_guàrdia = pygame.Rect(580, 100, 0, 0)

        if len(text_mostrat_1) > 0:
            mostrar_text(text_mostrat_1, font_petita, NEGRE, text_guàrdia.centerx, text_guàrdia.centery)

        if en_porta and not game_over:
            mostrar_text("E", font_petita, NEGRE, PORTA_SORTIDA.centerx, PORTA_SORTIDA.top - 20)

        if en_porta2 and not game_over:
            mostrar_text("E", font_petita, NEGRE, PORTA_SORTIDA2.centerx, PORTA_SORTIDA2.top - 20)

        if agente_mirant_dreta:
            PANTALLA.blit(agente_img_dreta, rect_agente)
            PANTALLA.blit(deteccio_img_dreta, rect_deteccio)
        else:
            PANTALLA.blit(agente_img_esquerra, rect_agente)
            PANTALLA.blit(deteccio_img_esquerra, rect_deteccio)

        imatges_jugador_actuals = jugador_img_dreta if mirant_dreta else jugador_img_esquerra
        caminant = tecles[K_a] or tecles[K_d]
        PANTALLA.blit(obtenir_frame_jugador(imatges_jugador_actuals, caminant, en_terra), jugador_rect)

        if game_over:
            mostrar_text("GAME  OVER", font_gran, VERMELL, AMPLADA // 2, ALCADA // 2 - 20)
            mostrar_text("Prem  ENTER  per  reiniciar", font_petita, BLANC, AMPLADA // 2, ALCADA // 2 + 40)

        actualitzar_pantalla_amb_transicio()

def nivell_tutorial4(reiniciar=False, pos_x_inici=50):
    global jugador_rect, mirant_dreta, vel_y, en_terra, textos_vistos, moment_pausa_inici, temps_pausa_acumulat

    if moment_pausa_inici is not None:
        temps_pausa_acumulat += pygame.time.get_ticks() - moment_pausa_inici
        moment_pausa_inici = None

    jugant = True
    game_over = False

    amplada_jugador, alcada_jugador = 40, 80
    jugador_img_dreta, jugador_img_esquerra = carregar_animacio_jugador(
        "Alex_quiet.png", "Alex_frame1.png", "Alex_frame2.png", "Alex_salt.png",
        amplada_jugador, alcada_jugador
    )

    if reiniciar or jugador_rect is None:
        jugador_rect = jugador_img_dreta["quiet"].get_rect(topleft=(pos_x_inici, 444))
        if pos_x_inici > 400:
            mirant_dreta = False
        else:
            mirant_dreta = True
        vel_y = 0
        en_terra = True

    GRAVETAT = 0.8
    FORCA_SALT = -14
    ALTURA_SOL = 390
    LIMIT_ESQUERRA = 20
    LIMIT_DRETA = 870
    PORTA_SORTIDA = pygame.Rect(840, 333, 50, 100)
    PORTA_SORTIDA2 = pygame.Rect(0, 333, 50, 100)

    missatge_1 = "O  ESQUIVAR  A  CÀMERES..."
    if textos_vistos["tutorial4"]:
        text_mostrat_1 = missatge_1
        index_1 = len(missatge_1)
    else:
        text_mostrat_1 = ""
        index_1 = 0

    velocitat_text = 40
    ultim_temps_text = pygame.time.get_ticks()

    camara_x = AMPLADA // 2
    camara_y = 50
    camara_rect = camara_img.get_rect(center=(camara_x, camara_y))
    amplada_cono_base = 250

    superficie_cono = pygame.Surface((AMPLADA, ALCADA), pygame.SRCALPHA)

    while jugant:
        clock.tick(60)
        en_porta = jugador_rect.colliderect(PORTA_SORTIDA)
        en_porta2 = jugador_rect.colliderect(PORTA_SORTIDA2)

        for event in pygame.event.get():
            if event.type == QUIT:
                iniciar_transicio()
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if game_over:
                    if event.key in (K_RETURN, K_KP_ENTER):
                        iniciar_transicio()
                        return "REINICIAR"
                if event.key == K_ESCAPE:
                    moment_pausa_inici = pygame.time.get_ticks()
                    return "PAUSAT4"
                if event.key == K_e and en_porta:
                    iniciar_transicio()
                    return "JUGANT_TUTORIAL5"
                if event.key == K_e and en_porta2:
                    iniciar_transicio()
                    return "JUGANT_TUTORIAL3"

        temps_actual = temps_joc()
        en_vermell = (temps_actual % 6000) >= 3000

        if not game_over:
            tecles = pygame.key.get_pressed()
            if tecles[K_a] or tecles[K_LEFT]:
                jugador_rect.x -= 5
                mirant_dreta = False
            elif tecles[K_d] or tecles[K_RIGHT]:
                jugador_rect.x += 5
                mirant_dreta = True
            if (tecles[K_w] or tecles[K_SPACE]) and en_terra:
                vel_y = FORCA_SALT
                en_terra = False

            vel_y += GRAVETAT
            jugador_rect.y += vel_y

            if jugador_rect.y >= ALTURA_SOL:
                jugador_rect.y = ALTURA_SOL
                vel_y = 0
                en_terra = True
            if jugador_rect.x <= LIMIT_ESQUERRA:
                jugador_rect.x = LIMIT_ESQUERRA
            if jugador_rect.right >= LIMIT_DRETA:
                jugador_rect.right = LIMIT_DRETA

            temps_actual = pygame.time.get_ticks()
            if temps_actual - ultim_temps_text > velocitat_text:
                if index_1 < len(missatge_1):
                    text_mostrat_1 += missatge_1[index_1]
                    index_1 += 1
                    ultim_temps_text = temps_actual
                else:
                    textos_vistos["tutorial4"] = True

            detectat = False
            if jugador_rect.top < (ALTURA_SOL + alcada_jugador) and jugador_rect.bottom > camara_y:
                distancia_y = jugador_rect.centery - camara_y
                altura_total = (ALTURA_SOL + alcada_jugador) - camara_y
                if distancia_y > 0:
                    anchura_actual = (distancia_y / altura_total) * amplada_cono_base
                    limite_izq = camara_x - (anchura_actual / 2)
                    limite_der = camara_x + (anchura_actual / 2)
                    if jugador_rect.right > limite_izq and jugador_rect.left < limite_der:
                        detectat = True

            if en_vermell and detectat:
                game_over = True

        PANTALLA.blit(fons_tutorial, (0, 0))
        PANTALLA.blit(camara_img, camara_rect)
        superficie_cono.fill((0, 0, 0, 0))

        text_camara = pygame.Rect(700, 100, 0, 0)
        if len(text_mostrat_1) > 0:
            mostrar_text(text_mostrat_1, font_petita, NEGRE, text_camara.centerx, text_camara.centery)

        if en_vermell:
            color_cono = (255, 0, 0, 100) if game_over or detectat else (255, 0, 0, 70)
        else:
            color_cono = (0, 255, 0, 70)

        punts_cono = [
            (camara_x, camara_y - 5),
            (camara_x - amplada_cono_base/2, ALTURA_SOL + alcada_jugador),
            (camara_x + amplada_cono_base/2, ALTURA_SOL + alcada_jugador)
        ]
        pygame.draw.polygon(superficie_cono, color_cono, punts_cono)
        PANTALLA.blit(superficie_cono, (0, 0))

        if en_porta and not game_over:
            mostrar_text("E", font_petita, NEGRE, PORTA_SORTIDA.centerx, PORTA_SORTIDA.top - 20)
        if en_porta2 and not game_over:
            mostrar_text("E", font_petita, NEGRE, PORTA_SORTIDA2.centerx, PORTA_SORTIDA2.top - 20)

        imatges_jugador_actuals = jugador_img_dreta if mirant_dreta else jugador_img_esquerra
        caminant = tecles[K_a] or tecles[K_d]
        PANTALLA.blit(obtenir_frame_jugador(imatges_jugador_actuals, caminant, en_terra), jugador_rect)

        if game_over:
            mostrar_text("GAME  OVER", font_gran, VERMELL, AMPLADA // 2, ALCADA // 2 - 20)
            mostrar_text("Prem  ENTER  per  reiniciar", font_petita, BLANC, AMPLADA // 2, ALCADA // 2 + 40)

        actualitzar_pantalla_amb_transicio()


def nivell_tutorial5(reiniciar=False, pos_x_inici=50):
    global jugador_rect, mirant_dreta, vel_y, en_terra, textos_vistos, moment_pausa_inici, temps_pausa_acumulat

    if moment_pausa_inici is not None:
        temps_pausa_acumulat += pygame.time.get_ticks() - moment_pausa_inici
        moment_pausa_inici = None

    jugant = True
    game_over = False
    amplada_jugador, alcada_jugador = 40, 80

    jugador_img_dreta, jugador_img_esquerra = carregar_animacio_jugador(
        "Alex_quiet.png", "Alex_frame1.png", "Alex_frame2.png", "Alex_salt.png",
        amplada_jugador, alcada_jugador
    )
    jugador_estado_dreta, jugador_estado_esquerra = carregar_animacio_jugador(
        "Alex_estado_quiet.png", "Alex_estado_frame1.png", "Alex_estado_frame2.png", "Alex_estado_salt.png",
        amplada_jugador, alcada_jugador
    )

    amplada_mur = img_mur.get_width()
    alcada_mur = img_mur.get_height()
    boto_rect = boto_img.get_rect(topleft=(25, 50))

    if reiniciar or jugador_rect is None:
        jugador_rect = jugador_img_dreta["quiet"].get_rect(topleft=(pos_x_inici, 444))
        if pos_x_inici > 400:
            mirant_dreta = False
        else:
            mirant_dreta = True
        vel_y = 0
        en_terra = True

    rect_agente = agente_img_base.get_rect(topleft=(800, 390))
    rect_deteccio = deteccio_img_base.get_rect()

    agente_mirant_dreta = False
    ultim_canvi_agente = temps_joc()

    GRAVETAT = 0.8
    FORCA_SALT = -14
    ALTURA_SOL = 390
    LIMIT_SOSTRE = 0
    LIMIT_ESQUERRA = 20
    LIMIT_DRETA = 870
    PORTA_SORTIDA = pygame.Rect(840, 333, 50, 100)
    PORTA_SORTIDA2 = pygame.Rect(0, 333, 50, 100)

    murs = [
        pygame.Rect(150, 400, amplada_mur, alcada_mur),
        pygame.Rect(75, 300, amplada_mur, alcada_mur),
        pygame.Rect(150, 200, amplada_mur, alcada_mur),
        pygame.Rect(75, 100, amplada_mur, alcada_mur),
    ]

    missatge_1 = "PERÒ  TENS  GADGETS"
    missatge_2 = "I  UN  PODER  QUE  T'AJUDEN,  BONA  SORT!"

    if textos_vistos["tutorial5"]:
        text_mostrat_1 = missatge_1
        index_1 = len(missatge_1)
        text_mostrat_2 = missatge_2
        index_2 = len(missatge_2)
    else:
        text_mostrat_1 = ""
        index_1 = 0
        text_mostrat_2 = ""
        index_2 = 0

    velocitat_text = 40
    ultim_temps_text = pygame.time.get_ticks()

    camara_x = 600
    camara_y = 50
    camara_rect = camara_img.get_rect(center=(camara_x, camara_y))
    amplada_cono_base = 250
    superficie_cono = pygame.Surface((AMPLADA, ALCADA), pygame.SRCALPHA)

    en_estado_robo = False
    cono_camara_activat = True
    laser_activat = False
    agente_inconsciente = False
    temps_inconsciente_inici = 0

    while jugant:
        clock.tick(60)
        en_porta = jugador_rect.colliderect(PORTA_SORTIDA)
        en_porta2 = jugador_rect.colliderect(PORTA_SORTIDA2)
        en_boto = jugador_rect.colliderect(boto_rect)
        temps_actual = temps_joc()

        for event in pygame.event.get():
            if event.type == QUIT:
                iniciar_transicio()
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if game_over:
                    if event.key in (K_RETURN, K_KP_ENTER):
                        iniciar_transicio()
                        return "REINICIAR"
                if event.key == K_ESCAPE:
                    moment_pausa_inici = pygame.time.get_ticks()
                    return "PAUSAT5"
                if event.key == K_e and en_porta:
                    iniciar_transicio()
                    return "JUGANT_TUTORIAL_FINAL"
                if event.key == K_e and en_porta2:
                    iniciar_transicio()
                    return "JUGANT_TUTORIAL4"
                if event.key == K_f and not laser_activat:
                    en_estado_robo = not en_estado_robo
                if event.key == K_q and not en_estado_robo:
                    laser_activat = not laser_activat
                if event.key == K_e and en_boto and en_estado_robo:
                    cono_camara_activat = not cono_camara_activat

        en_vermell = temps_actual

        if not game_over:
            temps_actual = temps_joc()
            if agente_inconsciente:
                if temps_actual - temps_inconsciente_inici >= 2000:
                    agente_inconsciente = False

            if temps_actual - ultim_canvi_agente >= 7000:
                agente_mirant_dreta = not agente_mirant_dreta
                ultim_canvi_agente = temps_actual

            altura_ojos = rect_agente.top + int(rect_agente.height * 0.22)
            if agente_mirant_dreta:
                rect_deteccio.left = rect_agente.right - 5
                rect_deteccio.centery = altura_ojos
            else:
                rect_deteccio.right = rect_agente.left + 5
                rect_deteccio.centery = altura_ojos

            dx = 0
            tecles = pygame.key.get_pressed()
            if tecles[K_a]:
                dx = -5
                mirant_dreta = False
            elif tecles[K_d]:
                dx = 5
                mirant_dreta = True

            jugador_rect.x += dx
            if jugador_rect.x <= LIMIT_ESQUERRA:
                jugador_rect.x = LIMIT_ESQUERRA
            if jugador_rect.right >= LIMIT_DRETA:
                jugador_rect.right = LIMIT_DRETA

            for mur in murs:
                if jugador_rect.colliderect(mur):
                    if dx > 0:
                        jugador_rect.right = mur.left
                    elif dx < 0:
                        jugador_rect.left = mur.right

            if tecles[K_w] and en_terra:
                vel_y = FORCA_SALT
                en_terra = False
            if jugador_rect.top <= LIMIT_SOSTRE:
                jugador_rect.top = LIMIT_SOSTRE
                vel_y = 0

            vel_y += GRAVETAT
            jugador_rect.y += vel_y
            en_terra = False

            if jugador_rect.y >= ALTURA_SOL:
                jugador_rect.y = ALTURA_SOL
                vel_y = 0
                en_terra = True

            for mur in murs:
                if jugador_rect.colliderect(mur):
                    if vel_y > 0:
                        jugador_rect.bottom = mur.top
                        vel_y = 0
                        en_terra = True
                    elif vel_y < 0:
                        jugador_rect.top = mur.bottom
                        vel_y = 0

            temps_actual = pygame.time.get_ticks()
            if temps_actual - ultim_temps_text > velocitat_text:
                if index_1 < len(missatge_1):
                    text_mostrat_1 += missatge_1[index_1]
                    index_1 += 1
                    ultim_temps_text = temps_actual
                elif index_2 < len(missatge_2):
                    text_mostrat_2 += missatge_2[index_2]
                    index_2 += 1
                    ultim_temps_text = temps_actual
                else:
                    textos_vistos["tutorial5"] = True

            detectat = False
            if cono_camara_activat:
                if jugador_rect.top < (ALTURA_SOL + alcada_jugador) and jugador_rect.bottom > camara_y:
                    distancia_y = jugador_rect.centery - camara_y
                    altura_total = (ALTURA_SOL + alcada_jugador) - camara_y
                    if distancia_y > 0:
                        anchura_actual = (distancia_y / altura_total) * amplada_cono_base
                        limite_izq = camara_x - (anchura_actual / 2)
                        limite_der = camara_x + (anchura_actual / 2)
                        if jugador_rect.right > limite_izq and jugador_rect.left < limite_der:
                            detectat = True

            if not agente_inconsciente:
                if jugador_rect.colliderect(rect_deteccio):
                    detectat = True
            if en_vermell and detectat:
                game_over = True

        PANTALLA.blit(fons_tutorial, (0, 0))
        for mur in murs:
            PANTALLA.blit(img_mur, (mur.x, mur.y))
        PANTALLA.blit(camara_img, camara_rect)
        PANTALLA.blit(boto_img, boto_rect)
        superficie_cono.fill((0, 0, 0, 0))

        text_tot = pygame.Rect(650, 100, 0, 0)
        text_tot2 = pygame.Rect(650, 125, 0, 0)
        if len(text_mostrat_1) > 0:
            mostrar_text(text_mostrat_1, font_petita, NEGRE, text_tot.centerx, text_tot.centery)
        if len(text_mostrat_2) > 0:
            mostrar_text(text_mostrat_2, font_petita, NEGRE, text_tot2.centerx, text_tot2.centery)

        if cono_camara_activat:
            if en_vermell:
                color_cono = (255, 0, 0, 100) if game_over or detectat else (255, 0, 0, 70)
            punts_cono = [
                (camara_x, camara_y - 5),
                (camara_x - amplada_cono_base/2, ALTURA_SOL + alcada_jugador),
                (camara_x + amplada_cono_base/2, ALTURA_SOL + alcada_jugador)
            ]
            pygame.draw.polygon(superficie_cono, color_cono, punts_cono)
            PANTALLA.blit(superficie_cono, (0, 0))

        if laser_activat:
            clau_frame_actual = obtenir_clau_frame_jugador(tecles[K_a] or tecles[K_d], en_terra)
            punt_ma_laser = punt_origen_laser(jugador_rect, mirant_dreta, clau_frame_actual)
            pos_mousse = pygame.mouse.get_pos()
            pos_final_laser = pos_mousse
            min_dist_sq = (pos_mousse[0] - punt_ma_laser[0])**2 + (pos_mousse[1] - punt_ma_laser[1])**2

            rect_terra = pygame.Rect(0, ALTURA_SOL + alcada_jugador, 2000, 500)
            rect_sostre = pygame.Rect(0, -500, 2000, 500 + LIMIT_SOSTRE)
            rect_esquerra = pygame.Rect(-500, 0, 500 + LIMIT_ESQUERRA, 2000)
            rect_dreta = pygame.Rect(LIMIT_DRETA, 0, 500, 2000)
            obstacles_laser = murs + [rect_terra, rect_sostre, rect_esquerra, rect_dreta]

            for obs in obstacles_laser:
                interseccions = obs.clipline(punt_ma_laser, pos_mousse)
                if interseccions:
                    for pt in interseccions:
                        dist_sq = (pt[0] - punt_ma_laser[0])**2 + (pt[1] - punt_ma_laser[1])**2
                        if dist_sq < min_dist_sq:
                            min_dist_sq = dist_sq
                            pos_final_laser = pt
            pygame.draw.line(PANTALLA, (255, 0, 0), punt_ma_laser, pos_final_laser, 3)

            if not game_over:
                if rect_agente.collidepoint(pos_final_laser) or rect_agente.clipline(punt_ma_laser, pos_final_laser):
                    agente_inconsciente = True
                    temps_inconsciente_inici = temps_joc()

        if en_porta and not game_over:
            mostrar_text("E", font_petita, NEGRE, PORTA_SORTIDA.centerx, PORTA_SORTIDA.top - 20)
        if en_porta2 and not game_over:
            mostrar_text("E", font_petita, NEGRE, PORTA_SORTIDA2.centerx, PORTA_SORTIDA2.top - 20)
        if en_boto and not game_over:
            if en_estado_robo:
                mostrar_text("E", font_petita, NEGRE, boto_rect.centerx, boto_rect.top - 20)
            else:
                mostrar_text("Necesitaes cambi de mans", font_mes_petita, VERMELL, boto_rect.centerx + 50, boto_rect.top - 40)

        if agente_mirant_dreta:
            PANTALLA.blit(agente_img_dreta, rect_agente)
            if not agente_inconsciente:
                PANTALLA.blit(deteccio_img_dreta, rect_deteccio)
        else:
            PANTALLA.blit(agente_img_esquerra, rect_agente)
            if not agente_inconsciente:
                PANTALLA.blit(deteccio_img_esquerra, rect_deteccio)

        if agente_inconsciente:
            temps_passat = temps_joc() - temps_inconsciente_inici
            temps_restant = 2 - (temps_passat // 1000)
            if temps_restant > 0:
                mostrar_text(str(temps_restant), font_petita, VERMELL, rect_agente.centerx, rect_agente.top - 20)

        if en_estado_robo:
            imatges_jugador_actuals = jugador_estado_dreta if mirant_dreta else jugador_estado_esquerra
        else:
            imatges_jugador_actuals = jugador_img_dreta if mirant_dreta else jugador_img_esquerra

        caminant = tecles[K_a] or tecles[K_d]
        PANTALLA.blit(obtenir_frame_jugador(imatges_jugador_actuals, caminant, en_terra), jugador_rect)

        if game_over:
            mostrar_text("GAME  OVER", font_gran, VERMELL, AMPLADA // 2, ALCADA // 2 - 20)
            mostrar_text("Prem  ENTER  per  reiniciar", font_petita, BLANC, AMPLADA // 2, ALCADA // 2 + 40)

        actualitzar_pantalla_amb_transicio()

def nivell1_pantalla1(reiniciar=False, pos_x_inici=50):
    global jugador_rect, mirant_dreta, vel_y, en_terra, textos_vistos, tresors_recollits, moment_pausa_inici, temps_pausa_acumulat

    if moment_pausa_inici is not None:
        temps_pausa_acumulat += pygame.time.get_ticks() - moment_pausa_inici
        moment_pausa_inici = None

    jugant = True
    game_over = False
    canviar_musica("niv1.mp3")

    amplada_jugador, alcada_jugador = 40, 80
    jugador_img_dreta, jugador_img_esquerra = carregar_animacio_jugador(
        "Alex_quiet.png", "Alex_frame1.png", "Alex_frame2.png", "Alex_salt.png",
        amplada_jugador, alcada_jugador
    )
    jugador_estado_dreta, jugador_estado_esquerra = carregar_animacio_jugador(
        "Alex_estado_quiet.png", "Alex_estado_frame1.png", "Alex_estado_frame2.png", "Alex_estado_salt.png",
        amplada_jugador, alcada_jugador
    )

    amplada_mur = img_estant.get_width()
    alcada_mur = img_estant.get_height()

    rect_tresor = nivell1_quadre.get_rect(topleft=(435, 260))

    if reiniciar or jugador_rect is None:
        jugador_rect = jugador_img_dreta["quiet"].get_rect(topleft=(pos_x_inici, 444))
        if pos_x_inici > 400:
            mirant_dreta = False
        else:
            mirant_dreta = True
        vel_y = 0
        en_terra = True

    GRAVETAT = 0.8
    FORCA_SALT = -14
    ALTURA_SOL = 390
    LIMIT_SOSTRE = 0
    LIMIT_ESQUERRA = 20
    LIMIT_DRETA = 870

    PORTA_SORTIDA = pygame.Rect(840, 333, 50, 100)

    murs = [
        pygame.Rect(150, 400, amplada_mur, alcada_mur),
        pygame.Rect(225, 325, amplada_mur, alcada_mur),
        pygame.Rect(300, 250, amplada_mur, alcada_mur),
        pygame.Rect(410, 325, amplada_mur, alcada_mur),
        pygame.Rect(520, 250, amplada_mur, alcada_mur),
        pygame.Rect(595, 325, amplada_mur, alcada_mur),
        pygame.Rect(670, 400, amplada_mur, alcada_mur),
    ]

    camara_x = 450
    camara_y = 50
    camara_rect = camara_img.get_rect(center=(camara_x, camara_y))
    amplada_cono_base = 250
    superficie_cono = pygame.Surface((AMPLADA, ALCADA), pygame.SRCALPHA)

    en_estado_robo = False
    cono_camara_activat = True
    laser_activat = False

    while jugant:
        clock.tick(60)
        en_porta = jugador_rect.colliderect(PORTA_SORTIDA)

        temps_actual = temps_joc()
        en_vermell = (temps_actual % 6000) >= 3000

        if not tresors_recollits["nivell1_quadre"]:
            if jugador_rect.colliderect(rect_tresor):
                tresors_recollits["nivell1_quadre"] = True
                if so_recollit:
                    so_recollit.set_volume(volum_sfx)
                    so_recollit.play()

        for event in pygame.event.get():
            if event.type == QUIT:
                iniciar_transicio()
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if game_over:
                    if event.key in (K_RETURN, K_KP_ENTER):
                        iniciar_transicio()
                        tresors_recollits["nivell1_quadre"] = False
                        return "REINICIAR"
                if event.key == K_ESCAPE:
                    moment_pausa_inici = pygame.time.get_ticks()
                    return "PAUSAN1.1"
                if event.key == K_e and en_porta and tresors_recollits["nivell1_quadre"]:
                    iniciar_transicio()
                    return "JUGANT_NIVELL1_PANTALLA2"
                if event.key == K_f and not laser_activat:
                    en_estado_robo = not en_estado_robo
                if event.key == K_q and not en_estado_robo:
                    laser_activat = not laser_activat

        if not game_over:
            temps_actual = temps_joc()

            dx = 0
            tecles = pygame.key.get_pressed()
            if tecles[K_a]:
                dx = -5
                mirant_dreta = False
            elif tecles[K_d]:
                dx = 5
                mirant_dreta = True

            jugador_rect.x += dx
            if jugador_rect.x <= LIMIT_ESQUERRA:
                jugador_rect.x = LIMIT_ESQUERRA
            if jugador_rect.right >= LIMIT_DRETA:
                jugador_rect.right = LIMIT_DRETA

            for mur in murs:
                if jugador_rect.colliderect(mur):
                    if dx > 0:
                        jugador_rect.right = mur.left
                    elif dx < 0:
                        jugador_rect.left = mur.right

            if tecles[K_w] and en_terra:
                vel_y = FORCA_SALT
                en_terra = False

            if jugador_rect.top <= LIMIT_SOSTRE:
                jugador_rect.top = LIMIT_SOSTRE
                vel_y = 0

            vel_y += GRAVETAT
            jugador_rect.y += vel_y
            en_terra = False

            if jugador_rect.y >= ALTURA_SOL:
                jugador_rect.y = ALTURA_SOL
                vel_y = 0
                en_terra = True

            for mur in murs:
                if jugador_rect.colliderect(mur):
                    if vel_y > 0:
                        jugador_rect.bottom = mur.top
                        vel_y = 0
                        en_terra = True
                    elif vel_y < 0:
                        jugador_rect.top = mur.bottom
                        vel_y = 0

            detectat = False
            if jugador_rect.top < (ALTURA_SOL + alcada_jugador) and jugador_rect.bottom > camara_y:
                distancia_y = jugador_rect.centery - camara_y
                altura_total = (ALTURA_SOL + alcada_jugador) - camara_y

                if distancia_y > 0:
                    anchura_actual = (distancia_y / altura_total) * amplada_cono_base
                    limite_izq = camara_x - (anchura_actual / 2)
                    limite_der = camara_x + (anchura_actual / 2)

                    if jugador_rect.right > limite_izq and jugador_rect.left < limite_der:
                        detectat = True

            if en_vermell and detectat:
                game_over = True

            if en_vermell:
                color_cono = (255, 0, 0, 100) if game_over or detectat else (255, 0, 0, 70)
            else:
                color_cono = (0, 255, 0, 70)

        PANTALLA.blit(fons_museu, (0, 0))

        for mur in murs:
            PANTALLA.blit(img_estant, (mur.x, mur.y))

        PANTALLA.blit(camara_img, camara_rect)

        if not tresors_recollits["nivell1_quadre"]:
            PANTALLA.blit(nivell1_quadre, rect_tresor)

        superficie_cono.fill((0, 0, 0, 0))

        if cono_camara_activat:
            if en_vermell:
                color_cono = (255, 0, 0, 100) if game_over or detectat else (255, 0, 0, 70)
            punts_cono = [
                (camara_x, camara_y - 5),
                (camara_x - amplada_cono_base/2, ALTURA_SOL + alcada_jugador),
                (camara_x + amplada_cono_base/2, ALTURA_SOL + alcada_jugador)
            ]
            pygame.draw.polygon(superficie_cono, color_cono, punts_cono)
            PANTALLA.blit(superficie_cono, (0, 0))

        if laser_activat:
            clau_frame_actual = obtenir_clau_frame_jugador(tecles[K_a] or tecles[K_d], en_terra)
            punt_ma_laser = punt_origen_laser(jugador_rect, mirant_dreta, clau_frame_actual)
            pos_mousse = pygame.mouse.get_pos()

            pos_final_laser = pos_mousse
            min_dist_sq = (pos_mousse[0] - punt_ma_laser[0])**2 + (pos_mousse[1] - punt_ma_laser[1])**2

            rect_terra = pygame.Rect(0, ALTURA_SOL + alcada_jugador, 2000, 500)
            rect_sostre = pygame.Rect(0, -500, 2000, 500 + LIMIT_SOSTRE)
            rect_esquerra = pygame.Rect(-500, 0, 500 + LIMIT_ESQUERRA, 2000)
            rect_dreta = pygame.Rect(LIMIT_DRETA, 0, 500, 2000)
            obstacles_laser = murs + [rect_terra, rect_sostre, rect_esquerra, rect_dreta]

            for obs in obstacles_laser:
                interseccions = obs.clipline(punt_ma_laser, pos_mousse)
                if interseccions:
                    for pt in interseccions:
                        dist_sq = (pt[0] - punt_ma_laser[0])**2 + (pt[1] - punt_ma_laser[1])**2
                        if dist_sq < min_dist_sq:
                            min_dist_sq = dist_sq
                            pos_final_laser = pt

            pygame.draw.line(PANTALLA, (255, 0, 0), punt_ma_laser, pos_final_laser, 3)

        if en_porta:
            if tresors_recollits["nivell1_quadre"]:
                mostrar_text("E", font_petita, NEGRE, PORTA_SORTIDA.centerx, PORTA_SORTIDA.top - 20)
            else:
                mostrar_text("Falta tresor", font_petita, VERMELL, PORTA_SORTIDA.centerx -100, PORTA_SORTIDA.top)

        if en_estado_robo:
            imatges_jugador_actuals = jugador_estado_dreta if mirant_dreta else jugador_estado_esquerra
        else:
            imatges_jugador_actuals = jugador_img_dreta if mirant_dreta else jugador_img_esquerra
        caminant = tecles[K_a] or tecles[K_d]
        PANTALLA.blit(obtenir_frame_jugador(imatges_jugador_actuals, caminant, en_terra), jugador_rect)

        if game_over:
            mostrar_text("GAME  OVER", font_gran, VERMELL, AMPLADA // 2, ALCADA // 2 - 20)
            mostrar_text("Prem  ENTER  per  reiniciar", font_petita, BLANC, AMPLADA // 2, ALCADA // 2 + 40)

        actualitzar_pantalla_amb_transicio()


def nivell1_pantalla2(reiniciar=False, pos_x_inici=50):
    global jugador_rect, mirant_dreta, vel_y, en_terra, textos_vistos, tresors_recollits, moment_pausa_inici, temps_pausa_acumulat

    if moment_pausa_inici is not None:
        temps_pausa_acumulat += pygame.time.get_ticks() - moment_pausa_inici
        moment_pausa_inici = None

    jugant = True
    game_over = False

    amplada_jugador, alcada_jugador = 40, 80
    jugador_img_dreta, jugador_img_esquerra = carregar_animacio_jugador(
        "Alex_quiet.png", "Alex_frame1.png", "Alex_frame2.png", "Alex_salt.png",
        amplada_jugador, alcada_jugador
    )
    jugador_estado_dreta, jugador_estado_esquerra = carregar_animacio_jugador(
        "Alex_estado_quiet.png", "Alex_estado_frame1.png", "Alex_estado_frame2.png", "Alex_estado_salt.png",
        amplada_jugador, alcada_jugador
    )

    amplada_mur = img_estant.get_width()
    alcada_mur = img_estant.get_height()

    rect_tresor = nivell1_quadre2.get_rect(topleft=(235, 100))
    boto_rect = boto_img.get_rect(topleft=(700, 390))

    rect_agente = agente_img_base.get_rect(topleft=(650, 390))
    rect_deteccio = deteccio_img_base.get_rect()
    agente_mirant_dreta = False
    ultim_canvi_agente = temps_joc()
    agente_inconsciente = False
    temps_inconsciente_inici = 0

    if reiniciar or jugador_rect is None:
        jugador_rect = jugador_img_dreta["quiet"].get_rect(topleft=(pos_x_inici, 444))
        if pos_x_inici > 400:
            mirant_dreta = False
        else:
            mirant_dreta = True
        vel_y = 0
        en_terra = True

    GRAVETAT = 0.8
    FORCA_SALT = -14
    ALTURA_SOL = 390
    LIMIT_SOSTRE = 0
    LIMIT_ESQUERRA = 20
    LIMIT_DRETA = 870
    PORTA_SORTIDA = pygame.Rect(840, 333, 50, 100)
    PORTA_SORTIDA2 = pygame.Rect(0, 333, 50, 100)

    murs = [
        pygame.Rect(220, 165, amplada_mur, alcada_mur),
        pygame.Rect(170, 265, amplada_mur, alcada_mur),
        pygame.Rect(220, 365, amplada_mur, alcada_mur),
    ]

    camara_x = 250
    camara_y = 50
    camara_rect = camara_img.get_rect(center=(camara_x, camara_y))
    amplada_cono_base = 250
    superficie_cono = pygame.Surface((AMPLADA, ALCADA), pygame.SRCALPHA)

    en_estado_robo = False
    cono_camara_activat = True
    laser_activat = False

    while jugant:
        clock.tick(60)
        en_porta = jugador_rect.colliderect(PORTA_SORTIDA)
        en_porta2 = jugador_rect.colliderect(PORTA_SORTIDA2)
        en_boto = jugador_rect.colliderect(boto_rect)

        temps_actual = temps_joc()
        en_vermell = (temps_actual % 6000) >= 1500

        if not tresors_recollits["nivell1_quadre2"]:
            if jugador_rect.colliderect(rect_tresor):
                tresors_recollits["nivell1_quadre2"] = True
                if so_recollit:
                    so_recollit.set_volume(volum_sfx)
                    so_recollit.play()

        for event in pygame.event.get():
            if event.type == QUIT:
                iniciar_transicio()
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if game_over:
                    if event.key in (K_RETURN, K_KP_ENTER):
                        iniciar_transicio()
                        tresors_recollits["nivell1_quadre2"] = False
                        return "REINICIAR"
                if event.key == K_ESCAPE:
                    moment_pausa_inici = pygame.time.get_ticks()
                    return "PAUSAN1.2"
                if event.key == K_e and en_porta and tresors_recollits["nivell1_quadre2"]:
                    iniciar_transicio()
                    return "JUGANT_NIVELL1_PANTALLA3"
                if event.key == K_e and en_porta2:
                    iniciar_transicio()
                    return "JUGANT_NIVELL1_PANTALLA1"
                if event.key == K_f and not laser_activat:
                    en_estado_robo = not en_estado_robo
                if event.key == K_q and not en_estado_robo:
                    laser_activat = not laser_activat

                if event.key == K_e and en_boto and en_estado_robo:
                    cono_camara_activat = not cono_camara_activat

        if not game_over:
            temps_actual = temps_joc()

            if agente_inconsciente:
                if temps_actual - temps_inconsciente_inici >= 2000:
                    agente_inconsciente = False

            if temps_actual - ultim_canvi_agente >= 7000:
                agente_mirant_dreta = not agente_mirant_dreta
                ultim_canvi_agente = temps_actual

            altura_ojos = rect_agente.top + int(rect_agente.height * 0.22)
            if agente_mirant_dreta:
                rect_deteccio.left = rect_agente.right - 5
                rect_deteccio.centery = altura_ojos
            else:
                rect_deteccio.right = rect_agente.left + 5
                rect_deteccio.centery = altura_ojos

            dx = 0
            tecles = pygame.key.get_pressed()
            if tecles[K_a]:
                dx = -5
                mirant_dreta = False
            elif tecles[K_d]:
                dx = 5
                mirant_dreta = True
            jugador_rect.x += dx

            if jugador_rect.x <= LIMIT_ESQUERRA:
                jugador_rect.x = LIMIT_ESQUERRA
            if jugador_rect.right >= LIMIT_DRETA:
                jugador_rect.right = LIMIT_DRETA

            for mur in murs:
                if jugador_rect.colliderect(mur):
                    if dx > 0:
                        jugador_rect.right = mur.left
                    elif dx < 0:
                        jugador_rect.left = mur.right

            if tecles[K_w] and en_terra:
                vel_y = FORCA_SALT
                en_terra = False

            if jugador_rect.top <= LIMIT_SOSTRE:
                jugador_rect.top = LIMIT_SOSTRE
                vel_y = 0

            vel_y += GRAVETAT
            jugador_rect.y += vel_y
            en_terra = False

            if jugador_rect.y >= ALTURA_SOL:
                jugador_rect.y = ALTURA_SOL
                vel_y = 0
                en_terra = True

            for mur in murs:
                if jugador_rect.colliderect(mur):
                    if vel_y > 0:
                        jugador_rect.bottom = mur.top
                        vel_y = 0
                        en_terra = True
                    elif vel_y < 0:
                        jugador_rect.top = mur.bottom
                        vel_y = 0

            detectat_cam = False
            detectat_agente = False

            if cono_camara_activat:
                if jugador_rect.top < (ALTURA_SOL + alcada_jugador) and jugador_rect.bottom > camara_y:
                    distancia_y = jugador_rect.centery - camara_y
                    altura_total = (ALTURA_SOL + alcada_jugador) - camara_y
                    if distancia_y > 0:
                        anchura_actual = (distancia_y / altura_total) * amplada_cono_base
                        limite_izq = camara_x - (anchura_actual / 2)
                        limite_der = camara_x + (anchura_actual / 2)
                        if jugador_rect.right > limite_izq and jugador_rect.left < limite_der:
                            detectat_cam = True

            if not agente_inconsciente:
                if jugador_rect.colliderect(rect_deteccio):
                    detectat_agente = True

            if (en_vermell and detectat_cam) or detectat_agente:
                game_over = True

        PANTALLA.blit(fons_museu, (0, 0))
        for mur in murs:
            PANTALLA.blit(img_estant, (mur.x, mur.y))

        PANTALLA.blit(camara_img, camara_rect)
        PANTALLA.blit(boto_img, boto_rect)

        if not tresors_recollits["nivell1_quadre2"]:
            PANTALLA.blit(nivell1_quadre2, rect_tresor)

        superficie_cono.fill((0, 0, 0, 0))

        if cono_camara_activat:
            if en_vermell:
                color_cono = (255, 0, 0, 100) if game_over or detectat_cam else (255, 0, 0, 70)
            else:
                color_cono = (0, 255, 0, 70)

            punts_cono = [
                (camara_x, camara_y - 5),
                (camara_x - amplada_cono_base/2, ALTURA_SOL + alcada_jugador),
                (camara_x + amplada_cono_base/2, ALTURA_SOL + alcada_jugador)
            ]
            pygame.draw.polygon(superficie_cono, color_cono, punts_cono)
            PANTALLA.blit(superficie_cono, (0, 0))

        if laser_activat:
            clau_frame_actual = obtenir_clau_frame_jugador(tecles[K_a] or tecles[K_d], en_terra)
            punt_ma_laser = punt_origen_laser(jugador_rect, mirant_dreta, clau_frame_actual)
            pos_mousse = pygame.mouse.get_pos()
            pos_final_laser = pos_mousse
            min_dist_sq = (pos_mousse[0] - punt_ma_laser[0])**2 + (pos_mousse[1] - punt_ma_laser[1])**2

            rect_terra = pygame.Rect(0, ALTURA_SOL + alcada_jugador, 2000, 500)
            rect_sostre = pygame.Rect(0, -500, 2000, 500 + LIMIT_SOSTRE)
            rect_esquerra = pygame.Rect(-500, 0, 500 + LIMIT_ESQUERRA, 2000)
            rect_dreta = pygame.Rect(LIMIT_DRETA, 0, 500, 2000)

            obstacles_laser = murs + [rect_terra, rect_sostre, rect_esquerra, rect_dreta]

            for obs in obstacles_laser:
                interseccions = obs.clipline(punt_ma_laser, pos_mousse)
                if interseccions:
                    for pt in interseccions:
                        dist_sq = (pt[0] - punt_ma_laser[0])**2 + (pt[1] - punt_ma_laser[1])**2
                        if dist_sq < min_dist_sq:
                            min_dist_sq = dist_sq
                            pos_final_laser = pt

            pygame.draw.line(PANTALLA, (255, 0, 0), punt_ma_laser, pos_final_laser, 3)

            if not game_over:
                if rect_agente.collidepoint(pos_final_laser) or rect_agente.clipline(punt_ma_laser, pos_final_laser):
                    agente_inconsciente = True
                    temps_inconsciente_inici = temps_joc()

        if en_boto and not game_over:
            if en_estado_robo:
                mostrar_text("E", font_petita, NEGRE, boto_rect.centerx, boto_rect.top - 20)
            else:
                mostrar_text("Necesitaes cambi de mans", font_mes_petita, VERMELL, boto_rect.centerx + 50, boto_rect.top - 40)

        if en_porta:
            if tresors_recollits["nivell1_quadre2"]:
                mostrar_text("E", font_petita, NEGRE, PORTA_SORTIDA.centerx, PORTA_SORTIDA.top - 20)
            else:
                mostrar_text("Falta tresor", font_petita, VERMELL, PORTA_SORTIDA.centerx -100, PORTA_SORTIDA.top)
        if en_porta2 and not game_over:
            mostrar_text("E", font_petita, NEGRE, PORTA_SORTIDA2.centerx, PORTA_SORTIDA2.top - 20)

        if agente_mirant_dreta:
            PANTALLA.blit(agente_img_dreta, rect_agente)
            if not agente_inconsciente:
                PANTALLA.blit(deteccio_img_dreta, rect_deteccio)
        else:
            PANTALLA.blit(agente_img_esquerra, rect_agente)
            if not agente_inconsciente:
                PANTALLA.blit(deteccio_img_esquerra, rect_deteccio)

        if agente_inconsciente:
            temps_passat = temps_joc() - temps_inconsciente_inici
            temps_restant = 2 - (temps_passat // 1000)
            if temps_restant > 0:
                mostrar_text(str(temps_restant), font_petita, VERMELL, rect_agente.centerx, rect_agente.top - 20)

        if en_estado_robo:
            imatges_jugador_actuals = jugador_estado_dreta if mirant_dreta else jugador_estado_esquerra
        else:
            imatges_jugador_actuals = jugador_img_dreta if mirant_dreta else jugador_img_esquerra
        caminant = tecles[K_a] or tecles[K_d]
        PANTALLA.blit(obtenir_frame_jugador(imatges_jugador_actuals, caminant, en_terra), jugador_rect)

        if game_over:
            mostrar_text("GAME  OVER", font_gran, VERMELL, AMPLADA // 2, ALCADA // 2 - 20)
            mostrar_text("Prem  ENTER  per  reiniciar", font_petita, BLANC, AMPLADA // 2, ALCADA // 2 + 40)

        actualitzar_pantalla_amb_transicio()

def nivell1_pantalla3(reiniciar=False, pos_x_inici=50):
    global jugador_rect, mirant_dreta, vel_y, en_terra, textos_vistos, tresors_recollits, moment_pausa_inici, temps_pausa_acumulat

    if moment_pausa_inici is not None:
        temps_pausa_acumulat += pygame.time.get_ticks() - moment_pausa_inici
        moment_pausa_inici = None

    jugant = True
    game_over = False

    amplada_jugador, alcada_jugador = 40, 80
    jugador_img_dreta, jugador_img_esquerra = carregar_animacio_jugador(
        "Alex_quiet.png", "Alex_frame1.png", "Alex_frame2.png", "Alex_salt.png",
        amplada_jugador, alcada_jugador
    )
    jugador_estado_dreta, jugador_estado_esquerra = carregar_animacio_jugador(
        "Alex_estado_quiet.png", "Alex_estado_frame1.png", "Alex_estado_frame2.png", "Alex_estado_salt.png",
        amplada_jugador, alcada_jugador
    )

    amplada_mur = img_estant.get_width()
    alcada_mur = img_estant.get_height()

    rect_tresor = nivell1_quadre3.get_rect(topleft=(430, 360))
    boto_rect = boto_img.get_rect(topleft=(140, 350))

    rect_agente = agente_img_base.get_rect(topleft=(330, 390))
    rect_deteccio = deteccio_img_base.get_rect()
    agente_mirant_dreta = False
    ultim_canvi_agente = temps_joc()
    agente_inconsciente = False
    temps_inconsciente_inici = 0

    rect_agente2 = agente_img_base.get_rect(topleft=(520, 390))
    rect_deteccio2 = deteccio_img_base.get_rect()
    agente2_mirant_dreta = False
    ultim_canvi_agente2 = temps_joc()
    agente2_inconsciente = False
    temps_inconsciente_inici2 = 0

    if reiniciar or jugador_rect is None:
        jugador_rect = jugador_img_dreta["quiet"].get_rect(topleft=(pos_x_inici, 444))
        if pos_x_inici > 400:
            mirant_dreta = False
        else:
            mirant_dreta = True
        vel_y = 0
        en_terra = True

    GRAVETAT = 0.8
    FORCA_SALT = -14
    ALTURA_SOL = 390
    LIMIT_SOSTRE = 0
    LIMIT_ESQUERRA = 20
    LIMIT_DRETA = 870
    PORTA_SORTIDA = pygame.Rect(840, 333, 50, 100)
    PORTA_SORTIDA2 = pygame.Rect(0, 333, 50, 100)

    murs = [
        pygame.Rect(120, 400, amplada_mur, alcada_mur),
    ]

    camara_x = AMPLADA // 2
    camara_y = 50
    camara_rect = camara_img.get_rect(center=(camara_x, camara_y))
    amplada_cono_base = 250
    superficie_cono = pygame.Surface((AMPLADA, ALCADA), pygame.SRCALPHA)

    en_estado_robo = False
    cono_camara_activat = True
    laser_activat = False

    while jugant:
        clock.tick(60)
        en_porta = jugador_rect.colliderect(PORTA_SORTIDA)
        en_porta2 = jugador_rect.colliderect(PORTA_SORTIDA2)
        en_boto = jugador_rect.colliderect(boto_rect)
        temps_actual = temps_joc()
        en_vermell = (temps_actual % 6000) >= 0

        if not tresors_recollits["nivell1_quadre3"]:
            if jugador_rect.colliderect(rect_tresor):
                tresors_recollits["nivell1_quadre3"] = True
                if so_recollit:
                    so_recollit.set_volume(volum_sfx)
                    so_recollit.play()

        for event in pygame.event.get():
            if event.type == QUIT:
                iniciar_transicio()
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if game_over:
                    if event.key in (K_RETURN, K_KP_ENTER):
                        iniciar_transicio()
                        tresors_recollits["nivell1_quadre3"] = False
                        return "REINICIAR"
                if event.key == K_ESCAPE:
                    moment_pausa_inici = pygame.time.get_ticks()
                    return "PAUSAN1.3"
                if event.key == K_e and en_porta and tresors_recollits["nivell1_quadre3"]:
                    iniciar_transicio()
                    return "JUGANT_NIVELL1_PANTALLA4"
                if event.key == K_e and en_porta2:
                    iniciar_transicio()
                    return "JUGANT_NIVELL1_PANTALLA2"
                if event.key == K_f and not laser_activat:
                    en_estado_robo = not en_estado_robo
                if event.key == K_q and not en_estado_robo:
                    laser_activat = not laser_activat
                if event.key == K_e and en_boto and en_estado_robo:
                    cono_camara_activat = not cono_camara_activat

        if not game_over:
            temps_actual = temps_joc()
            temps_actual2 = temps_joc()

            if agente_inconsciente:
                if temps_actual - temps_inconsciente_inici >= 2000:
                    agente_inconsciente = False
            if temps_actual - ultim_canvi_agente >= 7000:
                agente_mirant_dreta = not agente_mirant_dreta
                ultim_canvi_agente = temps_actual
            altura_ojos = rect_agente.top + int(rect_agente.height * 0.22)
            if agente_mirant_dreta:
                rect_deteccio.left = rect_agente.right - 5
                rect_deteccio.centery = altura_ojos
            else:
                rect_deteccio.right = rect_agente.left + 5
                rect_deteccio.centery = altura_ojos

            if agente2_inconsciente:
                if temps_actual2 - temps_inconsciente_inici2 >= 2000:
                    agente2_inconsciente = False
            if temps_actual2 - ultim_canvi_agente2 >= 7000:
                agente2_mirant_dreta = not agente2_mirant_dreta
                ultim_canvi_agente2 = temps_actual2
            altura_ojos2 = rect_agente2.top + int(rect_agente2.height * 0.22)
            if agente2_mirant_dreta:
                rect_deteccio2.left = rect_agente2.right - 5
                rect_deteccio2.centery = altura_ojos2
            else:
                rect_deteccio2.right = rect_agente2.left + 5
                rect_deteccio2.centery = altura_ojos2

            dx = 0
            tecles = pygame.key.get_pressed()
            if tecles[K_a]:
                dx = -5
                mirant_dreta = False
            elif tecles[K_d]:
                dx = 5
                mirant_dreta = True

            jugador_rect.x += dx
            if jugador_rect.x <= LIMIT_ESQUERRA:
                jugador_rect.x = LIMIT_ESQUERRA
            if jugador_rect.right >= LIMIT_DRETA:
                jugador_rect.right = LIMIT_DRETA

            for mur in murs:
                if jugador_rect.colliderect(mur):
                    if dx > 0:
                        jugador_rect.right = mur.left
                    elif dx < 0:
                        jugador_rect.left = mur.right

            if tecles[K_w] and en_terra:
                vel_y = FORCA_SALT
                en_terra = False
            if jugador_rect.top <= LIMIT_SOSTRE:
                jugador_rect.top = LIMIT_SOSTRE
                vel_y = 0

            vel_y += GRAVETAT
            jugador_rect.y += vel_y
            en_terra = False

            if jugador_rect.y >= ALTURA_SOL:
                jugador_rect.y = ALTURA_SOL
                vel_y = 0
                en_terra = True

            for mur in murs:
                if jugador_rect.colliderect(mur):
                    if vel_y > 0:
                        jugador_rect.bottom = mur.top
                        vel_y = 0
                        en_terra = True
                    elif vel_y < 0:
                        jugador_rect.top = mur.bottom
                        vel_y = 0

            detectat_cam = False
            detectat_agente = False
            detectat_agente2 = False

            if cono_camara_activat:
                if jugador_rect.top < (ALTURA_SOL + alcada_jugador) and jugador_rect.bottom > camara_y:
                    distancia_y = jugador_rect.centery - camara_y
                    altura_total = (ALTURA_SOL + alcada_jugador) - camara_y
                    if distancia_y > 0:
                        anchura_actual = (distancia_y / altura_total) * amplada_cono_base
                        limite_izq = camara_x - (anchura_actual / 2)
                        limite_der = camara_x + (anchura_actual / 2)
                        if jugador_rect.right > limite_izq and jugador_rect.left < limite_der:
                            detectat_cam = True

            if not agente_inconsciente:
                if jugador_rect.colliderect(rect_deteccio):
                    detectat_agente = True
            if not agente2_inconsciente:
                if jugador_rect.colliderect(rect_deteccio2):
                    detectat_agente2 = True

            if (en_vermell and detectat_cam) or detectat_agente or detectat_agente2:
                game_over = True

        PANTALLA.blit(fons_museu, (0, 0))

        for mur in murs:
            PANTALLA.blit(img_estant, (mur.x, mur.y))

        PANTALLA.blit(camara_img, camara_rect)
        PANTALLA.blit(boto_img, boto_rect)

        if not tresors_recollits["nivell1_quadre3"]:
            PANTALLA.blit(nivell1_quadre3, rect_tresor)

        superficie_cono.fill((0, 0, 0, 0))
        if cono_camara_activat:
            if en_vermell:
                color_cono = (255, 0, 0, 100) if game_over or detectat_cam else (255, 0, 0, 70)
            else:
                color_cono = (0, 255, 0, 70)
            punts_cono = [
                (camara_x, camara_y - 5),
                (camara_x - amplada_cono_base/2, ALTURA_SOL + alcada_jugador),
                (camara_x + amplada_cono_base/2, ALTURA_SOL + alcada_jugador)
            ]
            pygame.draw.polygon(superficie_cono, color_cono, punts_cono)
            PANTALLA.blit(superficie_cono, (0, 0))

        if laser_activat:
            clau_frame_actual = obtenir_clau_frame_jugador(tecles[K_a] or tecles[K_d], en_terra)
            punt_ma_laser = punt_origen_laser(jugador_rect, mirant_dreta, clau_frame_actual)
            pos_mousse = pygame.mouse.get_pos()
            pos_final_laser = pos_mousse
            min_dist_sq = (pos_mousse[0] - punt_ma_laser[0])**2 + (pos_mousse[1] - punt_ma_laser[1])**2

            rect_terra = pygame.Rect(0, ALTURA_SOL + alcada_jugador, 2000, 500)
            rect_sostre = pygame.Rect(0, -500, 2000, 500 + LIMIT_SOSTRE)
            rect_esquerra = pygame.Rect(-500, 0, 500 + LIMIT_ESQUERRA, 2000)
            rect_dreta = pygame.Rect(LIMIT_DRETA, 0, 500, 2000)
            obstacles_laser = murs + [rect_terra, rect_sostre, rect_esquerra, rect_dreta]

            for obs in obstacles_laser:
                interseccions = obs.clipline(punt_ma_laser, pos_mousse)
                if interseccions:
                    for pt in interseccions:
                        dist_sq = (pt[0] - punt_ma_laser[0])**2 + (pt[1] - punt_ma_laser[1])**2
                        if dist_sq < min_dist_sq:
                            min_dist_sq = dist_sq
                            pos_final_laser = pt

            pygame.draw.line(PANTALLA, (255, 0, 0), punt_ma_laser, pos_final_laser, 3)

            if not game_over:
                if rect_agente.collidepoint(pos_final_laser) or rect_agente.clipline(punt_ma_laser, pos_final_laser):
                    agente_inconsciente = True
                    temps_inconsciente_inici = temps_joc()
                if rect_agente2.collidepoint(pos_final_laser) or rect_agente2.clipline(punt_ma_laser, pos_final_laser):
                    agente2_inconsciente = True
                    temps_inconsciente_inici2 = temps_joc()

        if en_boto and not game_over:
            if en_estado_robo:
                mostrar_text("E", font_petita, NEGRE, boto_rect.centerx, boto_rect.top - 20)
            else:
                mostrar_text("Necesitaes cambi de mans", font_mes_petita, VERMELL, boto_rect.centerx + 50, boto_rect.top - 40)

        if en_porta:
            if tresors_recollits["nivell1_quadre3"]:
                mostrar_text("E", font_petita, NEGRE, PORTA_SORTIDA.centerx, PORTA_SORTIDA.top - 20)
            else:
                mostrar_text("Falta tresor", font_petita, VERMELL, PORTA_SORTIDA.centerx -100, PORTA_SORTIDA.top)

        if en_porta2 and not game_over:
            mostrar_text("E", font_petita, NEGRE, PORTA_SORTIDA2.centerx, PORTA_SORTIDA2.top - 20)

        if agente_mirant_dreta:
            PANTALLA.blit(agente_img_dreta, rect_agente)
            if not agente_inconsciente:
                PANTALLA.blit(deteccio_img_dreta, rect_deteccio)
        else:
            PANTALLA.blit(agente_img_esquerra, rect_agente)
            if not agente_inconsciente:
                PANTALLA.blit(deteccio_img_esquerra, rect_deteccio)

        if agente_inconsciente:
            temps_passat = temps_joc() - temps_inconsciente_inici
            temps_restant = 2 - (temps_passat // 1000)
            if temps_restant > 0:
                mostrar_text(str(temps_restant), font_petita, VERMELL, rect_agente.centerx, rect_agente.top - 20)

        if agente2_mirant_dreta:
            PANTALLA.blit(agente_img_dreta, rect_agente2)
            if not agente2_inconsciente:
                PANTALLA.blit(deteccio_img_dreta, rect_deteccio2)
        else:
            PANTALLA.blit(agente_img_esquerra, rect_agente2)
            if not agente2_inconsciente:
                PANTALLA.blit(deteccio_img_esquerra, rect_deteccio2)

        if agente2_inconsciente:
            temps_passat2 = temps_joc() - temps_inconsciente_inici2
            temps_restant2 = 2 - (temps_passat2 // 1000)
            if temps_restant2 > 0:
                mostrar_text(str(temps_restant2), font_petita, VERMELL, rect_agente2.centerx, rect_agente2.top - 20)

        if en_estado_robo:
            imatges_jugador_actuals = jugador_estado_dreta if mirant_dreta else jugador_estado_esquerra
        else:
            imatges_jugador_actuals = jugador_img_dreta if mirant_dreta else jugador_img_esquerra

        caminant = tecles[K_a] or tecles[K_d]
        PANTALLA.blit(obtenir_frame_jugador(imatges_jugador_actuals, caminant, en_terra), jugador_rect)

        if game_over:
            mostrar_text("GAME  OVER", font_gran, VERMELL, AMPLADA // 2, ALCADA // 2 - 20)
            mostrar_text("Prem  ENTER  per  reiniciar", font_petita, BLANC, AMPLADA // 2, ALCADA // 2 + 40)

        actualitzar_pantalla_amb_transicio()


def nivell1_pantalla4(reiniciar=False, pos_x_inici=50):
    global jugador_rect, mirant_dreta, vel_y, en_terra, textos_vistos, tresors_recollits, moment_pausa_inici, temps_pausa_acumulat

    if moment_pausa_inici is not None:
        temps_pausa_acumulat += pygame.time.get_ticks() - moment_pausa_inici
        moment_pausa_inici = None

    jugant = True
    game_over = False

    amplada_jugador, alcada_jugador = 40, 80
    jugador_img_dreta, jugador_img_esquerra = carregar_animacio_jugador(
        "Alex_quiet.png", "Alex_frame1.png", "Alex_frame2.png", "Alex_salt.png",
        amplada_jugador, alcada_jugador
    )
    jugador_estado_dreta, jugador_estado_esquerra = carregar_animacio_jugador(
        "Alex_estado_quiet.png", "Alex_estado_frame1.png", "Alex_estado_frame2.png", "Alex_estado_salt.png",
        amplada_jugador, alcada_jugador
    )

    amplada_mur = img_estant.get_width()
    alcada_mur = img_estant.get_height()

    rect_tresor = nivell1_quadre4.get_rect(topleft=(515, 100))

    if reiniciar or jugador_rect is None:
        jugador_rect = jugador_img_dreta["quiet"].get_rect(topleft=(pos_x_inici, 444))
        if pos_x_inici > 400:
            mirant_dreta = False
        else:
            mirant_dreta = True
        vel_y = 0
        en_terra = True

    GRAVETAT = 0.8
    FORCA_SALT = -14
    ALTURA_SOL = 390
    LIMIT_SOSTRE = 0
    LIMIT_ESQUERRA = 20
    LIMIT_DRETA = 870
    PORTA_SORTIDA = pygame.Rect(840, 333, 50, 100)
    PORTA_SORTIDA2 = pygame.Rect(0, 333, 50, 100)

    murs = [
        pygame.Rect(AMPLADA / 1.6666 - 45, 155, amplada_mur, alcada_mur),
        pygame.Rect(AMPLADA / 2.5 - 45, 225, amplada_mur, alcada_mur),
        pygame.Rect(AMPLADA / 1.6666 - 45, 295, amplada_mur, alcada_mur),
        pygame.Rect(AMPLADA / 2.5 - 45, 365, amplada_mur, alcada_mur),
    ]

    camara_x = AMPLADA / 2
    camara_y = 50
    camara_rect = camara_img.get_rect(center=(camara_x, camara_y))
    amplada_cono_base = 250
    superficie_cono = pygame.Surface((AMPLADA, ALCADA), pygame.SRCALPHA)

    en_estado_robo = False
    cono_camara_activat = True
    laser_activat = False

    while jugant:
        clock.tick(60)
        en_porta = jugador_rect.colliderect(PORTA_SORTIDA)
        en_porta2 = jugador_rect.colliderect(PORTA_SORTIDA2)
        temps_actual = temps_joc()
        en_vermell = (temps_actual % 6000) >= 1500

        if not tresors_recollits["nivell1_quadre4"]:
            if jugador_rect.colliderect(rect_tresor):
                tresors_recollits["nivell1_quadre4"] = True
                if so_recollit:
                    so_recollit.set_volume(volum_sfx)
                    so_recollit.play()

        for event in pygame.event.get():
            if event.type == QUIT:
                iniciar_transicio()
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if game_over:
                    if event.key in (K_RETURN, K_KP_ENTER):
                        iniciar_transicio()
                        tresors_recollits["nivell1_quadre4"] = False
                        return "REINICIAR"
                if event.key == K_ESCAPE:
                    moment_pausa_inici = pygame.time.get_ticks()
                    return "PAUSAN1.4"
                if event.key == K_e and en_porta and tresors_recollits["nivell1_quadre4"]:
                    iniciar_transicio()
                    nivells_completats["nivell1"] = True
                    return "JUGANT_NIVELL1_FINAL"
                if event.key == K_e and en_porta2:
                    iniciar_transicio()
                    return "JUGANT_NIVELL1_PANTALLA3"
                if event.key == K_f and not laser_activat:
                    en_estado_robo = not en_estado_robo
                if event.key == K_q and not en_estado_robo:
                    laser_activat = not laser_activat

        if not game_over:
            temps_actual = temps_joc()
            dx = 0
            tecles = pygame.key.get_pressed()
            if tecles[K_a]:
                dx = -5
                mirant_dreta = False
            elif tecles[K_d]:
                dx = 5
                mirant_dreta = True

            jugador_rect.x += dx
            if jugador_rect.x <= LIMIT_ESQUERRA:
                jugador_rect.x = LIMIT_ESQUERRA
            if jugador_rect.right >= LIMIT_DRETA:
                jugador_rect.right = LIMIT_DRETA

            for mur in murs:
                if jugador_rect.colliderect(mur):
                    if dx > 0:
                        jugador_rect.right = mur.left
                    elif dx < 0:
                        jugador_rect.left = mur.right

            if tecles[K_w] and en_terra:
                vel_y = FORCA_SALT
                en_terra = False

            if jugador_rect.top <= LIMIT_SOSTRE:
                jugador_rect.top = LIMIT_SOSTRE
                vel_y = 0

            vel_y += GRAVETAT
            jugador_rect.y += vel_y
            en_terra = False

            if jugador_rect.y >= ALTURA_SOL:
                jugador_rect.y = ALTURA_SOL
                vel_y = 0
                en_terra = True

            for mur in murs:
                if jugador_rect.colliderect(mur):
                    if vel_y > 0:
                        jugador_rect.bottom = mur.top
                        vel_y = 0
                        en_terra = True
                    elif vel_y < 0:
                        jugador_rect.top = mur.bottom
                        vel_y = 0

            detectat_cam = False
            if cono_camara_activat:
                if jugador_rect.top < (ALTURA_SOL + alcada_jugador) and jugador_rect.bottom > camara_y:
                    distancia_y = jugador_rect.centery - camara_y
                    altura_total = (ALTURA_SOL + alcada_jugador) - camara_y
                    if distancia_y > 0:
                        anchura_actual = (distancia_y / altura_total) * amplada_cono_base
                        limite_izq = camara_x - (anchura_actual / 4)
                        limite_der = camara_x + (anchura_actual / 4)
                        if jugador_rect.right > limite_izq and jugador_rect.left < limite_der:
                            detectat_cam = True

            if en_vermell and detectat_cam:
                game_over = True

        PANTALLA.blit(fons_museu, (0, 0))
        for mur in murs:
            PANTALLA.blit(img_estant, (mur.x, mur.y))

        PANTALLA.blit(camara_img, camara_rect)

        if not tresors_recollits["nivell1_quadre4"]:
            PANTALLA.blit(nivell1_quadre4, rect_tresor)

        superficie_cono.fill((0, 0, 0, 0))
        if cono_camara_activat:
            if en_vermell:
                color_cono = (255, 0, 0, 100) if game_over or detectat_cam else (255, 0, 0, 70)
            else:
                color_cono = (0, 255, 0, 70)
            punts_cono = [
                (camara_x, camara_y - 5),
                (camara_x - amplada_cono_base/4, ALTURA_SOL + alcada_jugador),
                (camara_x + amplada_cono_base/4, ALTURA_SOL + alcada_jugador)
            ]
            pygame.draw.polygon(superficie_cono, color_cono, punts_cono)
            PANTALLA.blit(superficie_cono, (0, 0))

        if laser_activat:
            clau_frame_actual = obtenir_clau_frame_jugador(tecles[K_a] or tecles[K_d], en_terra)
            punt_ma_laser = punt_origen_laser(jugador_rect, mirant_dreta, clau_frame_actual)
            pos_mousse = pygame.mouse.get_pos()
            pos_final_laser = pos_mousse
            min_dist_sq = (pos_mousse[0] - punt_ma_laser[0])**2 + (pos_mousse[1] - punt_ma_laser[1])**2

            rect_terra = pygame.Rect(0, ALTURA_SOL + alcada_jugador, 2000, 500)
            rect_sostre = pygame.Rect(0, -500, 2000, 500 + LIMIT_SOSTRE)
            rect_esquerra = pygame.Rect(-500, 0, 500 + LIMIT_ESQUERRA, 2000)
            rect_dreta = pygame.Rect(LIMIT_DRETA, 0, 500, 2000)
            obstacles_laser = murs + [rect_terra, rect_sostre, rect_esquerra, rect_dreta]

            for obs in obstacles_laser:
                interseccions = obs.clipline(punt_ma_laser, pos_mousse)
                if interseccions:
                    for pt in interseccions:
                        dist_sq = (pt[0] - punt_ma_laser[0])**2 + (pt[1] - punt_ma_laser[1])**2
                        if dist_sq < min_dist_sq:
                            min_dist_sq = dist_sq
                            pos_final_laser = pt

            pygame.draw.line(PANTALLA, (255, 0, 0), punt_ma_laser, pos_final_laser, 3)

        if en_porta:
            if tresors_recollits["nivell1_quadre4"]:
                mostrar_text("E", font_petita, NEGRE, PORTA_SORTIDA.centerx, PORTA_SORTIDA.top - 20)
            else:
                mostrar_text("Falta tresor", font_petita, VERMELL, PORTA_SORTIDA.centerx -100, PORTA_SORTIDA.top)

        if en_porta2 and not game_over:
            mostrar_text("E", font_petita, NEGRE, PORTA_SORTIDA2.centerx, PORTA_SORTIDA2.top - 20)

        if en_estado_robo:
            imatges_jugador_actuals = jugador_estado_dreta if mirant_dreta else jugador_estado_esquerra
        else:
            imatges_jugador_actuals = jugador_img_dreta if mirant_dreta else jugador_img_esquerra

        caminant = tecles[K_a] or tecles[K_d]
        PANTALLA.blit(obtenir_frame_jugador(imatges_jugador_actuals, caminant, en_terra), jugador_rect)

        if game_over:
            mostrar_text("GAME  OVER", font_gran, VERMELL, AMPLADA // 2, ALCADA // 2 - 20)
            mostrar_text("Prem  ENTER  per  reiniciar", font_petita, BLANC, AMPLADA // 2, ALCADA // 2 + 40)

        actualitzar_pantalla_amb_transicio()

def nivell2_pantalla1(reiniciar=False, pos_x_inici=50):
    global jugador_rect, mirant_dreta, vel_y, en_terra, textos_vistos, moment_pausa_inici, temps_pausa_acumulat

    if moment_pausa_inici is not None:
        temps_pausa_acumulat += pygame.time.get_ticks() - moment_pausa_inici
        moment_pausa_inici = None

    jugant = True
    game_over = False

    canviar_musica("niv2.mp3")

    amplada_jugador, alcada_jugador = 40, 80
    jugador_img_dreta, jugador_img_esquerra = carregar_animacio_jugador(
        "Alex_quiet.png", "Alex_frame1.png", "Alex_frame2.png", "Alex_salt.png",
        amplada_jugador, alcada_jugador
    )
    jugador_estado_dreta, jugador_estado_esquerra = carregar_animacio_jugador(
        "Alex_estado_quiet.png", "Alex_estado_frame1.png", "Alex_estado_frame2.png", "Alex_estado_salt.png",
        amplada_jugador, alcada_jugador
    )

    rect_agente = agente_img_base.get_rect(topleft=(350, 390))
    rect_deteccio = deteccio_img_base.get_rect()
    agente_mirant_dreta = False
    ultim_canvi_agente = temps_joc()
    agente_inconsciente = False
    temps_inconsciente_inici = 0

    rect_agente2 = agente_img_base.get_rect(topleft=(550, 390))
    rect_deteccio2 = deteccio_img_base.get_rect()
    agente2_mirant_dreta = False
    ultim_canvi_agente2 = temps_joc()
    agente2_inconsciente = False
    temps_inconsciente_inici2 = 0

    if reiniciar or jugador_rect is None:
        jugador_rect = jugador_img_dreta["quiet"].get_rect(topleft=(pos_x_inici, 444))
        if pos_x_inici > 400:
            mirant_dreta = False
        else:
            mirant_dreta = True
        vel_y = 0
        en_terra = True

    GRAVETAT = 0.8
    FORCA_SALT = -14
    ALTURA_SOL = 390
    LIMIT_SOSTRE = 0
    LIMIT_ESQUERRA = 20
    LIMIT_DRETA = 870
    PORTA_SORTIDA = pygame.Rect(840, 333, 50, 100)
    PORTA_SORTIDA2 = pygame.Rect(0, 333, 50, 100)

    camara_x = 644
    camara_y = 50
    camara_rect = camara_img.get_rect(center=(camara_x, camara_y))
    amplada_cono_base = 250
    superficie_cono = pygame.Surface((AMPLADA, ALCADA), pygame.SRCALPHA)

    en_estado_robo = False
    cono_camara_activat = True
    laser_activat = False

    while jugant:
        clock.tick(60)
        en_porta = jugador_rect.colliderect(PORTA_SORTIDA)
        en_porta2 = jugador_rect.colliderect(PORTA_SORTIDA2)
        temps_actual = temps_joc()
        en_vermell = (temps_actual % 6000) >= 1500

        for event in pygame.event.get():
            if event.type == QUIT:
                iniciar_transicio()
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if game_over:
                    if event.key in (K_RETURN, K_KP_ENTER):
                        iniciar_transicio()
                        return "REINICIAR"
                if event.key == K_ESCAPE:
                    moment_pausa_inici = pygame.time.get_ticks()
                    return "PAUSAN2.1"
                if event.key == K_e and en_porta:
                    iniciar_transicio()
                    return "JUGANT_NIVELL2_PANTALLA2"
                if event.key == K_f and not laser_activat:
                    en_estado_robo = not en_estado_robo
                if event.key == K_q and not en_estado_robo:
                    laser_activat = not laser_activat

        if not game_over:
            temps_actual = temps_joc()
            temps_actual2 = temps_joc()

            if agente_inconsciente:
                if temps_actual - temps_inconsciente_inici >= 2000:
                    agente_inconsciente = False
            if temps_actual - ultim_canvi_agente >= 7000:
                agente_mirant_dreta = not agente_mirant_dreta
                ultim_canvi_agente = temps_actual
            altura_ojos = rect_agente.top + int(rect_agente.height * 0.22)
            if agente_mirant_dreta:
                rect_deteccio.left = rect_agente.right - 5
                rect_deteccio.centery = altura_ojos
            else:
                rect_deteccio.right = rect_agente.left + 5
                rect_deteccio.centery = altura_ojos

            if agente2_inconsciente:
                if temps_actual2 - temps_inconsciente_inici2 >= 2000:
                    agente2_inconsciente = False
            if temps_actual2 - ultim_canvi_agente2 >= 7000:
                agente2_mirant_dreta = not agente2_mirant_dreta
                ultim_canvi_agente2 = temps_actual2
            altura_ojos2 = rect_agente2.top + int(rect_agente2.height * 0.22)
            if agente2_mirant_dreta:
                rect_deteccio2.left = rect_agente2.right - 5
                rect_deteccio2.centery = altura_ojos2
            else:
                rect_deteccio2.right = rect_agente2.left + 5
                rect_deteccio2.centery = altura_ojos2

            dx = 0
            tecles = pygame.key.get_pressed()
            if tecles[K_a]:
                dx = -5
                mirant_dreta = False
            elif tecles[K_d]:
                dx = 5
                mirant_dreta = True

            jugador_rect.x += dx
            if jugador_rect.x <= LIMIT_ESQUERRA:
                jugador_rect.x = LIMIT_ESQUERRA
            if jugador_rect.right >= LIMIT_DRETA:
                jugador_rect.right = LIMIT_DRETA

            if tecles[K_w] and en_terra:
                vel_y = FORCA_SALT
                en_terra = False
            if jugador_rect.top <= LIMIT_SOSTRE:
                jugador_rect.top = LIMIT_SOSTRE
                vel_y = 0

            vel_y += GRAVETAT
            jugador_rect.y += vel_y
            en_terra = False

            if jugador_rect.y >= ALTURA_SOL:
                jugador_rect.y = ALTURA_SOL
                vel_y = 0
                en_terra = True

            detectat_cam = False
            detectat_agente = False
            detectat_agente2 = False

            if cono_camara_activat:
                if jugador_rect.top < (ALTURA_SOL + alcada_jugador) and jugador_rect.bottom > camara_y:
                    distancia_y = jugador_rect.centery - camara_y
                    altura_total = (ALTURA_SOL + alcada_jugador) - camara_y
                    if distancia_y > 0:
                        anchura_actual = (distancia_y / altura_total) * amplada_cono_base
                        limite_izq = camara_x - (anchura_actual / 2)
                        limite_der = camara_x + (anchura_actual / 2)
                        if jugador_rect.right > limite_izq and jugador_rect.left < limite_der:
                            detectat_cam = True

            if not agente_inconsciente:
                if jugador_rect.colliderect(rect_deteccio):
                    detectat_agente = True
            if not agente2_inconsciente:
                if jugador_rect.colliderect(rect_deteccio2):
                    detectat_agente2 = True

            if (en_vermell and detectat_cam) or detectat_agente or detectat_agente2:
                game_over = True

        PANTALLA.blit(fons_banc, (0, 0))
        PANTALLA.blit(camara_img, camara_rect)
        superficie_cono.fill((0, 0, 0, 0))

        if cono_camara_activat:
            if en_vermell:
                color_cono = (255, 0, 0, 100) if game_over or detectat_cam else (255, 0, 0, 70)
            else:
                color_cono = (0, 255, 0, 70)
            punts_cono = [
                (camara_x, camara_y - 5),
                (camara_x - amplada_cono_base/2, ALTURA_SOL + alcada_jugador),
                (camara_x + amplada_cono_base/2, ALTURA_SOL + alcada_jugador)
            ]
            pygame.draw.polygon(superficie_cono, color_cono, punts_cono)
            PANTALLA.blit(superficie_cono, (0, 0))

        if laser_activat:
            clau_frame_actual = obtenir_clau_frame_jugador(tecles[K_a] or tecles[K_d], en_terra)
            punt_ma_laser = punt_origen_laser(jugador_rect, mirant_dreta, clau_frame_actual)
            pos_mousse = pygame.mouse.get_pos()
            pos_final_laser = pos_mousse
            min_dist_sq = (pos_mousse[0] - punt_ma_laser[0])**2 + (pos_mousse[1] - punt_ma_laser[1])**2

            rect_terra = pygame.Rect(0, ALTURA_SOL + alcada_jugador, 2000, 500)
            rect_sostre = pygame.Rect(0, -500, 2000, 500 + LIMIT_SOSTRE)
            rect_esquerra = pygame.Rect(-500, 0, 500 + LIMIT_ESQUERRA, 2000)
            rect_dreta = pygame.Rect(LIMIT_DRETA, 0, 500, 2000)
            obstacles_laser = [rect_terra, rect_sostre, rect_esquerra, rect_dreta]

            for obs in obstacles_laser:
                interseccions = obs.clipline(punt_ma_laser, pos_mousse)
                if interseccions:
                    for pt in interseccions:
                        dist_sq = (pt[0] - punt_ma_laser[0])**2 + (pt[1] - punt_ma_laser[1])**2
                        if dist_sq < min_dist_sq:
                            min_dist_sq = dist_sq
                            pos_final_laser = pt

            pygame.draw.line(PANTALLA, (255, 0, 0), punt_ma_laser, pos_final_laser, 3)

            if not game_over:
                if rect_agente.collidepoint(pos_final_laser) or rect_agente.clipline(punt_ma_laser, pos_final_laser):
                    agente_inconsciente = True
                    temps_inconsciente_inici = temps_joc()
                if rect_agente2.collidepoint(pos_final_laser) or rect_agente2.clipline(punt_ma_laser, pos_final_laser):
                    agente2_inconsciente = True
                    temps_inconsciente_inici2 = temps_joc()

        if en_porta:
            mostrar_text("E", font_petita, NEGRE, PORTA_SORTIDA.centerx, PORTA_SORTIDA.top - 20)
        if en_porta2 and not game_over:
            mostrar_text("E", font_petita, NEGRE, PORTA_SORTIDA2.centerx, PORTA_SORTIDA2.top - 20)

        if agente_mirant_dreta:
            PANTALLA.blit(agente_img_dreta, rect_agente)
            if not agente_inconsciente:
                PANTALLA.blit(deteccio_img_dreta, rect_deteccio)
        else:
            PANTALLA.blit(agente_img_esquerra, rect_agente)
            if not agente_inconsciente:
                PANTALLA.blit(deteccio_img_esquerra, rect_deteccio)

        if agente_inconsciente:
            temps_passat = temps_joc() - temps_inconsciente_inici
            temps_restant = 2 - (temps_passat // 1000)
            if temps_restant > 0:
                mostrar_text(str(temps_restant), font_petita, VERMELL, rect_agente.centerx, rect_agente.top - 20)

        if agente2_mirant_dreta:
            PANTALLA.blit(agente_img_dreta, rect_agente2)
            if not agente2_inconsciente:
                PANTALLA.blit(deteccio_img_dreta, rect_deteccio2)
        else:
            PANTALLA.blit(agente_img_esquerra, rect_agente2)
            if not agente2_inconsciente:
                PANTALLA.blit(deteccio_img_esquerra, rect_deteccio2)

        if agente2_inconsciente:
            temps_passat2 = temps_joc() - temps_inconsciente_inici2
            temps_restant2 = 2 - (temps_passat2 // 1000)
            if temps_restant2 > 0:
                mostrar_text(str(temps_restant2), font_petita, VERMELL, rect_agente2.centerx, rect_agente2.top - 20)

        if en_estado_robo:
            imatges_jugador_actuals = jugador_estado_dreta if mirant_dreta else jugador_estado_esquerra
        else:
            imatges_jugador_actuals = jugador_img_dreta if mirant_dreta else jugador_img_esquerra

        caminant = tecles[K_a] or tecles[K_d]
        PANTALLA.blit(obtenir_frame_jugador(imatges_jugador_actuals, caminant, en_terra), jugador_rect)

        if game_over:
            mostrar_text("GAME  OVER", font_gran, VERMELL, AMPLADA // 2, ALCADA // 2 - 20)
            mostrar_text("Prem  ENTER  per  reiniciar", font_petita, BLANC, AMPLADA // 2, ALCADA // 2 + 40)

        actualitzar_pantalla_amb_transicio()

def nivell2_pantalla2(reiniciar=False, pos_x_inici=50):
    global jugador_rect, mirant_dreta, vel_y, en_terra, textos_vistos, tresors_recollits, moment_pausa_inici, temps_pausa_acumulat

    if moment_pausa_inici is not None:
        temps_pausa_acumulat += pygame.time.get_ticks() - moment_pausa_inici
        moment_pausa_inici = None

    jugant = True
    game_over = False

    amplada_jugador, alcada_jugador = 40, 80
    jugador_img_dreta, jugador_img_esquerra = carregar_animacio_jugador(
        "Alex_quiet.png", "Alex_frame1.png", "Alex_frame2.png", "Alex_salt.png",
        amplada_jugador, alcada_jugador
    )
    jugador_estado_dreta, jugador_estado_esquerra = carregar_animacio_jugador(
        "Alex_estado_quiet.png", "Alex_estado_frame1.png", "Alex_estado_frame2.png", "Alex_estado_salt.png",
        amplada_jugador, alcada_jugador
    )

    amplada_mur = img_repisa.get_width()
    alcada_mur = img_repisa.get_height()

    rect_tresor = nivell2_clau.get_rect(topleft=(625, 180))
    rect_agente = agente_img_base.get_rect(topleft=(650, 390))
    rect_deteccio = deteccio_img_base.get_rect()

    agente_mirant_dreta = False
    ultim_canvi_agente = temps_joc()
    agente_inconsciente = False
    temps_inconsciente_inici = 0

    rect_agente2 = agente_img_base.get_rect(topleft=(470, 120))
    rect_deteccio2 = deteccio_img_base.get_rect()
    agente2_mirant_dreta = False
    ultim_canvi_agente2 = temps_joc()
    agente2_inconsciente = False
    temps_inconsciente_inici2 = 0

    if reiniciar or jugador_rect is None:
        jugador_rect = jugador_img_dreta["quiet"].get_rect(topleft=(pos_x_inici, 444))
        if pos_x_inici > 400:
            mirant_dreta = False
        else:
            mirant_dreta = True
        vel_y = 0
        en_terra = True

    GRAVETAT = 0.8
    FORCA_SALT = -14
    ALTURA_SOL = 390
    LIMIT_SOSTRE = 0
    LIMIT_ESQUERRA = 20
    LIMIT_DRETA = 870
    PORTA_SORTIDA = pygame.Rect(840, 333, 50, 100)
    PORTA_SORTIDA2 = pygame.Rect(0, 333, 50, 100)

    murs = [
        pygame.Rect(600, 200, amplada_mur, alcada_mur),
        pygame.Rect(450, 200, amplada_mur, alcada_mur),
        pygame.Rect(300, 300, amplada_mur, alcada_mur),
        pygame.Rect(150, 400, amplada_mur, alcada_mur),
    ]

    en_estado_robo = False
    laser_activat = False

    while jugant:
        clock.tick(60)
        en_porta = jugador_rect.colliderect(PORTA_SORTIDA)
        en_porta2 = jugador_rect.colliderect(PORTA_SORTIDA2)

        if not tresors_recollits["nivell2_clau"]:
            if jugador_rect.colliderect(rect_tresor):
                tresors_recollits["nivell2_clau"] = True
                if so_recollit:
                    so_recollit.set_volume(volum_sfx)
                    so_recollit.play()

        for event in pygame.event.get():
            if event.type == QUIT:
                iniciar_transicio()
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if game_over:
                    if event.key in (K_RETURN, K_KP_ENTER):
                        iniciar_transicio()
                        tresors_recollits["nivell2_clau"] = False
                        return "REINICIAR"
                if event.key == K_ESCAPE:
                    moment_pausa_inici = pygame.time.get_ticks()
                    return "PAUSAN2.2"
                if event.key == K_e and en_porta and tresors_recollits["nivell2_clau"]:
                    iniciar_transicio()
                    return "JUGANT_NIVELL2_PANTALLA3"
                if event.key == K_e and en_porta2:
                    iniciar_transicio()
                    return "JUGANT_NIVELL2_PANTALLA1"
                if event.key == K_f and not laser_activat:
                    en_estado_robo = not en_estado_robo
                if event.key == K_q and not en_estado_robo:
                    laser_activat = not laser_activat

        if not game_over:
            temps_actual = temps_joc()
            temps_actual2 = temps_joc()

            if agente_inconsciente:
                if temps_actual - temps_inconsciente_inici >= 2000:
                    agente_inconsciente = False
            if temps_actual - ultim_canvi_agente >= 7000:
                agente_mirant_dreta = not agente_mirant_dreta
                ultim_canvi_agente = temps_actual

            altura_ojos = rect_agente.top + int(rect_agente.height * 0.22)
            if agente_mirant_dreta:
                rect_deteccio.left = rect_agente.right - 5
                rect_deteccio.centery = altura_ojos
            else:
                rect_deteccio.right = rect_agente.left + 5
                rect_deteccio.centery = altura_ojos

            if agente2_inconsciente:
                if temps_actual2 - temps_inconsciente_inici2 >= 2000:
                    agente2_inconsciente = False
            if temps_actual2 - ultim_canvi_agente2 >= 7000:
                agente2_mirant_dreta = not agente2_mirant_dreta
                ultim_canvi_agente2 = temps_actual2

            altura_ojos2 = rect_agente2.top + int(rect_agente2.height * 0.22)
            if agente2_mirant_dreta:
                rect_deteccio2.left = rect_agente2.right - 5
                rect_deteccio2.centery = altura_ojos2
            else:
                rect_deteccio2.right = rect_agente2.left + 5
                rect_deteccio2.centery = altura_ojos2

            dx = 0
            tecles = pygame.key.get_pressed()
            if tecles[K_a]:
                dx = -5
                mirant_dreta = False
            elif tecles[K_d]:
                dx = 5
                mirant_dreta = True

            jugador_rect.x += dx
            if jugador_rect.x <= LIMIT_ESQUERRA:
                jugador_rect.x = LIMIT_ESQUERRA
            if jugador_rect.right >= LIMIT_DRETA:
                jugador_rect.right = LIMIT_DRETA

            for mur in murs:
                if jugador_rect.colliderect(mur):
                    if dx > 0:
                        jugador_rect.right = mur.left
                    elif dx < 0:
                        jugador_rect.left = mur.right

            if tecles[K_w] and en_terra:
                vel_y = FORCA_SALT
                en_terra = False
            if jugador_rect.top <= LIMIT_SOSTRE:
                jugador_rect.top = LIMIT_SOSTRE
                vel_y = 0

            vel_y += GRAVETAT
            jugador_rect.y += vel_y
            en_terra = False

            if jugador_rect.y >= ALTURA_SOL:
                jugador_rect.y = ALTURA_SOL
                vel_y = 0
                en_terra = True

            for mur in murs:
                if jugador_rect.colliderect(mur):
                    if vel_y > 0:
                        jugador_rect.bottom = mur.top
                        vel_y = 0
                        en_terra = True
                    elif vel_y < 0:
                        jugador_rect.top = mur.bottom
                        vel_y = 0

            detectat_agente = False
            detectat_agente2 = False

            if not agente_inconsciente:
                if jugador_rect.colliderect(rect_deteccio):
                    detectat_agente = True
            if not agente2_inconsciente:
                if jugador_rect.colliderect(rect_deteccio2):
                    detectat_agente2 = True
            if detectat_agente or detectat_agente2:
                game_over = True

        PANTALLA.blit(fons_banc2, (0, 0))
        for mur in murs:
            PANTALLA.blit(img_repisa, (mur.x, mur.y))

        if not tresors_recollits["nivell2_clau"]:
            PANTALLA.blit(nivell2_clau, rect_tresor)

        if laser_activat:
            clau_frame_actual = obtenir_clau_frame_jugador(tecles[K_a] or tecles[K_d], en_terra)
            punt_ma_laser = punt_origen_laser(jugador_rect, mirant_dreta, clau_frame_actual)
            pos_mousse = pygame.mouse.get_pos()
            pos_final_laser = pos_mousse
            min_dist_sq = (pos_mousse[0] - punt_ma_laser[0])**2 + (pos_mousse[1] - punt_ma_laser[1])**2

            rect_terra = pygame.Rect(0, ALTURA_SOL + alcada_jugador, 2000, 500)
            rect_sostre = pygame.Rect(0, -500, 2000, 500 + LIMIT_SOSTRE)
            rect_esquerra = pygame.Rect(-500, 0, 500 + LIMIT_ESQUERRA, 2000)
            rect_dreta = pygame.Rect(LIMIT_DRETA, 0, 500, 2000)
            obstacles_laser = murs + [rect_terra, rect_sostre, rect_esquerra, rect_dreta]

            for obs in obstacles_laser:
                interseccions = obs.clipline(punt_ma_laser, pos_mousse)
                if interseccions:
                    for pt in interseccions:
                        dist_sq = (pt[0] - punt_ma_laser[0])**2 + (pt[1] - punt_ma_laser[1])**2
                        if dist_sq < min_dist_sq:
                            min_dist_sq = dist_sq
                            pos_final_laser = pt
            pygame.draw.line(PANTALLA, (255, 0, 0), punt_ma_laser, pos_final_laser, 3)

            if not game_over:
                if rect_agente.collidepoint(pos_final_laser) or rect_agente.clipline(punt_ma_laser, pos_final_laser):
                    agente_inconsciente = True
                    temps_inconsciente_inici = temps_joc()
                if rect_agente2.collidepoint(pos_final_laser) or rect_agente2.clipline(punt_ma_laser, pos_final_laser):
                    agente2_inconsciente = True
                    temps_inconsciente_inici2 = temps_joc()

        if en_porta:
            if tresors_recollits["nivell2_clau"]:
                mostrar_text("E", font_petita, NEGRE, PORTA_SORTIDA.centerx, PORTA_SORTIDA.top - 20)
            else:
                mostrar_text("Falta clau", font_petita, VERMELL, PORTA_SORTIDA.centerx -100, PORTA_SORTIDA.top)

        if en_porta2 and not game_over:
            mostrar_text("E", font_petita, NEGRE, PORTA_SORTIDA2.centerx, PORTA_SORTIDA2.top - 20)

        if agente_mirant_dreta:
            PANTALLA.blit(agente_img_dreta, rect_agente)
            if not agente_inconsciente:
                PANTALLA.blit(deteccio_img_dreta, rect_deteccio)
        else:
            PANTALLA.blit(agente_img_esquerra, rect_agente)
            if not agente_inconsciente:
                PANTALLA.blit(deteccio_img_esquerra, rect_deteccio)

        if agente_inconsciente:
            temps_passat = temps_joc() - temps_inconsciente_inici
            temps_restant = 2 - (temps_passat // 1000)
            if temps_restant > 0:
                mostrar_text(str(temps_restant), font_petita, VERMELL, rect_agente.centerx, rect_agente.top - 20)

        if agente2_mirant_dreta:
            PANTALLA.blit(agente_img_dreta, rect_agente2)
            if not agente2_inconsciente:
                PANTALLA.blit(deteccio_img_dreta, rect_deteccio2)
        else:
            PANTALLA.blit(agente_img_esquerra, rect_agente2)
            if not agente2_inconsciente:
                PANTALLA.blit(deteccio_img_esquerra, rect_deteccio2)

        if agente2_inconsciente:
            temps_passat2 = temps_joc() - temps_inconsciente_inici2
            temps_restant2 = 2 - (temps_passat2 // 1000)
            if temps_restant2 > 0:
                mostrar_text(str(temps_restant2), font_petita, VERMELL, rect_agente2.centerx, rect_agente2.top - 20)

        if en_estado_robo:
            imatges_jugador_actuals = jugador_estado_dreta if mirant_dreta else jugador_estado_esquerra
        else:
            imatges_jugador_actuals = jugador_img_dreta if mirant_dreta else jugador_img_esquerra

        caminant = tecles[K_a] or tecles[K_d]
        PANTALLA.blit(obtenir_frame_jugador(imatges_jugador_actuals, caminant, en_terra), jugador_rect)

        if game_over:
            mostrar_text("GAME  OVER", font_gran, VERMELL, AMPLADA // 2, ALCADA // 2 - 20)
            mostrar_text("Prem  ENTER  per  reiniciar", font_petita, BLANC, AMPLADA // 2, ALCADA // 2 + 40)

        actualitzar_pantalla_amb_transicio()


def nivell2_pantalla3(reiniciar=False, pos_x_inici=50):
    global jugador_rect, mirant_dreta, vel_y, en_terra, textos_vistos, tresors_recollits, moment_pausa_inici, temps_pausa_acumulat

    if moment_pausa_inici is not None:
        temps_pausa_acumulat += pygame.time.get_ticks() - moment_pausa_inici
        moment_pausa_inici = None

    jugant = True
    game_over = False

    amplada_jugador, alcada_jugador = 40, 80
    jugador_img_dreta, jugador_img_esquerra = carregar_animacio_jugador(
        "Alex_quiet.png", "Alex_frame1.png", "Alex_frame2.png", "Alex_salt.png",
        amplada_jugador, alcada_jugador
    )
    jugador_estado_dreta, jugador_estado_esquerra = carregar_animacio_jugador(
        "Alex_estado_quiet.png", "Alex_estado_frame1.png", "Alex_estado_frame2.png", "Alex_estado_salt.png",
        amplada_jugador, alcada_jugador
    )

    rect_tresor = nivell2_or.get_rect(topleft=(170, 390))
    rect_tresor2 = nivell2_or2.get_rect(topleft=(370, 390))
    rect_tresor3 = nivell2_or3.get_rect(topleft=(570, 390))
    rect_tresor4 = nivell2_or4.get_rect(topleft=(770, 390))

    if reiniciar or jugador_rect is None:
        jugador_rect = jugador_img_dreta["quiet"].get_rect(topleft=(pos_x_inici, 444))
        if pos_x_inici > 400:
            mirant_dreta = False
        else:
            mirant_dreta = True
        vel_y = 0
        en_terra = True

    GRAVETAT = 0.8
    FORCA_SALT = -14
    ALTURA_SOL = 390
    LIMIT_SOSTRE = 0
    LIMIT_ESQUERRA = 20
    LIMIT_DRETA = 870
    PORTA_SORTIDA = pygame.Rect(840, 333, 50, 100)
    PORTA_SORTIDA2 = pygame.Rect(0, 333, 50, 100)

    camara_x = 180
    camara_y = 50
    camara_rect = camara_img.get_rect(center=(camara_x, camara_y))
    amplada_cono_base = 250
    superficie_cono = pygame.Surface((AMPLADA, ALCADA), pygame.SRCALPHA)

    camara2_x = 380
    camara2_y = 50
    camara2_rect = camara_img.get_rect(center=(camara2_x, camara2_y))
    amplada_cono2_base = 250
    superficie_cono2 = pygame.Surface((AMPLADA, ALCADA), pygame.SRCALPHA)

    camara3_x = 580
    camara3_y = 50
    camara3_rect = camara_img.get_rect(center=(camara3_x, camara3_y))
    amplada_cono3_base = 250
    superficie_cono3 = pygame.Surface((AMPLADA, ALCADA), pygame.SRCALPHA)

    camara4_x = 780
    camara4_y = 50
    camara4_rect = camara_img.get_rect(center=(camara4_x, camara4_y))
    amplada_cono4_base = 250
    superficie_cono4 = pygame.Surface((AMPLADA, ALCADA), pygame.SRCALPHA)

    en_estado_robo = False
    cono_camara_activat = True
    cono2_camara_activat = True
    cono3_camara_activat = True
    cono4_camara_activat = True
    laser_activat = False

    while jugant:
        clock.tick(60)
        en_porta = jugador_rect.colliderect(PORTA_SORTIDA)
        en_porta2 = jugador_rect.colliderect(PORTA_SORTIDA2)
        temps_actual = temps_joc()
        en_vermell = (temps_actual % 3000) >= 1000

        if not tresors_recollits["nivell2_or"]:
            if jugador_rect.colliderect(rect_tresor):
                tresors_recollits["nivell2_or"] = True
                if so_recollit:
                    so_recollit.set_volume(volum_sfx)
                    so_recollit.play()
        if not tresors_recollits["nivell2_or2"]:
            if jugador_rect.colliderect(rect_tresor2):
                tresors_recollits["nivell2_or2"] = True
                if so_recollit:
                    so_recollit.set_volume(volum_sfx)
                    so_recollit.play()
        if not tresors_recollits["nivell2_or3"]:
            if jugador_rect.colliderect(rect_tresor3):
                tresors_recollits["nivell2_or3"] = True
                if so_recollit:
                    so_recollit.set_volume(volum_sfx)
                    so_recollit.play()
        if not tresors_recollits["nivell2_or4"]:
            if jugador_rect.colliderect(rect_tresor4):
                tresors_recollits["nivell2_or4"] = True
                if so_recollit:
                    so_recollit.set_volume(volum_sfx)
                    so_recollit.play()

        for event in pygame.event.get():
            if event.type == QUIT:
                iniciar_transicio()
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if game_over:
                    if event.key in (K_RETURN, K_KP_ENTER):
                        iniciar_transicio()
                        tresors_recollits["nivell2_or"] = False
                        tresors_recollits["nivell2_or2"] = False
                        tresors_recollits["nivell2_or3"] = False
                        tresors_recollits["nivell2_or4"] = False
                        return "REINICIAR"
                if event.key == K_ESCAPE:
                    moment_pausa_inici = pygame.time.get_ticks()
                    return "PAUSAN2.3"
                if event.key == K_e and en_porta and tresors_recollits["nivell2_or"] and tresors_recollits["nivell2_or2"] and tresors_recollits["nivell2_or3"] and tresors_recollits["nivell2_or4"]:
                    iniciar_transicio()
                    return "JUGANT_NIVELL2_PANTALLA4"
                if event.key == K_e and en_porta2:
                    iniciar_transicio()
                    return "JUGANT_NIVELL2_PANTALLA2"
                if event.key == K_f and not laser_activat:
                    en_estado_robo = not en_estado_robo
                if event.key == K_q and not en_estado_robo:
                    laser_activat = not laser_activat

        if not game_over:
            temps_actual = temps_joc()
            dx = 0
            tecles = pygame.key.get_pressed()
            if tecles[K_a]:
                dx = -5
                mirant_dreta = False
            elif tecles[K_d]:
                dx = 5
                mirant_dreta = True

            jugador_rect.x += dx
            if jugador_rect.x <= LIMIT_ESQUERRA:
                jugador_rect.x = LIMIT_ESQUERRA
            if jugador_rect.right >= LIMIT_DRETA:
                jugador_rect.right = LIMIT_DRETA

            if tecles[K_w] and en_terra:
                vel_y = FORCA_SALT
                en_terra = False
            if jugador_rect.top <= LIMIT_SOSTRE:
                jugador_rect.top = LIMIT_SOSTRE
                vel_y = 0

            vel_y += GRAVETAT
            jugador_rect.y += vel_y
            en_terra = False

            if jugador_rect.y >= ALTURA_SOL:
                jugador_rect.y = ALTURA_SOL
                vel_y = 0
                en_terra = True

            detectat_cam = False
            if cono_camara_activat:
                if jugador_rect.top < (ALTURA_SOL + alcada_jugador) and jugador_rect.bottom > camara_y:
                    distancia_y = jugador_rect.centery - camara_y
                    altura_total = (ALTURA_SOL + alcada_jugador) - camara_y
                    if distancia_y > 0:
                        anchura_actual = (distancia_y / altura_total) * amplada_cono_base
                        limite_izq = camara_x - (anchura_actual / 4)
                        limite_der = camara_x + (anchura_actual / 4)
                        if jugador_rect.right > limite_izq and jugador_rect.left < limite_der:
                            detectat_cam = True
            if cono2_camara_activat:
                if jugador_rect.top < (ALTURA_SOL + alcada_jugador) and jugador_rect.bottom > camara2_y:
                    distancia_y = jugador_rect.centery - camara2_y
                    altura_total = (ALTURA_SOL + alcada_jugador) - camara2_y
                    if distancia_y > 0:
                        anchura_actual = (distancia_y / altura_total) * amplada_cono2_base
                        limite_izq = camara2_x - (anchura_actual / 4)
                        limite_der = camara2_x + (anchura_actual / 4)
                        if jugador_rect.right > limite_izq and jugador_rect.left < limite_der:
                            detectat_cam = True
            if cono3_camara_activat:
                if jugador_rect.top < (ALTURA_SOL + alcada_jugador) and jugador_rect.bottom > camara3_y:
                    distancia_y = jugador_rect.centery - camara3_y
                    altura_total = (ALTURA_SOL + alcada_jugador) - camara3_y
                    if distancia_y > 0:
                        anchura_actual = (distancia_y / altura_total) * amplada_cono3_base
                        limite_izq = camara3_x - (anchura_actual / 4)
                        limite_der = camara3_x + (anchura_actual / 4)
                        if jugador_rect.right > limite_izq and jugador_rect.left < limite_der:
                            detectat_cam = True
            if cono4_camara_activat:
                if jugador_rect.top < (ALTURA_SOL + alcada_jugador) and jugador_rect.bottom > camara4_y:
                    distancia_y = jugador_rect.centery - camara4_y
                    altura_total = (ALTURA_SOL + alcada_jugador) - camara4_y
                    if distancia_y > 0:
                        anchura_actual = (distancia_y / altura_total) * amplada_cono4_base
                        limite_izq = camara4_x - (anchura_actual / 4)
                        limite_der = camara4_x + (anchura_actual / 4)
                        if jugador_rect.right > limite_izq and jugador_rect.left < limite_der:
                            detectat_cam = True
            if en_vermell and detectat_cam:
                game_over = True

        PANTALLA.blit(fons_banc3, (0, 0))
        PANTALLA.blit(camara_img, camara_rect)
        PANTALLA.blit(camara_img, camara2_rect)
        PANTALLA.blit(camara_img, camara3_rect)
        PANTALLA.blit(camara_img, camara4_rect)

        if not tresors_recollits["nivell2_or"]:
            PANTALLA.blit(nivell2_or, rect_tresor)
        if not tresors_recollits["nivell2_or2"]:
            PANTALLA.blit(nivell2_or2, rect_tresor2)
        if not tresors_recollits["nivell2_or3"]:
            PANTALLA.blit(nivell2_or3, rect_tresor3)
        if not tresors_recollits["nivell2_or4"]:
            PANTALLA.blit(nivell2_or4, rect_tresor4)

        superficie_cono.fill((0, 0, 0, 0))
        superficie_cono2.fill((0, 0, 0, 0))
        superficie_cono3.fill((0, 0, 0, 0))
        superficie_cono4.fill((0, 0, 0, 0))

        if cono_camara_activat:
            if en_vermell:
                color_cono = (255, 0, 0, 100) if game_over or detectat_cam else (255, 0, 0, 70)
                color_cono2 = (255, 0, 0, 100) if game_over or detectat_cam else (255, 0, 0, 70)
                color_cono3 = (255, 0, 0, 100) if game_over or detectat_cam else (255, 0, 0, 70)
                color_cono4 = (255, 0, 0, 100) if game_over or detectat_cam else (255, 0, 0, 70)
            else:
                color_cono = (0, 255, 0, 70)
                color_cono2 = (0, 255, 0, 70)
                color_cono3 = (0, 255, 0, 70)
                color_cono4 = (0, 255, 0, 70)

            punts_cono = [
                (camara_x, camara_y - 5),
                (camara_x - amplada_cono_base/4, ALTURA_SOL + alcada_jugador),
                (camara_x + amplada_cono_base/4, ALTURA_SOL + alcada_jugador)
            ]
            punts_cono2 = [
                (camara2_x, camara2_y - 5),
                (camara2_x - amplada_cono2_base/4, ALTURA_SOL + alcada_jugador),
                (camara2_x + amplada_cono2_base/4, ALTURA_SOL + alcada_jugador)
            ]
            punts_cono3 = [
                (camara3_x, camara3_y - 5),
                (camara3_x - amplada_cono3_base/4, ALTURA_SOL + alcada_jugador),
                (camara3_x + amplada_cono3_base/4, ALTURA_SOL + alcada_jugador)
            ]
            punts_cono4 = [
                (camara4_x, camara4_y - 5),
                (camara4_x - amplada_cono4_base/4, ALTURA_SOL + alcada_jugador),
                (camara4_x + amplada_cono4_base/4, ALTURA_SOL + alcada_jugador)
            ]
            pygame.draw.polygon(superficie_cono, color_cono, punts_cono)
            PANTALLA.blit(superficie_cono, (0, 0))
            pygame.draw.polygon(superficie_cono2, color_cono2, punts_cono2)
            PANTALLA.blit(superficie_cono2, (0, 0))
            pygame.draw.polygon(superficie_cono3, color_cono3, punts_cono3)
            PANTALLA.blit(superficie_cono3, (0, 0))
            pygame.draw.polygon(superficie_cono4, color_cono4, punts_cono4)
            PANTALLA.blit(superficie_cono4, (0, 0))

        if laser_activat:
            clau_frame_actual = obtenir_clau_frame_jugador(tecles[K_a] or tecles[K_d], en_terra)
            punt_ma_laser = punt_origen_laser(jugador_rect, mirant_dreta, clau_frame_actual)
            pos_mousse = pygame.mouse.get_pos()
            pos_final_laser = pos_mousse
            min_dist_sq = (pos_mousse[0] - punt_ma_laser[0])**2 + (pos_mousse[1] - punt_ma_laser[1])**2

            rect_terra = pygame.Rect(0, ALTURA_SOL + alcada_jugador, 2000, 500)
            rect_sostre = pygame.Rect(0, -500, 2000, 500 + LIMIT_SOSTRE)
            rect_esquerra = pygame.Rect(-500, 0, 500 + LIMIT_ESQUERRA, 2000)
            rect_dreta = pygame.Rect(LIMIT_DRETA, 0, 500, 2000)
            obstacles_laser = [rect_terra, rect_sostre, rect_esquerra, rect_dreta]

            for obs in obstacles_laser:
                interseccions = obs.clipline(punt_ma_laser, pos_mousse)
                if interseccions:
                    for pt in interseccions:
                        dist_sq = (pt[0] - punt_ma_laser[0])**2 + (pt[1] - punt_ma_laser[1])**2
                        if dist_sq < min_dist_sq:
                            min_dist_sq = dist_sq
                            pos_final_laser = pt
            pygame.draw.line(PANTALLA, (255, 0, 0), punt_ma_laser, pos_final_laser, 3)

        if en_porta:
            if tresors_recollits["nivell2_or"] and tresors_recollits["nivell2_or2"] and tresors_recollits["nivell2_or3"] and tresors_recollits["nivell2_or4"]:
                mostrar_text("E", font_petita, NEGRE, PORTA_SORTIDA.centerx, PORTA_SORTIDA.top - 20)
            else:
                mostrar_text("Falta tresor", font_petita, VERMELL, PORTA_SORTIDA.centerx -100, PORTA_SORTIDA.top)

        if en_porta2 and not game_over:
            mostrar_text("E", font_petita, NEGRE, PORTA_SORTIDA2.centerx, PORTA_SORTIDA2.top - 20)

        if en_estado_robo:
            imatges_jugador_actuals = jugador_estado_dreta if mirant_dreta else jugador_estado_esquerra
        else:
            imatges_jugador_actuals = jugador_img_dreta if mirant_dreta else jugador_img_esquerra

        caminant = tecles[K_a] or tecles[K_d]
        PANTALLA.blit(obtenir_frame_jugador(imatges_jugador_actuals, caminant, en_terra), jugador_rect)

        if game_over:
            mostrar_text("GAME  OVER", font_gran, VERMELL, AMPLADA // 2, ALCADA // 2 - 20)
            mostrar_text("Prem  ENTER  per  reiniciar", font_petita, BLANC, AMPLADA // 2, ALCADA // 2 + 40)

        actualitzar_pantalla_amb_transicio()

def nivell2_pantalla4(reiniciar=False, pos_x_inici=50):
    global jugador_rect, mirant_dreta, vel_y, en_terra, textos_vistos, moment_pausa_inici, temps_pausa_acumulat

    if moment_pausa_inici is not None:
        temps_pausa_acumulat += pygame.time.get_ticks() - moment_pausa_inici
        moment_pausa_inici = None

    jugant = True
    game_over = False

    amplada_jugador, alcada_jugador = 40, 80
    jugador_img_dreta, jugador_img_esquerra = carregar_animacio_jugador(
        "Alex_quiet.png", "Alex_frame1.png", "Alex_frame2.png", "Alex_salt.png",
        amplada_jugador, alcada_jugador
    )
    jugador_estado_dreta, jugador_estado_esquerra = carregar_animacio_jugador(
        "Alex_estado_quiet.png", "Alex_estado_frame1.png", "Alex_estado_frame2.png", "Alex_estado_salt.png",
        amplada_jugador, alcada_jugador
    )

    amplada_mur = img_repisa.get_width()
    alcada_mur = img_repisa.get_height()

    if reiniciar or jugador_rect is None:
        jugador_rect = jugador_img_dreta["quiet"].get_rect(topleft=(pos_x_inici, 444))
        if pos_x_inici > 400:
            mirant_dreta = False
        else:
            mirant_dreta = True
        vel_y = 0
        en_terra = True

    GRAVETAT = 0.8
    FORCA_SALT = -14
    ALTURA_SOL = 390
    LIMIT_SOSTRE = 0
    LIMIT_ESQUERRA = 20
    LIMIT_DRETA = 870
    PORTA_SORTIDA = pygame.Rect(840, 333, 50, 100)
    PORTA_SORTIDA2 = pygame.Rect(0, 333, 50, 100)

    murs = [
        pygame.Rect(600, 200, amplada_mur, alcada_mur),
        pygame.Rect(450, 200, amplada_mur, alcada_mur),
        pygame.Rect(300, 300, amplada_mur, alcada_mur),
        pygame.Rect(450, 400, amplada_mur, alcada_mur),
    ]

    camara_x = 180
    camara_y = 50
    camara_rect = camara_img.get_rect(center=(camara_x, camara_y))
    amplada_cono_base = 250
    superficie_cono = pygame.Surface((AMPLADA, ALCADA), pygame.SRCALPHA)

    camara2_x = 640
    camara2_y = 230
    camara2_rect = camara_img.get_rect(center=(camara2_x, camara2_y))
    amplada_cono2_base = 250
    superficie_cono2 = pygame.Surface((AMPLADA, ALCADA), pygame.SRCALPHA)

    en_estado_robo = False
    cono_camara_activat = True
    cono2_camara_activat = True
    laser_activat = False

    while jugant:
        clock.tick(60)
        en_porta = jugador_rect.colliderect(PORTA_SORTIDA)
        en_porta2 = jugador_rect.colliderect(PORTA_SORTIDA2)
        temps_actual = temps_joc()
        temps_actual2 = temps_joc()
        en_vermell = (temps_actual % 3000) >= 1000
        en_vermell2 = (temps_actual2 % 3000) >= 0

        for event in pygame.event.get():
            if event.type == QUIT:
                iniciar_transicio()
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if game_over:
                    if event.key in (K_RETURN, K_KP_ENTER):
                        iniciar_transicio()
                        return "REINICIAR"
                if event.key == K_ESCAPE:
                    moment_pausa_inici = pygame.time.get_ticks()
                    return "PAUSAN2.4"
                if event.key == K_e and en_porta:
                    iniciar_transicio()
                    nivells_completats["nivell2"] = True
                    return "JUGANT_NIVELL2_FINAL"
                if event.key == K_e and en_porta2:
                    iniciar_transicio()
                    return "JUGANT_NIVELL2_PANTALLA3"
                if event.key == K_f and not laser_activat:
                    en_estado_robo = not en_estado_robo
                if event.key == K_q and not en_estado_robo:
                    laser_activat = not laser_activat

        if not game_over:
            temps_actual = temps_joc()
            temps_actual2 = temps_joc()
            dx = 0
            tecles = pygame.key.get_pressed()
            if tecles[K_a]:
                dx = -5
                mirant_dreta = False
            elif tecles[K_d]:
                dx = 5
                mirant_dreta = True

            jugador_rect.x += dx
            if jugador_rect.x <= LIMIT_ESQUERRA:
                jugador_rect.x = LIMIT_ESQUERRA
            if jugador_rect.right >= LIMIT_DRETA:
                jugador_rect.right = LIMIT_DRETA

            for mur in murs:
                if jugador_rect.colliderect(mur):
                    if dx > 0:
                        jugador_rect.right = mur.left
                    elif dx < 0:
                        jugador_rect.left = mur.right

            if tecles[K_w] and en_terra:
                vel_y = FORCA_SALT
                en_terra = False
            if jugador_rect.top <= LIMIT_SOSTRE:
                jugador_rect.top = LIMIT_SOSTRE
                vel_y = 0

            vel_y += GRAVETAT
            jugador_rect.y += vel_y
            en_terra = False

            if jugador_rect.y >= ALTURA_SOL:
                jugador_rect.y = ALTURA_SOL
                vel_y = 0
                en_terra = True

            for mur in murs:
                if jugador_rect.colliderect(mur):
                    if vel_y > 0:
                        jugador_rect.bottom = mur.top
                        vel_y = 0
                        en_terra = True
                    elif vel_y < 0:
                        jugador_rect.top = mur.bottom
                        vel_y = 0

            detectat_cam = False
            detectat_cam2 = False

            if cono_camara_activat:
                if jugador_rect.top < (ALTURA_SOL + alcada_jugador) and jugador_rect.bottom > camara_y:
                    distancia_y = jugador_rect.centery - camara_y
                    altura_total = (ALTURA_SOL + alcada_jugador) - camara_y
                    if distancia_y > 0:
                        anchura_actual = (distancia_y / altura_total) * amplada_cono_base
                        limite_izq = camara_x - (anchura_actual / 4)
                        limite_der = camara_x + (anchura_actual / 4)
                        if jugador_rect.right > limite_izq and jugador_rect.left < limite_der:
                            detectat_cam = True

            if cono2_camara_activat:
                if jugador_rect.top < (ALTURA_SOL + alcada_jugador) and jugador_rect.bottom > camara2_y:
                    distancia_y = jugador_rect.centery - camara2_y
                    altura_total = (ALTURA_SOL + alcada_jugador) - camara2_y
                    if distancia_y > 0:
                        anchura_actual = (distancia_y / altura_total) * amplada_cono2_base
                        limite_izq = camara2_x - (anchura_actual / 4)
                        limite_der = camara2_x + (anchura_actual / 4)
                        if jugador_rect.right > limite_izq and jugador_rect.left < limite_der:
                            detectat_cam2 = True

            if en_vermell and detectat_cam:
                game_over = True
            if en_vermell2 and detectat_cam2:
                game_over = True

        PANTALLA.blit(fons_banc4, (0, 0))
        for mur in murs:
            PANTALLA.blit(img_repisa, (mur.x, mur.y))

        PANTALLA.blit(camara_img, camara_rect)
        PANTALLA.blit(camara_img, camara2_rect)

        superficie_cono.fill((0, 0, 0, 0))
        superficie_cono2.fill((0, 0, 0, 0))

        if cono_camara_activat:
            if en_vermell:
                color_cono = (255, 0, 0, 100) if game_over or detectat_cam else (255, 0, 0, 70)
            else:
                color_cono = (0, 255, 0, 70)
            punts_cono = [
                (camara_x, camara_y - 5),
                (camara_x - amplada_cono_base/4, ALTURA_SOL + alcada_jugador),
                (camara_x + amplada_cono_base/4, ALTURA_SOL + alcada_jugador)
            ]
            pygame.draw.polygon(superficie_cono, color_cono, punts_cono)
            PANTALLA.blit(superficie_cono, (0, 0))

        if cono2_camara_activat:
            if en_vermell2:
                color_cono2 = (255, 0, 0, 100) if game_over or detectat_cam2 else (255, 0, 0, 70)
            else:
                color_cono2 = (0, 255, 0, 70)
            punts_cono2 = [
                (camara2_x, camara2_y - 5),
                (camara2_x - amplada_cono2_base/4, ALTURA_SOL + alcada_jugador),
                (camara2_x + amplada_cono2_base/4, ALTURA_SOL + alcada_jugador)
            ]
            pygame.draw.polygon(superficie_cono2, color_cono2, punts_cono2)
            PANTALLA.blit(superficie_cono2, (0, 0))

        if laser_activat:
            clau_frame_actual = obtenir_clau_frame_jugador(tecles[K_a] or tecles[K_d], en_terra)
            punt_ma_laser = punt_origen_laser(jugador_rect, mirant_dreta, clau_frame_actual)
            pos_mousse = pygame.mouse.get_pos()
            pos_final_laser = pos_mousse
            min_dist_sq = (pos_mousse[0] - punt_ma_laser[0])**2 + (pos_mousse[1] - punt_ma_laser[1])**2
            rect_terra = pygame.Rect(0, ALTURA_SOL + alcada_jugador, 2000, 500)
            rect_sostre = pygame.Rect(0, -500, 2000, 500 + LIMIT_SOSTRE)
            rect_esquerra = pygame.Rect(-500, 0, 500 + LIMIT_ESQUERRA, 2000)
            rect_dreta = pygame.Rect(LIMIT_DRETA, 0, 500, 2000)
            obstacles_laser = [rect_terra, rect_sostre, rect_esquerra, rect_dreta]

            for obs in obstacles_laser:
                interseccions = obs.clipline(punt_ma_laser, pos_mousse)
                if interseccions:
                    for pt in interseccions:
                        dist_sq = (pt[0] - punt_ma_laser[0])**2 + (pt[1] - punt_ma_laser[1])**2
                        if dist_sq < min_dist_sq:
                            min_dist_sq = dist_sq
                            pos_final_laser = pt
            pygame.draw.line(PANTALLA, (255, 0, 0), punt_ma_laser, pos_final_laser, 3)

        if en_porta:
            mostrar_text("E", font_petita, NEGRE, PORTA_SORTIDA.centerx, PORTA_SORTIDA.top - 20)
        if en_porta2 and not game_over:
            mostrar_text("E", font_petita, NEGRE, PORTA_SORTIDA2.centerx, PORTA_SORTIDA2.top - 20)

        if en_estado_robo:
            imatges_jugador_actuals = jugador_estado_dreta if mirant_dreta else jugador_estado_esquerra
        else:
            imatges_jugador_actuals = jugador_img_dreta if mirant_dreta else jugador_img_esquerra

        caminant = tecles[K_a] or tecles[K_d]
        PANTALLA.blit(obtenir_frame_jugador(imatges_jugador_actuals, caminant, en_terra), jugador_rect)

        if game_over:
            mostrar_text("GAME  OVER", font_gran, VERMELL, AMPLADA // 2, ALCADA // 2 - 20)
            mostrar_text("Prem  ENTER  per  reiniciar", font_petita, BLANC, AMPLADA // 2, ALCADA // 2 + 40)

        actualitzar_pantalla_amb_transicio()

def nivell3_pantalla1(reiniciar=False, pos_x_inici=50):
    global jugador_rect, mirant_dreta, vel_y, en_terra, textos_vistos, tresors_recollits, moment_pausa_inici, temps_pausa_acumulat
    if moment_pausa_inici is not None:
        temps_pausa_acumulat += pygame.time.get_ticks() - moment_pausa_inici
        moment_pausa_inici = None
    jugant = True
    game_over = False
    canviar_musica("niv3.mp3")
    amplada_jugador, alcada_jugador = 40, 80
    jugador_img_dreta, jugador_img_esquerra = carregar_animacio_jugador(
        "Alex_quiet.png", "Alex_frame1.png", "Alex_frame2.png", "Alex_salt.png",
        amplada_jugador, alcada_jugador
    )
    jugador_estado_dreta, jugador_estado_esquerra = carregar_animacio_jugador(
        "Alex_estado_quiet.png", "Alex_estado_frame1.png", "Alex_estado_frame2.png", "Alex_estado_salt.png",
        amplada_jugador, alcada_jugador
    )

    amplada_mur = img_repisa.get_width()
    alcada_mur = img_repisa.get_height()
    boto_rect = boto_img.get_rect(topleft=(120, 150))
    rect_agente = agente_img_base.get_rect(topleft=(220, 120))
    rect_deteccio = deteccio_img_base.get_rect()
    agente_mirant_dreta = False
    ultim_canvi_agente = temps_joc()
    agente_inconsciente = False
    temps_inconsciente_inici = 0
    rect_tresor = nivell3_gerro.get_rect(topleft=(330, 265))

    if reiniciar or jugador_rect is None:
        jugador_rect = jugador_img_dreta["quiet"].get_rect(topleft=(pos_x_inici, 444))
        if pos_x_inici > 400:
            mirant_dreta = False
        else:
            mirant_dreta = True
        vel_y = 0
        en_terra = True

    GRAVETAT = 0.8
    FORCA_SALT = -14
    ALTURA_SOL = 390
    LIMIT_SOSTRE = 0
    LIMIT_ESQUERRA = 20
    LIMIT_DRETA = 870
    PORTA_SORTIDA = pygame.Rect(840, 333, 50, 100)
    PORTA_SORTIDA2 = pygame.Rect(0, 333, 50, 100)

    murs = [
        pygame.Rect(100, 200, amplada_mur, alcada_mur),
        pygame.Rect(200, 200, amplada_mur, alcada_mur),
        pygame.Rect(300, 300, amplada_mur, alcada_mur),
        pygame.Rect(450, 400, amplada_mur, alcada_mur),
    ]

    camara_x = 240
    camara_y = 50
    camara_rect = camara_img.get_rect(center=(camara_x, camara_y))
    amplada_cono_base = 250
    superficie_cono = pygame.Surface((AMPLADA, ALCADA), pygame.SRCALPHA)

    camara2_x = 640
    camara2_y = 50
    camara2_rect = camara_img.get_rect(center=(camara2_x, camara2_y))
    amplada_cono2_base = 250
    superficie_cono2 = pygame.Surface((AMPLADA, ALCADA), pygame.SRCALPHA)

    en_estado_robo = False
    cono_camara_activat = True
    cono2_camara_activat = True
    laser_activat = False

    while jugant:
        clock.tick(60)
        en_porta = jugador_rect.colliderect(PORTA_SORTIDA)
        en_porta2 = jugador_rect.colliderect(PORTA_SORTIDA2)
        en_boto = jugador_rect.colliderect(boto_rect)

        temps_actual = temps_joc()
        temps_actual2 = temps_joc()
        en_vermell = (temps_actual % 3000) >= 1000
        en_vermell2 = (temps_actual2 % 3000) >= 0

        if not tresors_recollits["nivell3_gerro"]:
            if jugador_rect.colliderect(rect_tresor):
                tresors_recollits["nivell3_gerro"] = True
                if so_recollit:
                    so_recollit.set_volume(volum_sfx)
                    so_recollit.play()

        for event in pygame.event.get():
            if event.type == QUIT:
                iniciar_transicio()
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if game_over:
                    if event.key in (K_RETURN, K_KP_ENTER):
                        iniciar_transicio()
                        tresors_recollits["nivell3_gerro"] = False
                        return "REINICIAR"
                if event.key == K_ESCAPE:
                    moment_pausa_inici = pygame.time.get_ticks()
                    return "PAUSAN3.1"
                if event.key == K_e and en_porta and tresors_recollits["nivell3_gerro"]:
                    iniciar_transicio()
                    return "JUGANT_NIVELL3_PANTALLA2"
                if event.key == K_f and not laser_activat:
                    en_estado_robo = not en_estado_robo
                if event.key == K_q and not en_estado_robo:
                    laser_activat = not laser_activat
                if event.key == K_e and en_boto and en_estado_robo:
                    cono2_camara_activat = not cono2_camara_activat

        if not game_over:
            temps_actual = temps_joc()
            temps_actual2 = temps_joc()

            if agente_inconsciente:
                if temps_actual - temps_inconsciente_inici >= 2000:
                    agente_inconsciente = False

            if temps_actual - ultim_canvi_agente >= 7000:
                agente_mirant_dreta = not agente_mirant_dreta
                ultim_canvi_agente = temps_actual

            altura_ojos = rect_agente.top + int(rect_agente.height * 0.22)
            if agente_mirant_dreta:
                rect_deteccio.left = rect_agente.right - 5
                rect_deteccio.centery = altura_ojos
            else:
                rect_deteccio.right = rect_agente.left + 5
                rect_deteccio.centery = altura_ojos

            dx = 0
            tecles = pygame.key.get_pressed()
            if tecles[K_a]:
                dx = -5
                mirant_dreta = False
            elif tecles[K_d]:
                dx = 5
                mirant_dreta = True

            jugador_rect.x += dx
            if jugador_rect.x <= LIMIT_ESQUERRA:
                jugador_rect.x = LIMIT_ESQUERRA
            if jugador_rect.right >= LIMIT_DRETA:
                jugador_rect.right = LIMIT_DRETA

            for mur in murs:
                if jugador_rect.colliderect(mur):
                    if dx > 0:
                        jugador_rect.right = mur.left
                    elif dx < 0:
                        jugador_rect.left = mur.right

            if tecles[K_w] and en_terra:
                vel_y = FORCA_SALT
                en_terra = False

            if jugador_rect.top <= LIMIT_SOSTRE:
                jugador_rect.top = LIMIT_SOSTRE
                vel_y = 0

            vel_y += GRAVETAT
            jugador_rect.y += vel_y
            en_terra = False

            if jugador_rect.y >= ALTURA_SOL:
                jugador_rect.y = ALTURA_SOL
                vel_y = 0
                en_terra = True

            for mur in murs:
                if jugador_rect.colliderect(mur):
                    if vel_y > 0:
                        jugador_rect.bottom = mur.top
                        vel_y = 0
                        en_terra = True
                    elif vel_y < 0:
                        jugador_rect.top = mur.bottom
                        vel_y = 0

            detectat_agente = False
            detectat_cam = False
            detectat_cam2 = False

            if not agente_inconsciente:
                if jugador_rect.colliderect(rect_deteccio):
                    detectat_agente = True

            if detectat_agente:
                game_over = True

            if cono_camara_activat:
                if jugador_rect.top < (ALTURA_SOL + alcada_jugador) and jugador_rect.bottom > camara_y:
                    distancia_y = jugador_rect.centery - camara_y
                    altura_total = (ALTURA_SOL + alcada_jugador) - camara_y
                    if distancia_y > 0:
                        anchura_actual = (distancia_y / altura_total) * amplada_cono_base
                        limite_izq = camara_x - (anchura_actual / 4)
                        limite_der = camara_x + (anchura_actual / 4)
                        if jugador_rect.right > limite_izq and jugador_rect.left < limite_der:
                            detectat_cam = True

            if cono2_camara_activat:
                if jugador_rect.top < (ALTURA_SOL + alcada_jugador) and jugador_rect.bottom > camara2_y:
                    distancia_y = jugador_rect.centery - camara2_y
                    altura_total = (ALTURA_SOL + alcada_jugador) - camara2_y
                    if distancia_y > 0:
                        anchura_actual = (distancia_y / altura_total) * amplada_cono2_base
                        limite_izq = camara2_x - (anchura_actual / 4)
                        limite_der = camara2_x + (anchura_actual / 4)
                        if jugador_rect.right > limite_izq and jugador_rect.left < limite_der:
                            detectat_cam2 = True

            if en_vermell and detectat_cam:
                game_over = True
            if en_vermell2 and detectat_cam2:
                game_over = True

        PANTALLA.blit(fons_casa, (0, 0))
        for mur in murs:
            PANTALLA.blit(img_repisa, (mur.x, mur.y))
        PANTALLA.blit(camara_img, camara_rect)
        PANTALLA.blit(camara_img, camara2_rect)
        PANTALLA.blit(boto_img, boto_rect)

        if not tresors_recollits["nivell3_gerro"]:
            PANTALLA.blit(nivell3_gerro, rect_tresor)

        superficie_cono.fill((0, 0, 0, 0))
        superficie_cono2.fill((0, 0, 0, 0))

        if cono_camara_activat:
            if en_vermell:
                color_cono = (255, 0, 0, 100) if game_over or detectat_cam else (255, 0, 0, 70)
            else:
                color_cono = (0, 255, 0, 70)
            punts_cono = [
                (camara_x, camara_y - 5),
                (camara_x - amplada_cono_base/4, ALTURA_SOL + alcada_jugador),
                (camara_x + amplada_cono_base/4, ALTURA_SOL + alcada_jugador)
            ]
            pygame.draw.polygon(superficie_cono, color_cono, punts_cono)
            PANTALLA.blit(superficie_cono, (0, 0))

        if cono2_camara_activat:
            if en_vermell2:
                color_cono2 = (255, 0, 0, 100) if game_over or detectat_cam2 else (255, 0, 0, 70)
            else:
                color_cono2 = (0, 255, 0, 70)
            punts_cono2 = [
                (camara2_x, camara2_y - 5),
                (camara2_x - amplada_cono2_base/4, ALTURA_SOL + alcada_jugador),
                (camara2_x + amplada_cono2_base/4, ALTURA_SOL + alcada_jugador)
            ]
            pygame.draw.polygon(superficie_cono2, color_cono2, punts_cono2)
            PANTALLA.blit(superficie_cono2, (0, 0))

        if laser_activat:
            clau_frame_actual = obtenir_clau_frame_jugador(tecles[K_a] or tecles[K_d], en_terra)
            punt_ma_laser = punt_origen_laser(jugador_rect, mirant_dreta, clau_frame_actual)
            pos_mousse = pygame.mouse.get_pos()
            pos_final_laser = pos_mousse
            min_dist_sq = (pos_mousse[0] - punt_ma_laser[0])**2 + (pos_mousse[1] - punt_ma_laser[1])**2
            rect_terra = pygame.Rect(0, ALTURA_SOL + alcada_jugador, 2000, 500)
            rect_sostre = pygame.Rect(0, -500, 2000, 500 + LIMIT_SOSTRE)
            rect_esquerra = pygame.Rect(-500, 0, 500 + LIMIT_ESQUERRA, 2000)
            rect_dreta = pygame.Rect(LIMIT_DRETA, 0, 500, 2000)
            obstacles_laser = murs + [rect_terra, rect_sostre, rect_esquerra, rect_dreta]

            for obs in obstacles_laser:
                interseccions = obs.clipline(punt_ma_laser, pos_mousse)
                if interseccions:
                    for pt in interseccions:
                        dist_sq = (pt[0] - punt_ma_laser[0])**2 + (pt[1] - punt_ma_laser[1])**2
                        if dist_sq < min_dist_sq:
                            min_dist_sq = dist_sq
                            pos_final_laser = pt

            pygame.draw.line(PANTALLA, (255, 0, 0), punt_ma_laser, pos_final_laser, 3)

            if not game_over:
                if rect_agente.collidepoint(pos_final_laser) or rect_agente.clipline(punt_ma_laser, pos_final_laser):
                    agente_inconsciente = True
                    temps_inconsciente_inici = temps_joc()

        if en_boto and not game_over:
            if en_estado_robo:
                mostrar_text("E", font_petita, NEGRE, boto_rect.centerx, boto_rect.top - 20)
            else:
                mostrar_text("Necesitaes cambi de mans", font_mes_petita, VERMELL, boto_rect.centerx + 50, boto_rect.top - 40)

        if en_porta:
            if tresors_recollits["nivell3_gerro"]:
                mostrar_text("E", font_petita, NEGRE, PORTA_SORTIDA.centerx, PORTA_SORTIDA.top - 20)
            else:
                mostrar_text("Falta tresor", font_petita, VERMELL, PORTA_SORTIDA.centerx -100, PORTA_SORTIDA.top)

        if en_porta2 and not game_over:
            mostrar_text("E", font_petita, NEGRE, PORTA_SORTIDA2.centerx, PORTA_SORTIDA2.top - 20)

        if agente_mirant_dreta:
            PANTALLA.blit(agente_img_dreta, rect_agente)
            if not agente_inconsciente:
                PANTALLA.blit(deteccio_img_dreta, rect_deteccio)
        else:
            PANTALLA.blit(agente_img_esquerra, rect_agente)
            if not agente_inconsciente:
                PANTALLA.blit(deteccio_img_esquerra, rect_deteccio)

        if agente_inconsciente:
            temps_passat = temps_joc() - temps_inconsciente_inici
            temps_restant = 2 - (temps_passat // 1000)
            if temps_restant > 0:
                mostrar_text(str(temps_restant), font_petita, VERMELL, rect_agente.centerx, rect_agente.top - 20)

        if en_estado_robo:
            imatges_jugador_actuals = jugador_estado_dreta if mirant_dreta else jugador_estado_esquerra
        else:
            imatges_jugador_actuals = jugador_img_dreta if mirant_dreta else jugador_img_esquerra

        caminant = tecles[K_a] or tecles[K_d]
        PANTALLA.blit(obtenir_frame_jugador(imatges_jugador_actuals, caminant, en_terra), jugador_rect)

        if game_over:
            mostrar_text("GAME  OVER", font_gran, VERMELL, AMPLADA // 2, ALCADA // 2 - 20)
            mostrar_text("Prem  ENTER  per  reiniciar", font_petita, BLANC, AMPLADA // 2, ALCADA // 2 + 40)

        actualitzar_pantalla_amb_transicio()

def nivell3_pantalla2(reiniciar=False, pos_x_inici=50):
    global jugador_rect, mirant_dreta, vel_y, en_terra, textos_vistos, tresors_recollits, moment_pausa_inici, temps_pausa_acumulat

    if moment_pausa_inici is not None:
        temps_pausa_acumulat += pygame.time.get_ticks() - moment_pausa_inici
        moment_pausa_inici = None

    jugant = True
    game_over = False
    amplada_jugador, alcada_jugador = 40, 80

    jugador_img_dreta, jugador_img_esquerra = carregar_animacio_jugador(
        "Alex_quiet.png", "Alex_frame1.png", "Alex_frame2.png", "Alex_salt.png",
        amplada_jugador, alcada_jugador
    )
    jugador_estado_dreta, jugador_estado_esquerra = carregar_animacio_jugador(
        "Alex_estado_quiet.png", "Alex_estado_frame1.png", "Alex_estado_frame2.png", "Alex_estado_salt.png",
        amplada_jugador, alcada_jugador
    )

    amplada_mur = img_repisa.get_width()
    alcada_mur = img_repisa.get_height()

    rect_tresor = nivell3_diamant.get_rect(topleft=(520, 130))

    rect_agente = agente_img_base.get_rect(topleft=(513, 215))
    rect_deteccio = deteccio_img_base.get_rect()
    agente_mirant_dreta = False
    ultim_canvi_agente = temps_joc()
    agente_inconsciente = False
    temps_inconsciente_inici = 0

    rect_agente2 = agente_img_base.get_rect(topleft=(335, 145))
    rect_deteccio2 = deteccio_img_base.get_rect()
    agente2_mirant_dreta = False
    ultim_canvi_agente2 = temps_joc()
    agente2_inconsciente = False
    temps_inconsciente_inici2 = 0

    if reiniciar or jugador_rect is None:
        jugador_rect = jugador_img_dreta["quiet"].get_rect(topleft=(pos_x_inici, 444))
        if pos_x_inici > 400:
            mirant_dreta = False
        else:
            mirant_dreta = True
        vel_y = 0
        en_terra = True

    GRAVETAT = 0.8
    FORCA_SALT = -14
    ALTURA_SOL = 390
    LIMIT_SOSTRE = 0
    LIMIT_ESQUERRA = 20
    LIMIT_DRETA = 870
    PORTA_SORTIDA = pygame.Rect(840, 333, 50, 100)
    PORTA_SORTIDA2 = pygame.Rect(0, 333, 50, 100)

    murs = [
        pygame.Rect(AMPLADA / 1.6666 - 45, 155, amplada_mur, alcada_mur),
        pygame.Rect(AMPLADA / 2.5 - 45, 225, amplada_mur, alcada_mur),
        pygame.Rect(AMPLADA / 1.6666 - 45, 295, amplada_mur, alcada_mur),
        pygame.Rect(AMPLADA / 2.5 - 45, 365, amplada_mur, alcada_mur),
    ]

    en_estado_robo = False
    laser_activat = False

    while jugant:
        clock.tick(60)
        en_porta = jugador_rect.colliderect(PORTA_SORTIDA)
        en_porta2 = jugador_rect.colliderect(PORTA_SORTIDA2)

        if not tresors_recollits["nivell3_diamant"]:
            if jugador_rect.colliderect(rect_tresor):
                tresors_recollits["nivell3_diamant"] = True
                if so_recollit:
                    so_recollit.set_volume(volum_sfx)
                    so_recollit.play()

        for event in pygame.event.get():
            if event.type == QUIT:
                iniciar_transicio()
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if game_over:
                    if event.key in (K_RETURN, K_KP_ENTER):
                        iniciar_transicio()
                        tresors_recollits["nivell3_diamant"] = False
                        return "REINICIAR"
                if event.key == K_ESCAPE:
                    moment_pausa_inici = pygame.time.get_ticks()
                    return "PAUSAN3.2"
                if event.key == K_e and en_porta and tresors_recollits["nivell3_diamant"]:
                    iniciar_transicio()
                    return "JUGANT_NIVELL3_PANTALLA3"
                if event.key == K_e and en_porta2:
                    iniciar_transicio()
                    return "JUGANT_NIVELL3_PANTALLA1"
                if event.key == K_f and not laser_activat:
                    en_estado_robo = not en_estado_robo
                if event.key == K_q and not en_estado_robo:
                    laser_activat = not laser_activat

        if not game_over:
            temps_actual = temps_joc()
            temps_actual2 = temps_joc()

            if agente_inconsciente:
                if temps_actual - temps_inconsciente_inici >= 2000:
                    agente_inconsciente = False
            if temps_actual - ultim_canvi_agente >= 7000:
                agente_mirant_dreta = not agente_mirant_dreta
                ultim_canvi_agente = temps_actual

            altura_ojos = rect_agente.top + int(rect_agente.height * 0.22)
            if agente_mirant_dreta:
                rect_deteccio.left = rect_agente.right - 5
                rect_deteccio.centery = altura_ojos
            else:
                rect_deteccio.right = rect_agente.left + 5
                rect_deteccio.centery = altura_ojos

            if agente2_inconsciente:
                if temps_actual2 - temps_inconsciente_inici2 >= 2000:
                    agente2_inconsciente = False
            if temps_actual2 - ultim_canvi_agente2 >= 7000:
                agente2_mirant_dreta = not agente2_mirant_dreta
                ultim_canvi_agente2 = temps_actual2

            altura_ojos2 = rect_agente2.top + int(rect_agente2.height * 0.22)
            if agente2_mirant_dreta:
                rect_deteccio2.left = rect_agente2.right - 5
                rect_deteccio2.centery = altura_ojos2
            else:
                rect_deteccio2.right = rect_agente2.left + 5
                rect_deteccio2.centery = altura_ojos2

            dx = 0
            tecles = pygame.key.get_pressed()
            if tecles[K_a]:
                dx = -5
                mirant_dreta = False
            elif tecles[K_d]:
                dx = 5
                mirant_dreta = True

            jugador_rect.x += dx
            if jugador_rect.x <= LIMIT_ESQUERRA:
                jugador_rect.x = LIMIT_ESQUERRA
            if jugador_rect.right >= LIMIT_DRETA:
                jugador_rect.right = LIMIT_DRETA

            for mur in murs:
                if jugador_rect.colliderect(mur):
                    if dx > 0:
                        jugador_rect.right = mur.left
                    elif dx < 0:
                        jugador_rect.left = mur.right

            if tecles[K_w] and en_terra:
                vel_y = FORCA_SALT
                en_terra = False

            if jugador_rect.top <= LIMIT_SOSTRE:
                jugador_rect.top = LIMIT_SOSTRE
                vel_y = 0

            vel_y += GRAVETAT
            jugador_rect.y += vel_y
            en_terra = False

            if jugador_rect.y >= ALTURA_SOL:
                jugador_rect.y = ALTURA_SOL
                vel_y = 0
                en_terra = True

            for mur in murs:
                if jugador_rect.colliderect(mur):
                    if vel_y > 0:
                        jugador_rect.bottom = mur.top
                        vel_y = 0
                        en_terra = True
                    elif vel_y < 0:
                        jugador_rect.top = mur.bottom
                        vel_y = 0

            detectat_agente = False
            detectat_agente2 = False

            if not agente_inconsciente:
                if jugador_rect.colliderect(rect_deteccio):
                    detectat_agente = True
            if not agente2_inconsciente:
                if jugador_rect.colliderect(rect_deteccio2):
                    detectat_agente2 = True

            if detectat_agente or detectat_agente2:
                game_over = True

        PANTALLA.blit(fons_casa, (0, 0))

        for mur in murs:
            PANTALLA.blit(img_repisa, (mur.x, mur.y))

        if not tresors_recollits["nivell3_diamant"]:
            PANTALLA.blit(nivell3_diamant, rect_tresor)

        if laser_activat:
            clau_frame_actual = obtenir_clau_frame_jugador(tecles[K_a] or tecles[K_d], en_terra)
            punt_ma_laser = punt_origen_laser(jugador_rect, mirant_dreta, clau_frame_actual)
            pos_mousse = pygame.mouse.get_pos()
            pos_final_laser = pos_mousse
            min_dist_sq = (pos_mousse[0] - punt_ma_laser[0])**2 + (pos_mousse[1] - punt_ma_laser[1])**2

            rect_terra = pygame.Rect(0, ALTURA_SOL + alcada_jugador, 2000, 500)
            rect_sostre = pygame.Rect(0, -500, 2000, 500 + LIMIT_SOSTRE)
            rect_esquerra = pygame.Rect(-500, 0, 500 + LIMIT_ESQUERRA, 2000)
            rect_dreta = pygame.Rect(LIMIT_DRETA, 0, 500, 2000)
            obstacles_laser = murs + [rect_terra, rect_sostre, rect_esquerra, rect_dreta]

            for obs in obstacles_laser:
                interseccions = obs.clipline(punt_ma_laser, pos_mousse)
                if interseccions:
                    for pt in interseccions:
                        dist_sq = (pt[0] - punt_ma_laser[0])**2 + (pt[1] - punt_ma_laser[1])**2
                        if dist_sq < min_dist_sq:
                            min_dist_sq = dist_sq
                            pos_final_laser = pt

            pygame.draw.line(PANTALLA, (255, 0, 0), punt_ma_laser, pos_final_laser, 3)

            if not game_over:
                if rect_agente.collidepoint(pos_final_laser) or rect_agente.clipline(punt_ma_laser, pos_final_laser):
                    agente_inconsciente = True
                    temps_inconsciente_inici = temps_joc()
                if rect_agente2.collidepoint(pos_final_laser) or rect_agente2.clipline(punt_ma_laser, pos_final_laser):
                    agente2_inconsciente = True
                    temps_inconsciente_inici2 = temps_joc()

        if en_porta:
            if tresors_recollits["nivell3_diamant"]:
                mostrar_text("E", font_petita, NEGRE, PORTA_SORTIDA.centerx, PORTA_SORTIDA.top - 20)
            else:
                mostrar_text("Falta tresor", font_petita, VERMELL, PORTA_SORTIDA.centerx -100, PORTA_SORTIDA.top)

        if en_porta2 and not game_over:
            mostrar_text("E", font_petita, NEGRE, PORTA_SORTIDA2.centerx, PORTA_SORTIDA2.top - 20)

        if agente_mirant_dreta:
            PANTALLA.blit(agente_img_dreta, rect_agente)
            if not agente_inconsciente:
                PANTALLA.blit(deteccio_img_dreta, rect_deteccio)
        else:
            PANTALLA.blit(agente_img_esquerra, rect_agente)
            if not agente_inconsciente:
                PANTALLA.blit(deteccio_img_esquerra, rect_deteccio)

        if agente_inconsciente:
            temps_passat = temps_joc() - temps_inconsciente_inici
            temps_restant = 2 - (temps_passat // 1000)
            if temps_restant > 0:
                mostrar_text(str(temps_restant), font_petita, VERMELL, rect_agente.centerx, rect_agente.top - 20)

        if agente2_mirant_dreta:
            PANTALLA.blit(agente_img_dreta, rect_agente2)
            if not agente2_inconsciente:
                PANTALLA.blit(deteccio_img_dreta, rect_deteccio2)
        else:
            PANTALLA.blit(agente_img_esquerra, rect_agente2)
            if not agente2_inconsciente:
                PANTALLA.blit(deteccio_img_esquerra, rect_deteccio2)

        if agente2_inconsciente:
            temps_passat2 = temps_joc() - temps_inconsciente_inici2
            temps_restant2 = 2 - (temps_passat2 // 1000)
            if temps_restant2 > 0:
                mostrar_text(str(temps_restant2), font_petita, VERMELL, rect_agente2.centerx, rect_agente2.top - 20)

        if en_estado_robo:
            imatges_jugador_actuals = jugador_estado_dreta if mirant_dreta else jugador_estado_esquerra
        else:
            imatges_jugador_actuals = jugador_img_dreta if mirant_dreta else jugador_img_esquerra

        caminant = tecles[K_a] or tecles[K_d]
        PANTALLA.blit(obtenir_frame_jugador(imatges_jugador_actuals, caminant, en_terra), jugador_rect)

        if game_over:
            mostrar_text("GAME  OVER", font_gran, VERMELL, AMPLADA // 2, ALCADA // 2 - 20)
            mostrar_text("Prem  ENTER  per  reiniciar", font_petita, BLANC, AMPLADA // 2, ALCADA // 2 + 40)

        actualitzar_pantalla_amb_transicio()

def nivell3_pantalla3(reiniciar=False, pos_x_inici=50):
    global jugador_rect, mirant_dreta, vel_y, en_terra, textos_vistos, moment_pausa_inici, temps_pausa_acumulat

    if moment_pausa_inici is not None:
        temps_pausa_acumulat += pygame.time.get_ticks() - moment_pausa_inici
        moment_pausa_inici = None

    jugant = True
    game_over = False

    amplada_jugador, alcada_jugador = 40, 80
    jugador_img_dreta, jugador_img_esquerra = carregar_animacio_jugador(
        "Alex_quiet.png", "Alex_frame1.png", "Alex_frame2.png", "Alex_salt.png",
        amplada_jugador, alcada_jugador
    )
    jugador_estado_dreta, jugador_estado_esquerra = carregar_animacio_jugador(
        "Alex_estado_quiet.png", "Alex_estado_frame1.png", "Alex_estado_frame2.png", "Alex_estado_salt.png",
        amplada_jugador, alcada_jugador
    )

    boto_rect = boto_img.get_rect(topleft=(370, 390))

    if reiniciar or jugador_rect is None:
        jugador_rect = jugador_img_dreta["quiet"].get_rect(topleft=(pos_x_inici, 444))
        if pos_x_inici > 400:
            mirant_dreta = False
        else:
            mirant_dreta = True
        vel_y = 0
        en_terra = True

    GRAVETAT = 0.8
    FORCA_SALT = -14
    ALTURA_SOL = 390
    LIMIT_SOSTRE = 0
    LIMIT_ESQUERRA = 20
    LIMIT_DRETA = 870
    PORTA_SORTIDA = pygame.Rect(840, 333, 50, 100)
    PORTA_SORTIDA2 = pygame.Rect(0, 333, 50, 100)

    camara_x = 180
    camara_y = 50
    camara_rect = camara_img.get_rect(center=(camara_x, camara_y))
    amplada_cono_base = 250
    superficie_cono = pygame.Surface((AMPLADA, ALCADA), pygame.SRCALPHA)

    camara3_x = 580
    camara3_y = 50
    camara3_rect = camara_img.get_rect(center=(camara3_x, camara3_y))
    amplada_cono3_base = 250
    superficie_cono3 = pygame.Surface((AMPLADA, ALCADA), pygame.SRCALPHA)

    camara4_x = 780
    camara4_y = 50
    camara4_rect = camara_img.get_rect(center=(camara4_x, camara4_y))
    amplada_cono4_base = 250
    superficie_cono4 = pygame.Surface((AMPLADA, ALCADA), pygame.SRCALPHA)

    en_estado_robo = False
    cono_camara_activat = True
    cono3_camara_activat = True
    cono4_camara_activat = True
    laser_activat = False

    while jugant:
        clock.tick(60)
        en_porta = jugador_rect.colliderect(PORTA_SORTIDA)
        en_porta2 = jugador_rect.colliderect(PORTA_SORTIDA2)
        en_boto = jugador_rect.colliderect(boto_rect)
        temps_actual = temps_joc()
        en_vermell = (temps_actual % 3000) >= 1000
        temps_actual2 = temps_joc()
        en_vermell2 = (temps_actual2 % 3000) >= 0

        for event in pygame.event.get():
            if event.type == QUIT:
                iniciar_transicio()
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if game_over:
                    if event.key in (K_RETURN, K_KP_ENTER):
                        iniciar_transicio()
                        return "REINICIAR"
                if event.key == K_ESCAPE:
                    moment_pausa_inici = pygame.time.get_ticks()
                    return "PAUSAN3.4"
                if event.key == K_e and en_porta:
                    iniciar_transicio()
                    return "JUGANT_NIVELL3_PANTALLA4"
                if event.key == K_e and en_porta2:
                    iniciar_transicio()
                    return "JUGANT_NIVELL3_PANTALLA2"
                if event.key == K_f and not laser_activat:
                    en_estado_robo = not en_estado_robo
                if event.key == K_q and not en_estado_robo:
                    laser_activat = not laser_activat
                if event.key == K_e and en_boto and en_estado_robo:
                    cono4_camara_activat = not cono4_camara_activat

        if not game_over:
            temps_actual = temps_joc()
            temps_actual2 = temps_joc()
            dx = 0
            tecles = pygame.key.get_pressed()
            if tecles[K_a]:
                dx = -5
                mirant_dreta = False
            elif tecles[K_d]:
                dx = 5
                mirant_dreta = True

            jugador_rect.x += dx
            if jugador_rect.x <= LIMIT_ESQUERRA:
                jugador_rect.x = LIMIT_ESQUERRA
            if jugador_rect.right >= LIMIT_DRETA:
                jugador_rect.right = LIMIT_DRETA

            if tecles[K_w] and en_terra:
                vel_y = FORCA_SALT
                en_terra = False
            if jugador_rect.top <= LIMIT_SOSTRE:
                jugador_rect.top = LIMIT_SOSTRE
                vel_y = 0

            vel_y += GRAVETAT
            jugador_rect.y += vel_y
            en_terra = False

            if jugador_rect.y >= ALTURA_SOL:
                jugador_rect.y = ALTURA_SOL
                vel_y = 0
                en_terra = True

            detectat_cam = False
            detectat_cam3 = False
            detectat_cam4 = False

            if cono_camara_activat:
                if jugador_rect.top < (ALTURA_SOL + alcada_jugador) and jugador_rect.bottom > camara_y:
                    distancia_y = jugador_rect.centery - camara_y
                    altura_total = (ALTURA_SOL + alcada_jugador) - camara_y
                    if distancia_y > 0:
                        anchura_actual = (distancia_y / altura_total) * amplada_cono_base
                        limite_izq = camara_x - (anchura_actual / 4)
                        limite_der = camara_x + (anchura_actual / 4)
                        if jugador_rect.right > limite_izq and jugador_rect.left < limite_der:
                            detectat_cam = True

            if cono3_camara_activat:
                if jugador_rect.top < (ALTURA_SOL + alcada_jugador) and jugador_rect.bottom > camara3_y:
                    distancia_y = jugador_rect.centery - camara3_y
                    altura_total = (ALTURA_SOL + alcada_jugador) - camara3_y
                    if distancia_y > 0:
                        anchura_actual = (distancia_y / altura_total) * amplada_cono3_base
                        limite_izq = camara3_x - (anchura_actual / 4)
                        limite_der = camara3_x + (anchura_actual / 4)
                        if jugador_rect.right > limite_izq and jugador_rect.left < limite_der:
                            detectat_cam3 = True

            if cono4_camara_activat:
                if jugador_rect.top < (ALTURA_SOL + alcada_jugador) and jugador_rect.bottom > camara4_y:
                    distancia_y = jugador_rect.centery - camara4_y
                    altura_total = (ALTURA_SOL + alcada_jugador) - camara4_y
                    if distancia_y > 0:
                        anchura_actual = (distancia_y / altura_total) * amplada_cono4_base
                        limite_izq = camara4_x - (anchura_actual / 4)
                        limite_der = camara4_x + (anchura_actual / 4)
                        if jugador_rect.right > limite_izq and jugador_rect.left < limite_der:
                            detectat_cam4 = True

            if (en_vermell and detectat_cam) or (en_vermell and detectat_cam3) or (en_vermell2 and detectat_cam4):
                game_over = True

        PANTALLA.blit(fons_casa, (0, 0))
        PANTALLA.blit(camara_img, camara_rect)
        PANTALLA.blit(camara_img, camara3_rect)
        PANTALLA.blit(camara_img, camara4_rect)
        PANTALLA.blit(boto_img, boto_rect)

        superficie_cono.fill((0, 0, 0, 0))
        superficie_cono3.fill((0, 0, 0, 0))
        superficie_cono4.fill((0, 0, 0, 0))

        if cono_camara_activat:
            if en_vermell:
                color_cono = (255, 0, 0, 100) if game_over or detectat_cam else (255, 0, 0, 70)
                color_cono3 = (255, 0, 0, 100) if game_over or detectat_cam3 else (255, 0, 0, 70)
            else:
                color_cono = (0, 255, 0, 70)
                color_cono3 = (0, 255, 0, 70)

            punts_cono = [
                (camara_x, camara_y - 5),
                (camara_x - amplada_cono_base/4, ALTURA_SOL + alcada_jugador),
                (camara_x + amplada_cono_base/4, ALTURA_SOL + alcada_jugador)
            ]
            punts_cono3 = [
                (camara3_x, camara3_y - 5),
                (camara3_x - amplada_cono3_base/4, ALTURA_SOL + alcada_jugador),
                (camara3_x + amplada_cono3_base/4, ALTURA_SOL + alcada_jugador)
            ]
            pygame.draw.polygon(superficie_cono, color_cono, punts_cono)
            PANTALLA.blit(superficie_cono, (0, 0))
            pygame.draw.polygon(superficie_cono3, color_cono3, punts_cono3)
            PANTALLA.blit(superficie_cono3, (0, 0))

        if cono4_camara_activat:
            if en_vermell2:
                color_cono4 = (255, 0, 0, 100) if game_over or detectat_cam4 else (255, 0, 0, 70)
            else:
                color_cono4 = (0, 255, 0, 70)
            punts_cono4 = [
                (camara4_x, camara4_y - 5),
                (camara4_x - amplada_cono4_base/4, ALTURA_SOL + alcada_jugador),
                (camara4_x + amplada_cono4_base/4, ALTURA_SOL + alcada_jugador)
            ]
            pygame.draw.polygon(superficie_cono4, color_cono4, punts_cono4)
            PANTALLA.blit(superficie_cono4, (0, 0))

        if laser_activat:
            clau_frame_actual = obtenir_clau_frame_jugador(tecles[K_a] or tecles[K_d], en_terra)
            punt_ma_laser = punt_origen_laser(jugador_rect, mirant_dreta, clau_frame_actual)
            pos_mousse = pygame.mouse.get_pos()
            pos_final_laser = pos_mousse
            min_dist_sq = (pos_mousse[0] - punt_ma_laser[0])**2 + (pos_mousse[1] - punt_ma_laser[1])**2
            rect_terra = pygame.Rect(0, ALTURA_SOL + alcada_jugador, 2000, 500)
            rect_sostre = pygame.Rect(0, -500, 2000, 500 + LIMIT_SOSTRE)
            rect_esquerra = pygame.Rect(-500, 0, 500 + LIMIT_ESQUERRA, 2000)
            rect_dreta = pygame.Rect(LIMIT_DRETA, 0, 500, 2000)
            obstacles_laser = [rect_terra, rect_sostre, rect_esquerra, rect_dreta]

            for obs in obstacles_laser:
                interseccions = obs.clipline(punt_ma_laser, pos_mousse)
                if interseccions:
                    for pt in interseccions:
                        dist_sq = (pt[0] - punt_ma_laser[0])**2 + (pt[1] - punt_ma_laser[1])**2
                        if dist_sq < min_dist_sq:
                            min_dist_sq = dist_sq
                            pos_final_laser = pt
            pygame.draw.line(PANTALLA, (255, 0, 0), punt_ma_laser, pos_final_laser, 3)

        if en_boto and not game_over:
            if en_estado_robo:
                mostrar_text("E", font_petita, NEGRE, boto_rect.centerx, boto_rect.top - 20)
            else:
                mostrar_text("Necesitaes cambi de mans", font_mes_petita, VERMELL, boto_rect.centerx + 50, boto_rect.top - 40)

        if en_porta:
            mostrar_text("E", font_petita, NEGRE, PORTA_SORTIDA.centerx, PORTA_SORTIDA.top - 20)
        if en_porta2 and not game_over:
            mostrar_text("E", font_petita, NEGRE, PORTA_SORTIDA2.centerx, PORTA_SORTIDA2.top - 20)

        if en_estado_robo:
            imatges_jugador_actuals = jugador_estado_dreta if mirant_dreta else jugador_estado_esquerra
        else:
            imatges_jugador_actuals = jugador_img_dreta if mirant_dreta else jugador_img_esquerra

        caminant = tecles[K_a] or tecles[K_d]
        PANTALLA.blit(obtenir_frame_jugador(imatges_jugador_actuals, caminant, en_terra), jugador_rect)

        if game_over:
            mostrar_text("GAME  OVER", font_gran, VERMELL, AMPLADA // 2, ALCADA // 2 - 20)
            mostrar_text("Prem  ENTER  per  reiniciar", font_petita, BLANC, AMPLADA // 2, ALCADA // 2 + 40)

        actualitzar_pantalla_amb_transicio()

def nivell3_pantalla4(reiniciar=False, pos_x_inici=50):
    global jugador_rect, mirant_dreta, vel_y, en_terra, textos_vistos, tresors_recollits, moment_pausa_inici, temps_pausa_acumulat

    if moment_pausa_inici is not None:
        temps_pausa_acumulat += pygame.time.get_ticks() - moment_pausa_inici
        moment_pausa_inici = None

    jugant = True
    game_over = False
    amplada_jugador, alcada_jugador = 40, 80

    jugador_img_dreta, jugador_img_esquerra = carregar_animacio_jugador(
        "Alex_quiet.png", "Alex_frame1.png", "Alex_frame2.png", "Alex_salt.png",
        amplada_jugador, alcada_jugador
    )

    jugador_estado_dreta, jugador_estado_esquerra = carregar_animacio_jugador(
        "Alex_estado_quiet.png", "Alex_estado_frame1.png", "Alex_estado_frame2.png", "Alex_estado_salt.png",
        amplada_jugador, alcada_jugador
    )

    amplada_mur = img_repisa.get_width()
    alcada_mur = img_repisa.get_height()

    rect_tresor = nivell3_clau2.get_rect(topleft=(230, 370))

    if reiniciar or jugador_rect is None:
        jugador_rect = jugador_img_dreta["quiet"].get_rect(topleft=(pos_x_inici, 444))
        if pos_x_inici > 400:
            mirant_dreta = False
        else:
            mirant_dreta = True
        vel_y = 0
        en_terra = True

    GRAVETAT = 0.8
    FORCA_SALT = -14
    ALTURA_SOL = 390
    LIMIT_SOSTRE = 0
    LIMIT_ESQUERRA = 20
    LIMIT_DRETA = 870

    PORTA_SORTIDA = pygame.Rect(700, 390, 50, 50)
    PORTA_SORTIDA2 = pygame.Rect(0, 333, 50, 100)

    murs = [
        pygame.Rect(200, 390, amplada_mur, alcada_mur),
    ]

    en_estado_robo = False
    laser_activat = False

    while jugant:
        clock.tick(60)

        en_porta = jugador_rect.colliderect(PORTA_SORTIDA)
        en_porta2 = jugador_rect.colliderect(PORTA_SORTIDA2)

        if not tresors_recollits["nivell3_clau2"]:
            if jugador_rect.colliderect(rect_tresor):
                tresors_recollits["nivell3_clau2"] = True
                if so_recollit:
                    so_recollit.set_volume(volum_sfx)
                    so_recollit.play()

        for event in pygame.event.get():
            if event.type == QUIT:
                iniciar_transicio()
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if game_over:
                    if event.key in (K_RETURN, K_KP_ENTER):
                        iniciar_transicio()
                        tresors_recollits["nivell3_clau2"] = False
                        return "REINICIAR"

                if event.key == K_ESCAPE:
                    moment_pausa_inici = pygame.time.get_ticks()
                    return "PAUSAN3.4"

                if event.key == K_e and en_porta and tresors_recollits["nivell3_clau2"]:
                    iniciar_transicio()
                    return "CREDITS"

                if event.key == K_e and en_porta2:
                    iniciar_transicio()
                    return "JUGANT_NIVELL3_PANTALLA3"

                if event.key == K_f and not laser_activat:
                    en_estado_robo = not en_estado_robo

                if event.key == K_q and not en_estado_robo:
                    laser_activat = not laser_activat

        if not game_over:
            dx = 0
            tecles = pygame.key.get_pressed()

            if tecles[K_a]:
                dx = -5
                mirant_dreta = False
            elif tecles[K_d]:
                dx = 5
                mirant_dreta = True

            jugador_rect.x += dx

            if jugador_rect.x <= LIMIT_ESQUERRA:
                jugador_rect.x = LIMIT_ESQUERRA
            if jugador_rect.right >= LIMIT_DRETA:
                jugador_rect.right = LIMIT_DRETA

            for mur in murs:
                if jugador_rect.colliderect(mur):
                    if dx > 0:
                        jugador_rect.right = mur.left
                    elif dx < 0:
                        jugador_rect.left = mur.right

            if tecles[K_w] and en_terra:
                vel_y = FORCA_SALT
                en_terra = False

            if jugador_rect.top <= LIMIT_SOSTRE:
                jugador_rect.top = LIMIT_SOSTRE
                vel_y = 0

            vel_y += GRAVETAT
            jugador_rect.y += vel_y
            en_terra = False

            if jugador_rect.y >= ALTURA_SOL:
                jugador_rect.y = ALTURA_SOL
                vel_y = 0
                en_terra = True

            for mur in murs:
                if jugador_rect.colliderect(mur):
                    if vel_y > 0:
                        jugador_rect.bottom = mur.top
                        vel_y = 0
                        en_terra = True
                    elif vel_y < 0:
                        jugador_rect.top = mur.bottom
                        vel_y = 0

        PANTALLA.blit(fons_casa2, (0, 0))

        for mur in murs:
            PANTALLA.blit(img_repisa, (mur.x, mur.y))

        if not tresors_recollits["nivell3_clau2"]:
            PANTALLA.blit(nivell3_clau2, rect_tresor)

        if laser_activat:
            clau_frame_actual = obtenir_clau_frame_jugador(tecles[K_a] or tecles[K_d], en_terra)
            punt_ma_laser = punt_origen_laser(jugador_rect, mirant_dreta, clau_frame_actual)
            pos_mousse = pygame.mouse.get_pos()
            pos_final_laser = pos_mousse
            min_dist_sq = (pos_mousse[0] - punt_ma_laser[0])**2 + (pos_mousse[1] - punt_ma_laser[1])**2

            rect_terra = pygame.Rect(0, ALTURA_SOL + alcada_jugador, 2000, 500)
            rect_sostre = pygame.Rect(0, -500, 2000, 500 + LIMIT_SOSTRE)
            rect_esquerra = pygame.Rect(-500, 0, 500 + LIMIT_ESQUERRA, 2000)
            rect_dreta = pygame.Rect(LIMIT_DRETA, 0, 500, 2000)
            obstacles_laser = [rect_terra, rect_sostre, rect_esquerra, rect_dreta]

            for obs in obstacles_laser:
                interseccions = obs.clipline(punt_ma_laser, pos_mousse)
                if interseccions:
                    for pt in interseccions:
                        dist_sq = (pt[0] - punt_ma_laser[0])**2 + (pt[1] - punt_ma_laser[1])**2
                        if dist_sq < min_dist_sq:
                            min_dist_sq = dist_sq
                            pos_final_laser = pt

            pygame.draw.line(PANTALLA, (255, 0, 0), punt_ma_laser, pos_final_laser, 3)

        if en_porta:
            if tresors_recollits["nivell3_clau2"]:
                mostrar_text("E", font_petita, NEGRE, PORTA_SORTIDA.centerx, PORTA_SORTIDA.top - 20)
            else:
                mostrar_text("Falta clau", font_petita, VERMELL, PORTA_SORTIDA.centerx - 100, PORTA_SORTIDA.top)

        if en_porta2 and not game_over:
            mostrar_text("E", font_petita, NEGRE, PORTA_SORTIDA2.centerx, PORTA_SORTIDA2.top - 20)

        if en_estado_robo:
            imatges_jugador_actuals = jugador_estado_dreta if mirant_dreta else jugador_estado_esquerra
        else:
            imatges_jugador_actuals = jugador_img_dreta if mirant_dreta else jugador_img_esquerra

        caminant = tecles[K_a] or tecles[K_d]
        PANTALLA.blit(obtenir_frame_jugador(imatges_jugador_actuals, caminant, en_terra), jugador_rect)

        if game_over:
            mostrar_text("GAME  OVER", font_gran, VERMELL, AMPLADA // 2, ALCADA // 2 - 20)
            mostrar_text("Prem  ENTER  per  reiniciar", font_petita, BLANC, AMPLADA // 2, ALCADA // 2 + 40)

        actualitzar_pantalla_amb_transicio()

def pantalla_credits():
    en_credits = True

    missatges = [
        "P . R . A . I . L .",
        "PROGRAMACIÓ: Marc Pérez Carvajal",
        "GRÀFICS: Marc Pérez Carvajal amb LibreSprite",
        "SO:                      ",
        "   MÚSICA: looplicator i Romariogrande",
        "   SFX: MATUSTRM",
        "Prem Enter per tornar al menú"
    ]

    textos_mostrats = ["" for _ in missatges]
    indexos = [0 for _ in missatges]
    linia_actual = 0

    velocitat_text = 40
    ultim_temps_text = pygame.time.get_ticks()

    while en_credits:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == QUIT:
                iniciar_transicio()
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key in (K_RETURN, K_KP_ENTER):
                    iniciar_transicio()
                    return "INICI"

        temps_actual = pygame.time.get_ticks()
        if linia_actual < len(missatges):
            if temps_actual - ultim_temps_text > velocitat_text:
                if indexos[linia_actual] < len(missatges[linia_actual]):
                    textos_mostrats[linia_actual] += missatges[linia_actual][indexos[linia_actual]]
                    indexos[linia_actual] += 1
                    ultim_temps_text = temps_actual
                else:
                    linia_actual += 1
                    ultim_temps_text = temps_actual + 300

        PANTALLA.fill(NEGRE)

        y_inicial = (ALCADA // 2) - ((len(missatges) * 50) // 2)

        for i in range(len(missatges)):
            if i == 0:
                mostrar_text(textos_mostrats[i], font_gran, BLANC, AMPLADA // 2, y_inicial + i * 50)
            elif i == len(missatges) - 1:
                if linia_actual == len(missatges):
                    mostrar_text(textos_mostrats[i], font_petita, VERMELL, AMPLADA // 2, y_inicial + i * 50 + 20)
            else:
                mostrar_text(textos_mostrats[i], font_petita, CIBER_BLAU, AMPLADA // 2, y_inicial + i * 50)

        actualitzar_pantalla_amb_transicio()

estat = "INICI"
nivell_escollit = None
estat_previ_pausa = "PAUSA"
estat_ajustaments_actual = "AJUSTAMENTS2"
posicio_spawn_x = 100
reiniciar_tutorial = False
reiniciar_nivell1 = False
reiniciar_nivell2 = False
reiniciar_nivell3 = False

tresors_recollits = {
    "tutorial2_copa": False,
    "nivell1_quadre": False,
    "nivell1_quadre2": False,
    "nivell1_quadre3": False,
    "nivell1_quadre4": False,
    "nivell2_clau": False,
    "nivell2_or": False,
    "nivell2_or2": False,
    "nivell2_or3": False,
    "nivell2_or4": False,
    "nivell3_gerro": False,
    "nivell3_diamant": False,
    "nivell3_clau2": False,
}

textos_vistos = {
    "tutorial": False,
    "tutorial2": False,
    "tutorial3": False,
    "tutorial4": False,
    "tutorial5": False
}

nivells_completats = {
    "nivell1": False,
    "nivell2": False
}

while True:
    if estat == "INICI":
        pygame.mouse.set_visible(False)
        canviar_musica("inici.mp3")
        jugador_rect = None
        opcio = pantalla_inici()
        if opcio == "SELECCIÓ NIVELLS":
            estat = "NIVELLS"
        elif opcio == "AJUSTAMENTS":
            estat = "AJUSTAMENTS2"
            estat_ajustaments_actual = "AJUSTAMENTS2"

    elif estat == "NIVELLS":
        pygame.mouse.set_visible(False)
        canviar_musica("inici.mp3")
        jugador_rect = None
        opcio = pantalla_nivells()
        if opcio == "TORNAR":
            estat = "INICI"
        elif opcio == "TUTORIAL":
            iniciar_transicio()
            estat = "JUGANT_TUTORIAL"
            reiniciar_tutorial = True
            posicio_spawn_x = 100
            tresors_recollits["tutorial2_copa"] = False
        elif opcio == "NIVELL1":
            iniciar_transicio()
            estat = "JUGANT_NIVELL1_PANTALLA1"
            reiniciar_nivell1 = True
            posicio_spawn_x = 100
            tresors_recollits["nivell1_quadre"] = False
            tresors_recollits["nivell1_quadre2"] = False
            tresors_recollits["nivell1_quadre3"] = False
            tresors_recollits["nivell1_quadre4"] = False
        elif opcio == "NIVELL2":
            iniciar_transicio()
            estat = "JUGANT_NIVELL2_PANTALLA1"
            reiniciar_nivell2 = True
            posicio_spawn_x = 100
            tresors_recollits["nivell2_clau"] = False
            tresors_recollits["nivell2_or"] = False
            tresors_recollits["nivell2_or2"] = False
            tresors_recollits["nivell2_or3"] = False
            tresors_recollits["nivell2_or4"] = False
        elif opcio == "NIVELL3":
            iniciar_transicio()
            estat = "JUGANT_NIVELL3_PANTALLA1"
            reiniciar_nivell3 = True
            posicio_spawn_x = 100
            tresors_recollits["nivell3_gerro"] = False
            tresors_recollits["nivell3_diamant"] = False
            tresors_recollits["nivell3_clau2"] = False

    elif estat == "JUGANT_TUTORIAL":
        pygame.mouse.set_visible(True)
        opcio = nivell_tutorial(reiniciar=reiniciar_tutorial, pos_x_inici=posicio_spawn_x)
        reiniciar_tutorial = False
        if opcio == "TORNAR":
            estat = "NIVELLS"
        elif opcio == "PAUSAT":
            iniciar_transicio()
            estat = "PAUSAT"
        elif opcio == "JUGANT_TUTORIAL2":
            estat = "JUGANT_TUTORIAL2"
            reiniciar_tutorial = True
            posicio_spawn_x = 50

    elif estat == "JUGANT_TUTORIAL2":
        pygame.mouse.set_visible(True)
        opcio = nivell_tutorial2(reiniciar=reiniciar_tutorial, pos_x_inici=posicio_spawn_x)
        reiniciar_tutorial = False
        if opcio == "PAUSAT2":
            iniciar_transicio()
            estat = "PAUSAT2"
        elif opcio == "JUGANT_TUTORIAL":
            estat = "JUGANT_TUTORIAL"
            reiniciar_tutorial = True
            posicio_spawn_x = 800
        elif opcio == "JUGANT_TUTORIAL3":
            estat = "JUGANT_TUTORIAL3"
            reiniciar_tutorial = True
            posicio_spawn_x = 50

    elif estat == "JUGANT_TUTORIAL3":
        pygame.mouse.set_visible(True)
        opcio = nivell_tutorial3(reiniciar=reiniciar_tutorial, pos_x_inici=posicio_spawn_x)
        reiniciar_tutorial = False
        if opcio == "REINICIAR":
            estat = "JUGANT_TUTORIAL3"
            reiniciar_tutorial = True
            posicio_spawn_x = 50
        if opcio == "PAUSAT3":
            iniciar_transicio()
            estat = "PAUSAT3"
        elif opcio == "JUGANT_TUTORIAL2":
            estat = "JUGANT_TUTORIAL2"
            reiniciar_tutorial = True
            posicio_spawn_x = 800
        elif opcio == "JUGANT_TUTORIAL4":
            estat = "JUGANT_TUTORIAL4"
            reiniciar_tutorial = True
            posicio_spawn_x = 50

    elif estat == "JUGANT_TUTORIAL4":
        pygame.mouse.set_visible(True)
        opcio = nivell_tutorial4(reiniciar=reiniciar_tutorial, pos_x_inici=posicio_spawn_x)
        reiniciar_tutorial = False
        if opcio == "REINICIAR":
            estat = "JUGANT_TUTORIAL4"
            reiniciar_tutorial = True
            posicio_spawn_x = 50
        if opcio == "PAUSAT4":
            iniciar_transicio()
            estat = "PAUSAT4"
        elif opcio == "JUGANT_TUTORIAL3":
            estat = "JUGANT_TUTORIAL3"
            reiniciar_tutorial = True
            posicio_spawn_x = 800
        elif opcio == "JUGANT_TUTORIAL5":
            estat = "JUGANT_TUTORIAL5"
            reiniciar_tutorial = True
            posicio_spawn_x = 50

    elif estat == "JUGANT_TUTORIAL5":
        pygame.mouse.set_visible(True)
        opcio = nivell_tutorial5(reiniciar=reiniciar_tutorial, pos_x_inici=posicio_spawn_x)
        reiniciar_tutorial = False
        if opcio == "REINICIAR":
            estat = "JUGANT_TUTORIAL5"
            reiniciar_tutorial = True
            posicio_spawn_x = 50
        if opcio == "PAUSAT5" or opcio == "PAUSAT":
            iniciar_transicio()
            estat = "PAUSAT5"
        elif opcio == "JUGANT_TUTORIAL4":
            estat = "JUGANT_TUTORIAL4"
            reiniciar_tutorial = True
            posicio_spawn_x = 800
        elif opcio == "JUGANT_TUTORIAL_FINAL":
            estat = "JUGANT_TUTORIAL_FINAL"
            reiniciar_tutorial = True
            posicio_spawn_x = 50

    elif estat == "JUGANT_TUTORIAL_FINAL":
        pygame.mouse.set_visible(False)
        estat = "NIVELLS"

    elif estat == "JUGANT_NIVELL1_PANTALLA1":
        pygame.mouse.set_visible(True)
        opcio = nivell1_pantalla1(reiniciar=reiniciar_nivell1, pos_x_inici=posicio_spawn_x)
        reiniciar_nivell1 = False
        if opcio == "TORNAR":
            estat = "NIVELLS"
        if opcio == "REINICIAR":
            estat = "JUGANT_NIVELL1_PANTALLA1"
            reiniciar_nivell1 = True
            posicio_spawn_x = 50
        elif opcio == "PAUSAN1.1":
            iniciar_transicio()
            estat = "PAUSAN1.1"
        elif opcio == "JUGANT_NIVELL1_PANTALLA2":
            estat = "JUGANT_NIVELL1_PANTALLA2"
            reiniciar_nivell1 = True
            posicio_spawn_x = 50

    elif estat == "JUGANT_NIVELL1_PANTALLA2":
        pygame.mouse.set_visible(True)
        opcio = nivell1_pantalla2(reiniciar=reiniciar_nivell1, pos_x_inici=posicio_spawn_x)
        reiniciar_nivell1 = False
        if opcio == "REINICIAR":
            estat = "JUGANT_NIVELL1_PANTALLA2"
            reiniciar_nivell1 = True
            posicio_spawn_x = 50
        if opcio == "PAUSAN1.2":
            iniciar_transicio()
            estat = "PAUSAN1.2"
        elif opcio == "JUGANT_NIVELL1_PANTALLA1":
            estat = "JUGANT_NIVELL1_PANTALLA1"
            reiniciar_nivell1 = True
            posicio_spawn_x = 800
        elif opcio == "JUGANT_NIVELL1_PANTALLA3":
            estat = "JUGANT_NIVELL1_PANTALLA3"
            reiniciar_nivell1 = True
            posicio_spawn_x = 50

    elif estat == "JUGANT_NIVELL1_PANTALLA3":
        pygame.mouse.set_visible(True)
        opcio = nivell1_pantalla3(reiniciar=reiniciar_nivell1, pos_x_inici=posicio_spawn_x)
        reiniciar_nivell1 = False
        if opcio == "REINICIAR":
            estat = "JUGANT_NIVELL1_PANTALLA3"
            reiniciar_nivell1 = True
            posicio_spawn_x = 50
        if opcio == "PAUSAN1.3":
            iniciar_transicio()
            estat = "PAUSAN1.3"
        elif opcio == "JUGANT_NIVELL1_PANTALLA2":
            estat = "JUGANT_NIVELL1_PANTALLA2"
            reiniciar_nivell1 = True
            posicio_spawn_x = 800
        elif opcio == "JUGANT_NIVELL1_PANTALLA4":
            estat = "JUGANT_NIVELL1_PANTALLA4"
            reiniciar_nivell1 = True
            posicio_spawn_x = 50

    elif estat == "JUGANT_NIVELL1_PANTALLA4":
        pygame.mouse.set_visible(True)
        opcio = nivell1_pantalla4(reiniciar=reiniciar_nivell1, pos_x_inici=posicio_spawn_x)
        reiniciar_nivell1 = False
        if opcio == "REINICIAR":
            estat = "JUGANT_NIVELL1_PANTALLA4"
            reiniciar_nivell1 = True
            posicio_spawn_x = 50
        if opcio == "PAUSAN1.4":
            iniciar_transicio()
            estat = "PAUSAN1.4"
        elif opcio == "JUGANT_NIVELL1_PANTALLA3":
            estat = "JUGANT_NIVELL1_PANTALLA3"
            reiniciar_nivell1 = True
            posicio_spawn_x = 800
        elif opcio == "JUGANT_NIVELL1_FINAL":
            estat = "JUGANT_NIVELL1_FINAL"
            reiniciar_nivell1 = True
            posicio_spawn_x = 50

    elif estat == "JUGANT_NIVELL1_FINAL":
        pygame.mouse.set_visible(False)
        estat = "NIVELLS"

    elif estat == "JUGANT_NIVELL2_PANTALLA1":
        pygame.mouse.set_visible(True)
        opcio = nivell2_pantalla1(reiniciar=reiniciar_nivell2, pos_x_inici=posicio_spawn_x)
        reiniciar_nivell2 = False
        if opcio == "TORNAR":
            estat = "NIVELLS"
        if opcio == "REINICIAR":
            estat = "JUGANT_NIVELL2_PANTALLA1"
            reiniciar_nivell2 = True
            posicio_spawn_x = 50
        elif opcio == "PAUSAN2.1":
            iniciar_transicio()
            estat = "PAUSAN2.1"
        elif opcio == "JUGANT_NIVELL2_PANTALLA2":
            estat = "JUGANT_NIVELL2_PANTALLA2"
            reiniciar_nivell2 = True
            posicio_spawn_x = 50

    elif estat == "JUGANT_NIVELL2_PANTALLA2":
        pygame.mouse.set_visible(True)
        opcio = nivell2_pantalla2(reiniciar=reiniciar_nivell2, pos_x_inici=posicio_spawn_x)
        reiniciar_nivell2 = False
        if opcio == "REINICIAR":
            estat = "JUGANT_NIVELL2_PANTALLA2"
            reiniciar_nivell2 = True
            posicio_spawn_x = 50
        if opcio == "PAUSAN2.2":
            iniciar_transicio()
            estat = "PAUSAN2.2"
        elif opcio == "JUGANT_NIVELL2_PANTALLA1":
            estat = "JUGANT_NIVELL2_PANTALLA1"
            reiniciar_nivell2 = True
            posicio_spawn_x = 800
        elif opcio == "JUGANT_NIVELL2_PANTALLA3":
            estat = "JUGANT_NIVELL2_PANTALLA3"
            reiniciar_nivell2 = True
            posicio_spawn_x = 50

    elif estat == "JUGANT_NIVELL2_PANTALLA3":
        pygame.mouse.set_visible(True)
        opcio = nivell2_pantalla3(reiniciar=reiniciar_nivell2, pos_x_inici=posicio_spawn_x)
        reiniciar_nivell2 = False
        if opcio == "REINICIAR":
            estat = "JUGANT_NIVELL2_PANTALLA3"
            reiniciar_nivell2 = True
            posicio_spawn_x = 50
        if opcio == "PAUSAN2.3":
            iniciar_transicio()
            estat = "PAUSAN2.3"
        elif opcio == "JUGANT_NIVELL2_PANTALLA2":
            estat = "JUGANT_NIVELL2_PANTALLA2"
            reiniciar_nivell2 = True
            posicio_spawn_x = 800
        elif opcio == "JUGANT_NIVELL2_PANTALLA4":
            estat = "JUGANT_NIVELL2_PANTALLA4"
            reiniciar_nivell2 = True
            posicio_spawn_x = 50

    elif estat == "JUGANT_NIVELL2_PANTALLA4":
        pygame.mouse.set_visible(True)
        opcio = nivell2_pantalla4(reiniciar=reiniciar_nivell2, pos_x_inici=posicio_spawn_x)
        reiniciar_nivell2 = False
        if opcio == "REINICIAR":
            estat = "JUGANT_NIVELL2_PANTALLA4"
            reiniciar_nivell2 = True
            posicio_spawn_x = 50
        if opcio == "PAUSAN2.4":
            iniciar_transicio()
            estat = "PAUSAN2.4"
        elif opcio == "JUGANT_NIVELL2_PANTALLA3":
            estat = "JUGANT_NIVELL2_PANTALLA3"
            reiniciar_nivell2 = True
            posicio_spawn_x = 800
        elif opcio == "JUGANT_NIVELL2_FINAL":
            estat = "JUGANT_NIVELL2_FINAL"
            reiniciar_nivell2 = True
            posicio_spawn_x = 50

    elif estat == "JUGANT_NIVELL2_FINAL":
        pygame.mouse.set_visible(False)
        estat = "NIVELLS"

    elif estat == "JUGANT_NIVELL3_PANTALLA1":
        pygame.mouse.set_visible(True)
        opcio = nivell3_pantalla1(reiniciar=reiniciar_nivell3, pos_x_inici=posicio_spawn_x)
        reiniciar_nivell3 = False
        if opcio == "TORNAR":
            estat = "NIVELLS"
        if opcio == "REINICIAR":
            estat = "JUGANT_NIVELL3_PANTALLA1"
            reiniciar_nivell3 = True
            posicio_spawn_x = 50
        elif opcio == "PAUSAN3.1":
            iniciar_transicio()
            estat = "PAUSAN3.1"
        elif opcio == "JUGANT_NIVELL3_PANTALLA2":
            estat = "JUGANT_NIVELL3_PANTALLA2"
            reiniciar_nivell3 = True
            posicio_spawn_x = 50

    elif estat == "JUGANT_NIVELL3_PANTALLA2":
        pygame.mouse.set_visible(True)
        opcio = nivell3_pantalla2(reiniciar=reiniciar_nivell3, pos_x_inici=posicio_spawn_x)
        reiniciar_nivell3 = False
        if opcio == "REINICIAR":
            estat = "JUGANT_NIVELL3_PANTALLA2"
            reiniciar_nivell3 = True
            posicio_spawn_x = 50
        if opcio == "PAUSAN3.2":
            iniciar_transicio()
            estat = "PAUSAN3.2"
        elif opcio == "JUGANT_NIVELL3_PANTALLA1":
            estat = "JUGANT_NIVELL3_PANTALLA1"
            reiniciar_nivell3 = True
            posicio_spawn_x = 800
        elif opcio == "JUGANT_NIVELL3_PANTALLA3":
            estat = "JUGANT_NIVELL3_PANTALLA3"
            reiniciar_nivell3 = True
            posicio_spawn_x = 50

    elif estat == "JUGANT_NIVELL3_PANTALLA3":
        pygame.mouse.set_visible(True)
        opcio = nivell3_pantalla3(reiniciar=reiniciar_nivell3, pos_x_inici=posicio_spawn_x)
        reiniciar_nivell3 = False
        if opcio == "REINICIAR":
            estat = "JUGANT_NIVELL3_PANTALLA3"
            reiniciar_nivell3 = True
            posicio_spawn_x = 50
        if opcio == "PAUSAN3.3":
            iniciar_transicio()
            estat = "PAUSAN3.3"
        elif opcio == "JUGANT_NIVELL3_PANTALLA2":
            estat = "JUGANT_NIVELL3_PANTALLA2"
            reiniciar_nivell3 = True
            posicio_spawn_x = 800
        elif opcio == "JUGANT_NIVELL3_PANTALLA4":
            estat = "JUGANT_NIVELL3_PANTALLA4"
            reiniciar_nivell3 = True
            posicio_spawn_x = 50

    elif estat == "JUGANT_NIVELL3_PANTALLA4":
        pygame.mouse.set_visible(True)
        opcio = nivell3_pantalla4(reiniciar=reiniciar_nivell3, pos_x_inici=posicio_spawn_x)
        reiniciar_nivell3 = False
        if opcio == "REINICIAR":
            estat = "JUGANT_NIVELL3_PANTALLA4"
            reiniciar_nivell3 = True
            posicio_spawn_x = 50
        if opcio == "PAUSAN3.4":
            iniciar_transicio()
            estat = "PAUSAN3.4"
        elif opcio == "JUGANT_NIVELL3_PANTALLA3":
            estat = "JUGANT_NIVELL3_PANTALLA3"
            reiniciar_nivell3 = True
            posicio_spawn_x = 800
        elif opcio == "CREDITS":
            estat = "CREDITS"

    elif estat == "CREDITS":
        estat = pantalla_credits()

    elif estat == "AJUSTAMENTS2":
        pygame.mouse.set_visible(False)
        opcio = pantalla_ajustaments()
        if opcio == "TORNAR":
            estat = "INICI"
        elif opcio == "CONTROLS":
            estat = "CONTROLS2"
        elif opcio == "SO":
            estat = "SO2"
        elif opcio == "PANTALLA":
            estat = "PANTALLA2"

    elif estat == "AJUSTAMENTS3":
        pygame.mouse.set_visible(False)
        opcio = pantalla_ajustaments2()
        if opcio == "TORNAR2" or opcio == "TORNAR":
            estat = estat_previ_pausa
        elif opcio == "CONTROLS":
            estat = "CONTROLS2"
        elif opcio == "SO":
            estat = "SO2"
        elif opcio == "PANTALLA":
            estat = "PANTALLA2"

    elif estat == "CONTROLS2":
        pygame.mouse.set_visible(False)
        opcio = pantalla_controls()
        if opcio == "TORNAR":
            estat = estat_ajustaments_actual

    elif estat == "SO2":
        pygame.mouse.set_visible(True)
        opcio = pantalla_so()
        if opcio == "TORNAR":
            estat = estat_ajustaments_actual

    elif estat == "PANTALLA2":
        pygame.mouse.set_visible(False)
        opcio = pantalla_pantalla()
        if opcio == "TORNAR":
            estat = estat_ajustaments_actual

    elif estat == "JUGANT":
        pygame.mouse.set_visible(False)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        actualitzar_pantalla_amb_transicio()

    elif estat == "PAUSA":
        pygame.mouse.set_visible(False)
        opcio = pantalla_pausa_tutorial()
        if opcio == "JUGANT_TUTORIAL":
            estat = "JUGANT_TUTORIAL"
        elif opcio == "INICI":
            pygame.mixer.music.stop()
            estat = "INICI"
        elif opcio == "AJUSTAMENTS3":
            estat = "AJUSTAMENTS3"
            estat_previ_pausa = "PAUSA"
            estat_ajustaments_actual = "AJUSTAMENTS3"

    elif estat == "PAUSAT":
        pygame.mouse.set_visible(False)
        opcio = pantalla_pausa_tutorial()
        if opcio == "JUGANT_TUTORIAL":
            estat = "JUGANT_TUTORIAL"
        elif opcio == "INICI":
            pygame.mixer.music.stop()
            estat = "INICI"
        elif opcio == "AJUSTAMENTS3":
            estat = "AJUSTAMENTS3"
            estat_previ_pausa = "PAUSAT"
            estat_ajustaments_actual = "AJUSTAMENTS3"

    elif estat == "PAUSAT2":
        pygame.mouse.set_visible(False)
        opcio = pantalla_pausa_tutorial()
        if opcio == "JUGANT_TUTORIAL":
            estat = "JUGANT_TUTORIAL2"
        elif opcio == "INICI":
            pygame.mixer.music.stop()
            estat = "INICI"
        elif opcio == "AJUSTAMENTS3":
            estat = "AJUSTAMENTS3"
            estat_previ_pausa = "PAUSAT2"
            estat_ajustaments_actual = "AJUSTAMENTS3"

    elif estat == "PAUSAT3":
        pygame.mouse.set_visible(False)
        opcio = pantalla_pausa_tutorial()
        if opcio == "JUGANT_TUTORIAL":
            estat = "JUGANT_TUTORIAL3"
        elif opcio == "INICI":
            pygame.mixer.music.stop()
            estat = "INICI"
        elif opcio == "AJUSTAMENTS3":
            estat = "AJUSTAMENTS3"
            estat_previ_pausa = "PAUSAT3"
            estat_ajustaments_actual = "AJUSTAMENTS3"

    elif estat == "PAUSAT4":
        pygame.mouse.set_visible(False)
        opcio = pantalla_pausa_tutorial()
        if opcio == "JUGANT_TUTORIAL":
            estat = "JUGANT_TUTORIAL4"
        elif opcio == "INICI":
            pygame.mixer.music.stop()
            estat = "INICI"
        elif opcio == "AJUSTAMENTS3":
            estat = "AJUSTAMENTS3"
            estat_previ_pausa = "PAUSAT4"
            estat_ajustaments_actual = "AJUSTAMENTS3"

    elif estat == "PAUSAT5":
        pygame.mouse.set_visible(False)
        opcio = pantalla_pausa_tutorial()
        if opcio == "JUGANT_TUTORIAL":
            estat = "JUGANT_TUTORIAL5"
        elif opcio == "INICI":
            pygame.mixer.music.stop()
            estat = "INICI"
        elif opcio == "AJUSTAMENTS3":
            estat = "AJUSTAMENTS3"
            estat_previ_pausa = "PAUSAT5"
            estat_ajustaments_actual = "AJUSTAMENTS3"

    elif estat == "PAUSAN1.1":
        pygame.mouse.set_visible(False)
        opcio = pantalla_pausa_nivell1()
        if opcio == "JUGANT_NIVELL1_PANTALLA1":
            estat = "JUGANT_NIVELL1_PANTALLA1"
        elif opcio == "INICI":
            pygame.mixer.music.stop()
            estat = "INICI"
        elif opcio == "AJUSTAMENTS3":
            estat = "AJUSTAMENTS3"
            estat_previ_pausa = "PAUSAN1.1"
            estat_ajustaments_actual = "AJUSTAMENTS3"

    elif estat == "PAUSAN1.2":
        pygame.mouse.set_visible(False)
        opcio = pantalla_pausa_nivell1()
        if opcio == "JUGANT_NIVELL1_PANTALLA1":
            estat = "JUGANT_NIVELL1_PANTALLA2"
        elif opcio == "INICI":
            pygame.mixer.music.stop()
            estat = "INICI"
        elif opcio == "AJUSTAMENTS3":
            estat = "AJUSTAMENTS3"
            estat_previ_pausa = "PAUSAN1.2"
            estat_ajustaments_actual = "AJUSTAMENTS3"

    elif estat == "PAUSAN1.3":
        pygame.mouse.set_visible(False)
        opcio = pantalla_pausa_nivell1()
        if opcio == "JUGANT_NIVELL1_PANTALLA1":
            estat = "JUGANT_NIVELL1_PANTALLA3"
        elif opcio == "INICI":
            pygame.mixer.music.stop()
            estat = "INICI"
        elif opcio == "AJUSTAMENTS3":
            estat = "AJUSTAMENTS3"
            estat_previ_pausa = "PAUSAN1.3"
            estat_ajustaments_actual = "AJUSTAMENTS3"

    elif estat == "PAUSAN1.4":
        pygame.mouse.set_visible(False)
        opcio = pantalla_pausa_nivell1()
        if opcio == "JUGANT_NIVELL1_PANTALLA1":
            estat = "JUGANT_NIVELL1_PANTALLA4"
        elif opcio == "INICI":
            pygame.mixer.music.stop()
            estat = "INICI"
        elif opcio == "AJUSTAMENTS3":
            estat = "AJUSTAMENTS3"
            estat_previ_pausa = "PAUSAN1.4"
            estat_ajustaments_actual = "AJUSTAMENTS3"

    elif estat == "PAUSAN2.1":
        pygame.mouse.set_visible(False)
        opcio = pantalla_pausa_nivell2()
        if opcio == "JUGANT_NIVELL2_PANTALLA1":
            estat = "JUGANT_NIVELL2_PANTALLA1"
        elif opcio == "INICI":
            pygame.mixer.music.stop()
            estat = "INICI"
        elif opcio == "AJUSTAMENTS3":
            estat = "AJUSTAMENTS3"
            estat_previ_pausa = "PAUSAN2.1"
            estat_ajustaments_actual = "AJUSTAMENTS3"

    elif estat == "PAUSAN2.2":
        pygame.mouse.set_visible(False)
        opcio = pantalla_pausa_nivell2()
        if opcio == "JUGANT_NIVELL2_PANTALLA1":
            estat = "JUGANT_NIVELL2_PANTALLA2"
        elif opcio == "INICI":
            pygame.mixer.music.stop()
            estat = "INICI"
        elif opcio == "AJUSTAMENTS3":
            estat = "AJUSTAMENTS3"
            estat_previ_pausa = "PAUSAN2.2"
            estat_ajustaments_actual = "AJUSTAMENTS3"

    elif estat == "PAUSAN2.3":
        pygame.mouse.set_visible(False)
        opcio = pantalla_pausa_nivell2()
        if opcio == "JUGANT_NIVELL2_PANTALLA1":
            estat = "JUGANT_NIVELL2_PANTALLA3"
        elif opcio == "INICI":
            pygame.mixer.music.stop()
            estat = "INICI"
        elif opcio == "AJUSTAMENTS3":
            estat = "AJUSTAMENTS3"
            estat_previ_pausa = "PAUSAN2.3"
            estat_ajustaments_actual = "AJUSTAMENTS3"

    elif estat == "PAUSAN2.4":
        pygame.mouse.set_visible(False)
        opcio = pantalla_pausa_nivell2()
        if opcio == "JUGANT_NIVELL2_PANTALLA1":
            estat = "JUGANT_NIVELL2_PANTALLA4"
        elif opcio == "INICI":
            pygame.mixer.music.stop()
            estat = "INICI"
        elif opcio == "AJUSTAMENTS3":
            estat = "AJUSTAMENTS3"
            estat_previ_pausa = "PAUSAN2.4"
            estat_ajustaments_actual = "AJUSTAMENTS3"

    elif estat == "PAUSAN3.1":
        pygame.mouse.set_visible(False)
        opcio = pantalla_pausa_nivell3()
        if opcio == "JUGANT_NIVELL3_PANTALLA1":
            estat = "JUGANT_NIVELL3_PANTALLA1"
        elif opcio == "INICI":
            pygame.mixer.music.stop()
            estat = "INICI"
        elif opcio == "AJUSTAMENTS3":
            estat = "AJUSTAMENTS3"
            estat_previ_pausa = "PAUSAN3.1"
            estat_ajustaments_actual = "AJUSTAMENTS3"

    elif estat == "PAUSAN3.2":
        pygame.mouse.set_visible(False)
        opcio = pantalla_pausa_nivell3()
        if opcio == "JUGANT_NIVELL3_PANTALLA1":
            estat = "JUGANT_NIVELL3_PANTALLA2"
        elif opcio == "INICI":
            pygame.mixer.music.stop()
            estat = "INICI"
        elif opcio == "AJUSTAMENTS3":
            estat = "AJUSTAMENTS3"
            estat_previ_pausa = "PAUSAN3.2"
            estat_ajustaments_actual = "AJUSTAMENTS3"

    elif estat == "PAUSAN3.3":
        pygame.mouse.set_visible(False)
        opcio = pantalla_pausa_nivell3()
        if opcio == "JUGANT_NIVELL3_PANTALLA1":
            estat = "JUGANT_NIVELL3_PANTALLA3"
        elif opcio == "INICI":
            pygame.mixer.music.stop()
            estat = "INICI"
        elif opcio == "AJUSTAMENTS3":
            estat = "AJUSTAMENTS3"
            estat_previ_pausa = "PAUSAN3.3"
            estat_ajustaments_actual = "AJUSTAMENTS3"

    elif estat == "PAUSAN3.4":
        pygame.mouse.set_visible(False)
        opcio = pantalla_pausa_nivell3()
        if opcio == "JUGANT_NIVELL3_PANTALLA1":
            estat = "JUGANT_NIVELL3_PANTALLA4"
        elif opcio == "INICI":
            pygame.mixer.music.stop()
            estat = "INICI"
        elif opcio == "AJUSTAMENTS3":
            estat = "AJUSTAMENTS3"
            estat_previ_pausa = "PAUSAN3.4"
            estat_ajustaments_actual = "AJUSTAMENTS3"
