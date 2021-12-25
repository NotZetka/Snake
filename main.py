import pygame
import random

WIDTH, HEIGHT = 500, 500

ORANGE = (255, 80, 10)
WHITE = (255, 255, 255)
BLACK = (0,0,0)

FPS = 10
velocity = 20
score = 0
run = True

APPLE_EATEN = pygame.USEREVENT + 1

SNAKE_HEAD_IMAGE_DEFAULT = pygame.transform.scale(pygame.image.load('assets/snakehead.png'),(20,20))
SNAKE_HEAD_IMAGE = SNAKE_HEAD_IMAGE_DEFAULT
SNAKE_TAIL_IMAGE = pygame.transform.scale(pygame.image.load('assets/snaketail.png'),(20,20))
GOLDEN_APPLE_IMAGE = pygame.transform.scale(pygame.image.load('assets/GoldenApple.png'),(20,20))

STARTX = 250
STARTY = 250

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake by Jakub Kochański')

def draw_window(tail):
    WIN.fill(BLACK)
    for part in tail:
        WIN.blit(SNAKE_TAIL_IMAGE,(part.x,part.y))
    WIN.blit(SNAKE_HEAD_IMAGE,(snake.x,snake.y))
    WIN.blit(GOLDEN_APPLE_IMAGE,(apple.x,apple.y))
    pygame.display.update()

def snake_movement(keys_pressed, snake,side):
    global SNAKE_HEAD_IMAGE
    if keys_pressed[pygame.K_LEFT] and side != 'RIGHT':
        side = 'LEFT'
        SNAKE_HEAD_IMAGE = pygame.transform.rotate(SNAKE_HEAD_IMAGE_DEFAULT,90)
    if keys_pressed[pygame.K_RIGHT] and side != 'LEFT':
        side =  'RIGHT'
        SNAKE_HEAD_IMAGE = pygame.transform.rotate(SNAKE_HEAD_IMAGE_DEFAULT, 270)
    if keys_pressed[pygame.K_UP] and side != 'DOWN':
        side = 'UPSIDE'
        SNAKE_HEAD_IMAGE = SNAKE_HEAD_IMAGE_DEFAULT
    if keys_pressed[pygame.K_DOWN] and side != 'UPSIDE':
        side= 'DOWN'
        SNAKE_HEAD_IMAGE = pygame.transform.rotate(SNAKE_HEAD_IMAGE_DEFAULT, 180)

    if side == 'LEFT':
        snake.x -= velocity
    if side == 'RIGHT':
        snake.x += velocity
    if side == 'UPSIDE':
        snake.y -= velocity
    if side == 'DOWN':
        snake.y += velocity
    return side

def tail_movement(tail,snake):
    for i in range(1,len(tail)):
        tail[-i].x=tail[-i-1].x
        tail[-i].y=tail[-i-1].y
    if len(tail)>0:
        tail[0].x=snake.x
        tail[0].y=snake.y

def check_borders(snake):
    if snake.x<0 or snake.x>WIDTH-snake.width or snake.y<0 or snake.y>HEIGHT-snake.height:
        lose_game()

    return True

def lose_game():
    pygame.font.init()
    text = pygame.font.SysFont('comicsans', 20)
    text = text.render(f'wynik {score}',1,WHITE)
    WIN.blit(text,(WIDTH/2 - text.get_width() /2, HEIGHT/2 - text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(3000)
    pygame.quit()



snake = pygame.Rect(STARTX,STARTY,SNAKE_HEAD_IMAGE.get_width(),SNAKE_HEAD_IMAGE.get_height())
apple = pygame.Rect(random.randrange(500-GOLDEN_APPLE_IMAGE.get_width()),random.randrange(500-GOLDEN_APPLE_IMAGE.get_height()),GOLDEN_APPLE_IMAGE.get_width(),GOLDEN_APPLE_IMAGE.get_height())

def main():
    tail = []
    global velocity
    global score
    side = 'UPSIDE'
    global run
    while run:
        if len(tail) == 0:
            x=snake.x
            y=snake.y
        else:
            x=tail[-1].x
            y=tail[-1].y
        keys_pressed=pygame.key.get_pressed()
        tail_movement(tail, snake)
        side = snake_movement(keys_pressed,snake,side)
        if snake.colliderect(apple):
            print(apple)
            score+=1
            apple.x = random.randrange(500-GOLDEN_APPLE_IMAGE.get_width())
            apple.y = random.randrange(500-GOLDEN_APPLE_IMAGE.get_height())
            tail.append(pygame.Rect(x,y,20,20))
            print(snake)
            print(tail)


        pygame.time.Clock().tick(FPS)
        draw_window(tail)
        check_borders(snake)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False

        for i in range(len(tail)-1):
            if snake.colliderect(tail[i+1]):
                lose_game()
                run = False


main()
