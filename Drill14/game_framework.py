import time
running = False
stack = []


def change_mode(mode):
    if stack:
        stack.pop().finish()
    stack.append(mode)
    mode.init()


def push_mode(mode):
    if stack:
        stack[-1].pause()
    stack.append(mode)
    mode.init()


def pop_mode():
    if stack:
        stack.pop().finish()
    if stack:
        stack[-1].resume()
    else:
        quit()


def quit():
    global running
    running = False

frame_time = 0.0
frame_rate = 0.0


def run(start_mode):
    global running, stack, frame_time, frame_rate
    running = True
    stack = [start_mode]
    frame_time = 0.0
    frame_rate = 0.0
    try:
        start_mode.init()
        current_time = time.time()
        while running and stack:
            stack[-1].handle_events()
            if not running or not stack:
                break
            stack[-1].update()
            if not running or not stack:
                break
            stack[-1].render()
            frame_time = time.time() - current_time
            frame_rate = 1.0 / frame_time if frame_time > 0.0 else 0.0
            current_time += frame_time
            print(f'Frame Time: {frame_time:.6f}, Frame Rate: {frame_rate:.2f}')
    finally:
        while stack:
            stack.pop().finish()
        running = False
