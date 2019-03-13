import pygame

def affichage_gui(fenetre,scrrec):
    fond=pygame.image.load("Ressources Graphiques/GUI/BOFHtileAndObjects/console1.png").convert_alpha()
    fond_transformed = pygame.transform.scale(fond, (int(scrrec.right/4), scrrec.bottom))
    position_fond = (int(scrrec.right-2.5*int(scrrec.right / 10)), 0)
    fenetre.blit(fond_transformed, position_fond)

    radar = pygame.image.load("Ressources Graphiques/GUI/Radar.png").convert_alpha()
    radar_transformed = pygame.transform.scale(radar, (int(scrrec.right / 5), int(scrrec.right / 5)))
    position_radar = (int(scrrec.right - 2.3 * int(scrrec.right / 10)), int(0+0.06*scrrec.bottom))
    fenetre.blit(radar_transformed, position_radar)

