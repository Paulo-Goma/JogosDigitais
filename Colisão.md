import pygame

BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)

pygame.init()

screen = pygame.display.set_mode((640, 480))

pygame.display.set_caption('Collision')

# cria o Rect para o quadrado
square = pygame.Rect(300, 230, 20, 20)

# cria o Rect para os pads
left_pad = pygame.Rect(20, 210, 20, 60)
right_pad = pygame.Rect(600, 210, 20, 60)

pads = [left_pad, right_pad]

velocity_x = 0.1

clock = pygame.time.Clock()

while True:
    dt = clock.tick(30)

    event = pygame.event.poll()

    if event.type == pygame.QUIT:
        break

    # usa a função move inplace
    square.move_ip(velocity_x * dt, 0)

    # checa por colisão com os pads
    if square.collidelist(pads) >= 0:
        velocity_x = -velocity_x

    screen.fill(BLACK)

    # desenha o quadrado usando o Rect
    pygame.draw.rect(screen, WHITE, square)

    # desenha os pads
    for pad in pads:
        pygame.draw.rect(screen, WHITE, pad)

    pygame.display.flip()
