from operator import truediv
import random
from pico2d import *

# Game object class here
class Grass:
    def __init__(self):
        # 생성자 함수 __init__() : 객체의 초기상태를 설정한다
        # 초기 : 모양이 없는 빈 틀, 이 self에 속성들을 부여한다.
        self.image = load_image('grass.png')
    def update(self):
        pass
    def draw(self):
        self.image.draw(400, 30)

class Boy:
    def __init__(self):
        self.x, self.y = random.randint(0, 700), 90
        self.frame = random.randint(0, 7)
        self.image = load_image('run_animation.png')
    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5
    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)

class Ball_s:
    def __init__(self):
        self.x, self.y = random.randint(50, 800), 599
        self.dy = random.randint(3, 10)
        self.image = load_image('ball21x21.png')
    def update(self):
        if (self.y > 30 + 31):
            self.y -= self.dy
        else:
            self.y = 30 + 31
    def draw(self):
        self.image.clip_draw(0, 0, 21, 21, self.x, self.y)

class Ball_l:
    def __init__(self):
        self.x, self.y = random.randint(50, 800), 599
        self.dy = random.randint(3, 10)
        self.image = load_image('ball41x41.png')
    def update(self):
        if(self.y > 30 + 41):
            self.y -= self.dy
        else:
            self.y = 30 + 41
    def draw(self):
        self.image.clip_draw(0, 0, 41, 41, self.x, self.y)

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

def reset_world():
    global running
    global grass
    global team
    global world

    global ball_s
    global ball_l

    running = True
    world = []

    grass = Grass() # 잔디생성 -> 클래스가 호출되면, 클래스의 생성자를 찾는다
    world.append(grass)

    team = [Boy() for i in range(11)]
    world += team

    ball_s = [Ball_s() for i in range(10)]
    world += ball_s
    ball_l = [Ball_l() for i in range(10)]
    world += ball_l

running = True

def update_world():
    # grass.update() # 객체의 상태를 업데이트(시뮬레이션)
    # for boy in team:
    #     boy.update()
    for o in world:
        o.update()
    pass

def render_world():
    clear_canvas()
    # grass.draw()
    # for boy in team:
    #     boy.draw()
    for o in world:
        o.draw()
    update_canvas()

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
