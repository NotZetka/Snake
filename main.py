import pygame

WIDTH, HEIGHT = 500, 500

ORANGE = (255, 80, 10)
WHITE = (255, 255, 255)

FPS = 60
VELOCITY = 3

SNAKE_HEAD_IMAGE = pygame.transform.scale(pygame.image.load('assets/snakehead.png'),(20,20))
SNAKE_TAIL_IMAGE = pygame.transform.scale(pygame.image.load('assets/snaketail.png'),(20,20))
GOLDEN_APPLE_IMAGE = pygame.transform.scale(pygame.image.load('assets/GoldenApple.png'),(20,20))

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake by Jakub Kochański')

def draw_window():
    WIN.fill(WHITE)
    WIN.blit(SNAKE_HEAD_IMAGE,(snake.x,snake.y))
    WIN.blit(GOLDEN_APPLE_IMAGE,(300,300))
    pygame.display.update()

def snake_movement(keys_pressed, snake):
    if keys_pressed[pygame.K_LEFT]:
        snake.x -= VELOCITY
    if keys_pressed[pygame.K_RIGHT]:
        snake.x += VELOCITY
    if keys_pressed[pygame.K_UP]:
        snake.y -= VELOCITY
    if keys_pressed[pygame.K_DOWN]:
        snake.y += VELOCITY


snake = pygame.Rect(240,240,SNAKE_HEAD_IMAGE.get_width(),SNAKE_HEAD_IMAGE.get_height())


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.time.Clock().tick(FPS)
    keys_pressed=pygame.key.get_pressed()
    snake_movement(keys_pressed,snake)


    draw_window()


pygame.quit()
