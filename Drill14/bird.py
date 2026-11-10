from pico2d import load_image, get_canvas_width
import game_framework

PIXEL_PER_METER = 10.0 / 0.3
FLIGHT_SPEED_KMPH = 20.0
FLIGHT_SPEED_PPS = FLIGHT_SPEED_KMPH * 1000.0 / 3600.0 * PIXEL_PER_METER
FRAME_COUNT = 14
SHEET_COLUMNS = 5
SHEET_ROWS = 3
FLAP_CYCLES_PER_SECOND = 2.0
FRAMES_PER_SECOND = FRAME_COUNT * FLAP_CYCLES_PER_SECOND
DRAW_WIDTH = 92
DRAW_HEIGHT = 84


class Bird:
    image = None

    def __init__(self, x, y, direction=1, phase=0.0, speed=FLIGHT_SPEED_PPS):
        if Bird.image is None:
            Bird.image = load_image('bird_animation.png')
        self.x, self.y = x, y
        self.direction = direction
        self.frame = phase % FRAME_COUNT
        self.speed = speed

    def update(self):
        dt = game_framework.frame_time
        self.frame = (self.frame + FRAMES_PER_SECOND * dt) % FRAME_COUNT
        # Reflect the travelled distance, including multiple turns in a long frame.
        left = DRAW_WIDTH / 2
        right = get_canvas_width() - DRAW_WIDTH / 2
        span = right - left
        travel = self.x - left
        if self.direction < 0:
            travel = 2 * span - travel
        travel = (travel + self.speed * dt) % (2 * span)
        if travel < span:
            self.x = left + travel
            self.direction = 1
        else:
            self.x = left + 2 * span - travel
            self.direction = -1

    def clip_rect(self):
        # Read left-to-right, top-to-bottom; the last cell is empty.
        row, column = divmod(int(self.frame), SHEET_COLUMNS)
        x0 = round(column * self.image.w / SHEET_COLUMNS)
        x1 = round((column + 1) * self.image.w / SHEET_COLUMNS)
        top = round(row * self.image.h / SHEET_ROWS)
        bottom = round((row + 1) * self.image.h / SHEET_ROWS)
        return x0, self.image.h - bottom, x1 - x0, bottom - top

    def draw(self):
        flip = 'h' if self.direction < 0 else ''
        self.image.clip_composite_draw(
            *self.clip_rect(), 0, flip, self.x, self.y, DRAW_WIDTH, DRAW_HEIGHT)
