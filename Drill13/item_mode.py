from pico2d import *
from sdl2 import SDLK_0, SDLK_1, SDLK_2, SDLK_i
import game_framework
import game_world
import play_mode

image = None


def init():
    global image
    image = load_image('item_select.png')


def finish():
    global image
    image = None


def handle_events():
    choices = {SDLK_0: 0, SDLK_1: 1, SDLK_2: 2}
    for event in get_events():
        if event.type == SDL_QUIT:
            game_framework.quit()
            return
        if event.type == SDL_KEYDOWN:
            if event.key in choices:
                play_mode.boy.ball_type = choices[event.key]
                game_framework.pop_mode()
                return
            if event.key in (SDLK_ESCAPE, SDLK_i):
                game_framework.pop_mode()
                return


def update():
    pass


def render():
    clear_canvas()
    game_world.render()
    image.draw(400, 300)
    update_canvas()


def pause(): pass

def resume(): pass
