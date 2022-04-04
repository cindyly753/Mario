import pygame as pg
from landing_page import LandingPage
from sys import exit
import game_functions as gf
from time import sleep
from stats import Stats
from scoreboard import Scoreboard
from settings import Settings
from sound import Sound


class Game:
    RED = (255, 0, 0)


    def __init__(self):
        pg.init()
        self.settings = Settings()
        self.stats = Stats(game=self)
        self.screen = pg.display.set_mode((self.settings.screen_width,
                                           self.settings.screen_height))
        self.bg_color = self.settings.bg_color
        self.sound = Sound()
        self.sb = Scoreboard(game=self)
        pg.display.set_caption("Umamusume Pretty Derby")
        self.sound.play_bg()
        
    def restart(self):
            pass

    def update(self):
        self.sb.update()

    def draw(self):

        self.screen.fill(self.bg_color)
        background_img = pg.image.load(f'images/Background.jpg').convert()
        self.screen.blit(background_img, (0, 0))
        self.sb.draw()

        pg.display.flip()

    def play(self):
        self.finished = False
        self.sound.play_bg()
        while not self.finished:
            self.update()
            self.draw()
            gf.check_events(game=self)   # exits game if QUIT pressed
        self.game_over()

    def game_over(self):
      self.sound.play_game_over()
      print('\nGAME OVER!\n\n')
      exit()    # can ask to replay here instead of exiting the game

def main():
    g = Game()
    lp = LandingPage(game=g)
    lp.show()
    g.play()


if __name__ == '__main__':
    main()
