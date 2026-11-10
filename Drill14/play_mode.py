from pico2d import *
import game_world
import game_framework
from boy import Boy
from grass import Grass
from bird import Bird, FLIGHT_SPEED_PPS, FRAME_COUNT

boy = None
birds = []


def handle_events():


    event_list = get_events()
    for event in event_list:
        if event.type == SDL_QUIT:
            game_framework.quit()
            return
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            boy.handle_event(event)


def init():
    global boy, birds
    game_world.clear()

    boy = Boy()
    game_world.add_oject(boy)

    grass = Grass()
    game_world.add_oject(grass, 0)

    # Add the flock alongside the existing character and background.
    birds = [Bird(120 + i * 140, 160 + i * 40,
                  direction=1 if i % 2 == 0 else -1,
                  phase=i * FRAME_COUNT / 10,
                  speed=FLIGHT_SPEED_PPS * (1.0 + i * 0.025))
             for i in range(10)]
    for bird in birds:
        game_world.add_oject(bird, 1)


def pause():
    boy.pause()


def resume():
    pass


def finish():
    global boy, birds
    game_world.clear()
    boy = None
    birds = []
    Bird.image = None


def update():
    game_world.update()
    # Lecture 16, page 25: simulate a slow frame.
    delay(0.1)

def render():
    clear_canvas()
    game_world.render()
    update_canvas()









