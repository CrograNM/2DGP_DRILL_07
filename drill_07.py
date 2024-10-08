
from pico2d import *

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


def reset_world():
    pass
running = True

def update_world():
    pass
def render_world():
    pass

open_canvas()

# initialization code
reset_world()

# game main loop code
while running :
    handle_events()
    update_world() # 상호작용 시뮬레이션
    render_world() # 결과 출력(Draw)
    delay(0.05)

# finalization code

close_canvas()