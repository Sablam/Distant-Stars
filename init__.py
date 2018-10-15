import pygame
import graphic.window

from entities import Starmap

from pygame.locals import *


def main():
    pygame.init()
    pygame.display.set_caption("Distant Stars")
    fenetre = pygame.display.set_mode((1450, 950))
    info = pygame.display.Info()
    print(info)

    game_starmap = Starmap.Starmap_obj(20, 20)
    graphic.window.affichage_starmap(game_starmap, fenetre)


    running = 1
    while running:
        for event in pygame.event.get():

            if event.type == QUIT:
                running = 0

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = 0

            #if event.type == VIDEORESIZE:

                # etoile = pygame.transform.scale(etoile1, (event.w, event.h))
                #
                # nebula1_scale = pygame.transform.scale(nebula1_load, (event.w, event.h))
                #
                # nebula2_scale = pygame.transform.scale(nebula2_load, (event.w, event.h))
                #
                # hexa_scale = pygame.transform.scale(hexa_load, (event.w, event.h))
                #
                # fenetre = pygame.display.set_mode((event.w, event.h), RESIZABLE)
                #
                #
                # fenetre.blit(etoile, position_fond)
                # fenetre.blit(nebula1_scale, position_fond)
                # fenetre.blit(nebula2_scale, position_fond)
                # fenetre.blit(hexa_scale, position_fond)

            #if event.type == MOUSEMOTION:
                #print(event.pos[0], event.pos[1])



        pygame.display.flip()

    pygame.quit()

if __name__ == '__main__':
    main()