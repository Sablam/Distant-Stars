import pygame
import Graphic.visible_starmap
import Graphic.gui


def affichage(game_starmap, fenetre, size, pos):
    scrrec = fenetre.get_rect()

    #affichage du background
    fenetre.fill(0)
    etoile = pygame.image.load("Ressources Graphiques\Espace\Stars-Nebulae\Stars.png").convert_alpha()
    etoile1 = pygame.transform.scale(etoile, (scrrec.right, scrrec.bottom))
    position_fond = (0, 0)
    fenetre.blit(etoile1, position_fond)

    nebula1_load = pygame.image.load("Ressources Graphiques\\Espace\\Stars-Nebulae\\Nebula1.png").convert_alpha()
    nebula1_scale = pygame.transform.scale(nebula1_load, (scrrec.right, scrrec.bottom))
    position_fond = (0, 0)
    fenetre.blit(nebula1_scale, position_fond)

    nebula2_load = pygame.image.load("Ressources Graphiques\\Espace\\Stars-Nebulae\\Nebula2.png").convert_alpha()
    nebula2_scale = pygame.transform.scale(nebula2_load, (scrrec.right, scrrec.bottom))
    position_fond = (0, 0)
    fenetre.blit(nebula2_scale, position_fond)

    Graphic.visible_starmap.affichage_starmap(game_starmap, fenetre, size, pos, scrrec)#affiche la grille hexagonal et les entitées visibles
    Graphic.gui.affichage_gui(fenetre, scrrec)#affiche l'interface utilisateur


    pygame.display.flip()