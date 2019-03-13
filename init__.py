import pygame
import graphic.Window
from Core import GameSession



from pygame.locals import *


#test

def main():
    pygame.init()
    pygame.display.set_caption("Distant Stars")
    fenetre = pygame.display.set_mode((1450, 950))
    info = pygame.display.Info()
    print(info)

    scrrec = fenetre.get_rect()
    img_menu=pygame.transform.scale(pygame.image.load("Ressources Graphiques/menu.png"),(scrrec.right, scrrec.bottom))
    fenetre.blit(img_menu,(0,0))
    pygame.display.flip()

    pygame.mixer.music.load("Musics/271866__mrpork__era-of-space.ogg")
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play()



    flag_game_started = 0




    running = 1
    while running:
        for event in pygame.event.get():

            if event.type == QUIT:
                running = 0

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = 0

            if event.type == MOUSEBUTTONDOWN:
                if flag_game_started == 0:
                    if (0.45*scrrec.bottom < pygame.mouse.get_pos()[1] < 0.55*scrrec.bottom) and (0.40*scrrec.right < pygame.mouse.get_pos()[0] < 0.60*scrrec.right):
                        flag_game_started = 1
                        gamesession = GameSession.GameSession(fenetre)


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