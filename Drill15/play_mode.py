from pico2d import *
import game_world
import game_framework
from boy import Boy
from grass import Grass
from ball import Ball
from zombie import Zombie

boy = None


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
    global boy

    boy = Boy()
    game_world.add_oject(boy)

    grass = Grass()
    game_world.add_oject(grass, 0)
    game_world.add_objects([Zombie() for _ in range(5)])


def pause():
    boy.pause()


def resume():
    pass


def finish():
    global boy
    game_world.clear()
    boy = None


def update():
    game_world.update()
    objects = game_world.world[1]
    zombies = [obj for obj in objects if isinstance(obj, Zombie)]
    balls = [obj for obj in objects if isinstance(obj, Ball) and not obj.stopped]

    for ball in balls:
        for zombie in zombies[:]:
            if game_world.collide(ball, zombie):
                game_world.remove_object(ball)
                if zombie.take_hit():
                    game_world.remove_object(zombie)
                    zombies.remove(zombie)
                break

    if any(game_world.collide(boy, zombie) for zombie in zombies):
        game_framework.quit()


def render():
    clear_canvas()
    game_world.render()
    update_canvas()









