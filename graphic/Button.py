import pygame
import Core.Config

class button:

    def __init__(self, img_button, coords, surface, text_file, text_label):
        self.rect_button = img_button.get_rect()
        self.rect_button.topleft = coords
        surface.blit(img_button, coords)


        myfont = pygame.font.Font('Text/NEUROPOL.TTF', 40)
        textsurface = myfont.render(text_file[Core.Config.language][0][text_label], False, (0, 100, 200))
        surface.blit(textsurface, (coords[0] + ((img_button.get_width() - textsurface.get_width()) / 2), coords[1] + ((img_button.get_height() - textsurface.get_height()) / 2)))

