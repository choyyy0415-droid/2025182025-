from pico2d import *
import game_framework
import game_world
from bird import Bird, FLIGHT_SPEED_PPS, FRAME_COUNT
from grass import Grass

birds = []


def init():
    global birds
    game_world.clear()
    game_world.add_oject(Grass(), 0)
    birds = [Bird(120 + i * 140, 120 + i * 44,
                  direction=1 if i % 2 == 0 else -1,
                  phase=i * FRAME_COUNT / 10,
                  speed=FLIGHT_SPEED_PPS * (1.0 + i * 0.025))
             for i in range(10)]
    for bird in birds:
        game_world.add_oject(bird, 1)


def finish():
    global birds
    game_world.clear()
    birds = []
    Bird.image = None


def handle_events():
    for event in get_events():
        if event.type == SDL_QUIT or (event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE):
            game_framework.quit()
            return


def update():
    game_world.update()


def render():
    clear_canvas()
    game_world.render()
    update_canvas()


def pause(): pass

def resume(): pass
