import pygame

# Inicializar o Pygame
pygame.init()

# Definir as dimensões da janela do jogo
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
WINDOW_SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT)

# Definir as cores utilizadas no jogo
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Criar a janela do jogo
window = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Bloco de concreto caindo")

# Definir as propriedades do bloco de concreto
block_width = 50
block_height = 50
block_x = WINDOW_WIDTH / 2 - block_width / 2
block_y = 0
block_speed = 5

# Definir o personagem principal João
joao_width = 50
joao_height = 50
joao_x = WINDOW_WIDTH / 4 - joao_width / 2
joao_y = WINDOW_HEIGHT - joao_height - 50
joao_speed = 5

# Loop principal do jogo
clock = pygame.time.Clock()
running = True

while running:
    # Lidar com eventos do Pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Mover o bloco de concreto para baixo
    block_y += block_speed
    
    # Desenhar o bloco de concreto e o personagem João
    window.fill(BLACK)
    pygame.draw.rect(window, WHITE, [block_x, block_y, block_width, block_height])
    pygame.draw.rect(window, WHITE, [joao_x, joao_y, joao_width, joao_height])
    
    # Atualizar a tela
    pygame.display.update()
    
    # Limitar a taxa de atualização da tela
    clock.tick(60)

# Finalizar o Pygame
pygame.quit()
