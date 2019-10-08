import pygame
import json
import tkinter as tk
import Graphic.window
from Core import game_session
from Graphic.button import button



from pygame.locals import *




def main():

    root = tk.Tk()
    screen_width = 800#root.winfo_screenwidth()
    screen_height = 500#root.winfo_screenheight()

    pygame.init()
    pygame.display.set_caption("Distant Stars")
    fenetre = pygame.display.set_mode((screen_width, screen_height))

    pygame.font.init()
    info = pygame.display.Info()
    print(info)
    global language


    with open("Text/Menu.json", "r") as file_Menu:
        menu_text = json.load(file_Menu)

    scrrec = fenetre.get_rect()
    img_menu=pygame.transform.scale(pygame.image.load("Ressources Graphiques/Menu/menu.png"),(scrrec.right, scrrec.bottom))
    fenetre.blit(img_menu,(0,0))
    img_button = pygame.image.load("Ressources Graphiques/Menu/button_menu.png")
    button_start=button(img_button,(scrrec.right*0.38,scrrec.bottom*0.3),fenetre,menu_text,"menu_newgame")
    button_config = button(img_button, (scrrec.right * 0.38, scrrec.bottom * 0.5), fenetre, menu_text, "menu_config")
    button_quit = button(img_button, (scrrec.right * 0.38, scrrec.bottom * 0.7), fenetre, menu_text, "menu_quit")

    pygame.display.flip()

    pygame.mixer.music.load("Musics/John_Bartmann_-_12_-_Interstellar_Space.mp3")
    pygame.mixer.music.set_volume(0.1)
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
                mouse = pygame.mouse.get_pos()
                if flag_game_started == 0:

                    if button_start.rect_button.collidepoint(mouse):
                        flag_game_started = 1
                        gamesession = game_session.GameSession(fenetre)

                    if button_config.rect_button.collidepoint(mouse):
                        running = 1 #TODO

                    if button_quit.rect_button.collidepoint(mouse):
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