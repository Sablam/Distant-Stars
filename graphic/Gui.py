import pygame

def affichage_gui(fenetre,scrrec):
    fond=pygame.image.load("Ressources Graphiques/GUI/Chunk6.png").convert_alpha()
    fond_transformed = pygame.transform.scale(fond, (int(scrrec.right/4), scrrec.bottom))
    position_fond = (int(scrrec.right-0.25*int(scrrec.right )), 0)
    fenetre.blit(fond_transformed, position_fond)

    deco_up = pygame.image.load("Ressources Graphiques/GUI/Machine 3.png").convert_alpha()
    deco_up_transformed = pygame.transform.scale(deco_up, (int(scrrec.right / 7), int(scrrec.right / 7)))
    position_deco_up = (int(scrrec.right - 1.85 * int(scrrec.right / 10)), int(0))
    fenetre.blit(deco_up_transformed, position_deco_up)

    deco_down = pygame.image.load("Ressources Graphiques/GUI/Machine 2.png").convert_alpha()
    deco_down_transformed = pygame.transform.scale(deco_down, (int(scrrec.right / 7), int(scrrec.right / 7)))
    position_deco_down = (int(scrrec.right - 1.95 * int(scrrec.right / 10)), int(0.8*scrrec.bottom))
    fenetre.blit(deco_down_transformed, position_deco_down)

    radar = pygame.image.load("Ressources Graphiques/GUI/Radar.png").convert_alpha()
    radar_transformed = pygame.transform.scale(radar, (int(scrrec.right / 5), int(scrrec.right / 5)))
    position_radar = (int(scrrec.right - 2.2 * int(scrrec.right / 10)), int(0 + 0.06 * scrrec.bottom))
    fenetre.blit(radar_transformed, position_radar)

