import pygame

def affichage_starmap(game_starmap, fenetre, size, pos,scrrec):
    # affichage de la grille hexagonale
    hexa_load = pygame.image.load("Ressources Graphiques\GUI\\40x44px-Hexagon_blue.svg.png").convert_alpha()
    hexa_scale = pygame.transform.scale(hexa_load, (int(scrrec.right / 20), int(scrrec.bottom / 20)))
    taille_hexa = hexa_scale.get_rect()
    i = 0
    while i < size:
        j = 0
        while j < pos[0] + size:
            position_hexa = (j * taille_hexa.right * 0.75, i * taille_hexa.bottom)
            fenetre.blit(hexa_scale, position_hexa)
            j = j + 2

        j = 0
        while j < pos[1] + size:
            position_hexa = (
            j * taille_hexa.right * 0.75 + taille_hexa.right * 0.75, i * taille_hexa.bottom + (taille_hexa.bottom / 2))
            fenetre.blit(hexa_scale, position_hexa)
            j = j + 2
        i = i + 1

    # chargement des ressourrces pour les entities
    #planet_classeM_load = pygame.image.load("Ressources Graphiques\Espaces\planets\planet18_0.png").convert_alpha()
    #planet_classeM_scaled = pygame.transform.scale(planet_classeM_load,(int(taille_hexa.right), int(taille_hexa.bottom)))

    # affichage des entities
    for i in range(pos[0], size - 1):
        for j in range(pos[1], size - 1):
            if len(game_starmap.hexaGrid[i][j].entities) != 0:  # ligne, colonne
                # print(self.hexaGrid[0][0].entities[0].entitie_type)
                if game_starmap.hexaGrid[i][j].entities[0].entitie_type == "planet":

                    if j % 2 == 0:
                        position_planet = (j * taille_hexa.right * 0.75, i * taille_hexa.bottom)
                    else:  # si la colonne est impaire, l'affichage est décalé pour corespondre à l'hexagone
                        position_planet = (
                        j * taille_hexa.right * 0.75, i * taille_hexa.bottom + 0.5 * taille_hexa.bottom)

                    # chargement des ressourrces pour les entities
                    planet_classeM_load = pygame.image.load("Ressources Graphiques\Espace\planets\{0}.png".format(game_starmap.hexaGrid[i][j].entities[0].appearence)).convert_alpha()
                    planet_classeM_scaled = pygame.transform.scale(planet_classeM_load,(int(0.9*taille_hexa.right), int(taille_hexa.bottom)))

                    fenetre.blit(planet_classeM_scaled, position_planet)
                    # print("PLANETE AFFICHEE")
