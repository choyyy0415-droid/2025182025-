from pico2d import *
from sdl2 import SDLK_p, SDLK_i
import game_framework
import game_world
from boy import Boy
from grass import Grass

boy = None
paused_at = 0.0


def init():
    global boy
    game_world.clear()
    game_world.add_oject(Grass(), 0)
    boy = Boy()
    game_world.add_oject(boy, 1)


def finish():
    global boy
    game_world.clear()
    boy = None


def handle_events():
    for event in get_events():
        if event.type == SDL_QUIT:
            game_framework.quit()
            return
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                import title_mode
                game_framework.change_mode(title_mode)
                return
            if event.key == SDLK_i:
                import item_mode
                game_framework.push_mode(item_mode)
                return
            if event.key == SDLK_p:
                import pause_mode
                game_framework.push_mode(pause_mode)
                return
        boy.handle_event(event)


def update():
    game_world.update()


def render():
    clear_canvas()
    game_world.render()
    update_canvas()


def pause():
    global paused_at
    paused_at = get_time()
    if boy is not None:
        boy.pressed_keys.clear()
        boy.dir = 0
        if boy.state == 'RUN':
            boy.stop_run()

def resume():
    if boy is not None:
        boy.idle_started_at += get_time() - paused_at
