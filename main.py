import pygame
import time
import random

# Initialisation de Pygame
pygame.init()

# Dimensions de l'écran
largeur_ecran = 800
hauteur_ecran = 600

# Couleurs
blanc = (255, 255, 255)
noir = (0, 0, 0)
rouge = (255, 0, 0)

# Taille des blocs et vitesse
taille_bloc = 20
vitesse = 20

# Configuration de la fenêtre de jeu
ecran = pygame.display.set_mode((largeur_ecran, hauteur_ecran))
pygame.display.set_caption("Snake")

horloge = pygame.time.Clock()

# Fonction principale du jeu
def jeu_snake():
    game_over = False
    game_quit = False

    # Position initiale du serpent
    x_serpent = largeur_ecran / 2
    y_serpent = hauteur_ecran / 2

    # Déplacement initial du serpent
    deplacement_x = 0
    deplacement_y = 0

    # Liste pour stocker les parties du serpent
    serpent_parties = []
    longueur_serpent = 1

    # Position aléatoire de la pomme
    x_pomme = round(random.randrange(0, largeur_ecran - taille_bloc) / 20.0) * 20.0
    y_pomme = round(random.randrange(0, hauteur_ecran - taille_bloc) / 20.0) * 20.0

    while not game_quit:
        while game_over:
            ecran.fill(noir)
            message("Game Over! Appuyez sur C pour continuer ou Q pour quitter.", blanc)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_quit = True
                        game_over = False
                    if event.key == pygame.K_c:
                        jeu_snake()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_quit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    deplacement_x = -vitesse
                    deplacement_y = 0
                elif event.key == pygame.K_RIGHT:
                    deplacement_x = vitesse
                    deplacement_y = 0
                elif event.key == pygame.K_UP:
                    deplacement_y = -vitesse
                    deplacement_x = 0
                elif event.key == pygame.K_DOWN:
                    deplacement_y = vitesse
                    deplacement_x = 0

        if x_serpent >= largeur_ecran or x_serpent < 0 or y_serpent >= hauteur_ecran or y_serpent < 0:
            game_over = True

        x_serpent += deplacement_x
        y_serpent += deplacement_y
        ecran.fill(noir)
        pygame.draw.rect(ecran, rouge, [x_pomme, y_pomme, taille_bloc, taille_bloc])
        serpent_tete = []
        serpent_tete.append(x_serpent)
        serpent_tete.append(y_serpent)
        serpent_parties.append(serpent_tete)
        if len(serpent_parties) > longueur_serpent:
            del serpent_parties[0]

        for partie in serpent_parties[:-1]:
            if partie == serpent_tete:
                game_over = True

        for partie in serpent_parties:
            pygame.draw.rect(ecran, blanc, [partie[0], partie[1], taille_bloc, taille_bloc])

        pygame.display.update()

        if x_serpent == x_pomme and y_serpent == y_pomme:
            x_pomme = round(random.randrange(0, largeur_ecran - taille_bloc) / 20.0) * 20.0
            y_pomme = round(random.randrange(0, hauteur_ecran - taille_bloc) / 20.0) * 20.0
            longueur_serpent += 1

        horloge.tick(20)

    pygame.quit()
    quit()

# Fonction pour afficher un message à l'écran
def message(msg, couleur):
    font_style = pygame.font.SysFont(None, 25)
    texte = font_style.render(msg, True, couleur)
    ecran.blit(texte, [largeur_ecran / 6, hauteur_ecran / 3])

# Lancement du jeu
jeu_snake()
