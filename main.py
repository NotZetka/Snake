import pygame
import random

WIDTH, HEIGHT = 500, 500

ORANGE = (255, 80, 10)
WHITE = (255, 255, 255)

FPS = 60
velocity = 3
score = 0

APPLE_EATEN = pygame.USEREVENT + 1

SNAKE_HEAD_IMAGE = pygame.transform.scale(pygame.image.load('assets/snakehead.png'),(20,20))
SNAKE_TAIL_IMAGE = pygame.transform.scale(pygame.image.load('assets/snaketail.png'),(20,20))
GOLDEN_APPLE_IMAGE = pygame.transform.scale(pygame.image.load('assets/GoldenApple.png'),(20,20))

STARTX = 250
STARTY = 250

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake by Jakub Kochański')

def draw_window():
    WIN.fill(WHITE)
    WIN.blit(SNAKE_HEAD_IMAGE,(snake.x,snake.y))
    WIN.blit(GOLDEN_APPLE_IMAGE,(apple.x,apple.y))
    pygame.display.update()

def snake_movement(keys_pressed, snake,side):
    if keys_pressed[pygame.K_LEFT] and side != 'RIGHT':
        side = 'LEFT'
    if keys_pressed[pygame.K_RIGHT] and side != 'LEFT':
        side =  'RIGHT'
    if keys_pressed[pygame.K_UP] and side != 'DOWN':
        side = 'UPSIDE'
    if keys_pressed[pygame.K_DOWN] and side != 'UPSIDE':
        side= 'DOWN'

    if side == 'LEFT':
        snake.x -= velocity
    if side == 'RIGHT':
        snake.x += velocity
    if side == 'UPSIDE':
        snake.y -= velocity
    if side == 'DOWN':
        snake.y += velocity
    return side

def check_borders(snake,side):
    if snake.x<0 or snake.x>WIDTH-snake.width or snake.y<0 or snake.y>HEIGHT-snake.height:
        print(f'przegrałęś wynik {score}')
        pygame.time.delay(5000)
        snake.x = STARTX
        snake.y = STARTY
        return 'UPSIDE'
    return side



snake = pygame.Rect(STARTX,STARTY,SNAKE_HEAD_IMAGE.get_width(),SNAKE_HEAD_IMAGE.get_height())
apple = pygame.Rect(random.randrange(500-GOLDEN_APPLE_IMAGE.get_width()),random.randrange(500-GOLDEN_APPLE_IMAGE.get_height()),GOLDEN_APPLE_IMAGE.get_width(),GOLDEN_APPLE_IMAGE.get_height())

def main():
    global velocity
    global score
    side = 'UPSIDE'
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        if snake.colliderect(apple):
            score+=1
            apple.x = random.randrange(500)
            apple.y = random.randrange(500)
            velocity = 3 + score//5


        pygame.time.Clock().tick(FPS)
        keys_pressed=pygame.key.get_pressed()
        side = snake_movement(keys_pressed,snake,side)

        side = check_borders(snake,side)
        draw_window()



main()
pygame.quit()
