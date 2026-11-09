import os
from pathlib import Path
from pico2d import open_canvas, close_canvas
import game_framework
import logo_mode


def main():
    previous_directory = Path.cwd()
    os.chdir(Path(__file__).resolve().parent)
    try:
        open_canvas()
        try:
            game_framework.run(logo_mode)
        finally:
            close_canvas()
    finally:
        os.chdir(previous_directory)


if __name__ == '__main__':
    main()
