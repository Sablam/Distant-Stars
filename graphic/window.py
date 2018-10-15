import pygame


def affichage_starmap(game_starmap, fenetre):
    scrrec = fenetre.get_rect()

    etoile = pygame.image.load("Ressources Graphiques\Espaces\Stars-Nebulae\Stars.png").convert_alpha()
    etoile1 = pygame.transform.scale(etoile, (scrrec.right, scrrec.bottom))
    position_fond = (0, 0)
    fenetre.blit(etoile1, position_fond)

    nebula1_load = pygame.image.load("Ressources Graphiques\\Espaces\\Stars-Nebulae\\Nebula1.png").convert_alpha()
    nebula1_scale = pygame.transform.scale(nebula1_load, (scrrec.right, scrrec.bottom))
    position_fond = (0, 0)
    fenetre.blit(nebula1_scale, position_fond)

    nebula2_load = pygame.image.load("Ressources Graphiques\\Espaces\\Stars-Nebulae\\Nebula2.png").convert_alpha()
    nebula2_scale = pygame.transform.scale(nebula2_load, (scrrec.right, scrrec.bottom))
    position_fond = (0, 0)
    fenetre.blit(nebula2_scale, position_fond)

    hexa_load = pygame.image.load("Ressources Graphiques\\GUI\\40x44px-Hexagon_blue.svg.png").convert_alpha()
    # hexa_scale = pygame.transform.scale(hexa_load, (int(scrrec.right/40), int(scrrec.bottom/20)))
    taille_hexa = hexa_load.get_rect()
    i = 0
    while i < game_starmap.size[1]:
        y = 0
        while y < game_starmap.size[0]:
            position_hexa = (y * taille_hexa.right * 0.75, i * taille_hexa.bottom)
            fenetre.blit(hexa_load, position_hexa)
            y = y + 2

        y = 0
        while y < game_starmap.size[0]:
            position_hexa = (
            y * taille_hexa.right * 0.75 + taille_hexa.right * 0.75, i * taille_hexa.bottom + (taille_hexa.bottom / 2))
            fenetre.blit(hexa_load, position_hexa)
            y = y + 2
        i = i + 1

    for i in range(0, game_starmap.size[0] - 1):
        for j in range(0, game_starmap.size[1] - 1):
            if len(game_starmap.hexaGrid[i][j].entities) != 0:
                # print(self.hexaGrid[0][0].entities[0].entitie_type)
                if game_starmap.hexaGrid[i][j].entities[0].entitie_type == "planet":
                    planet_classeM_load = pygame.image.load(
                        "Ressources Graphiques\Espaces\planets\planet18_0.png").convert_alpha()
                    planet_classeM_scaled = pygame.transform.scale(planet_classeM_load, (
                    int(taille_hexa.right * 0.75), int(taille_hexa.bottom * 0.75)))
                    position_planet = (j * taille_hexa.right * 0.75 + taille_hexa.right * 0.75 / 2,
                                       i * taille_hexa.bottom + taille_hexa.bottom / 2)
                    fenetre.blit(planet_classeM_scaled, position_planet)
                    print("PLANETE AFFICHEE")

    pygame.display.flip()