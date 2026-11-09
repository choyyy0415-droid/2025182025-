from pico2d import *
from sdl2 import SDLK_p
import game_framework

image = None


def init():
    global image
    image = load_image('pause.png')


def finish():
    global image
    image = None


def handle_events():
    for event in get_events():
        if event.type == SDL_QUIT:
            game_framework.quit()
            return
        if event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.pop_mode()
            return


def update(): pass


def render():
    clear_canvas()
    image.draw(400, 300, 800, 600)
    update_canvas()


def pause(): pass

def resume(): pass
