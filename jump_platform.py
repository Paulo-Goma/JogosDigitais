import pygame
from pygame.locals import *

pygame.init()

clock = pygame.time.Clock()
fps = 60

screen_width = 900
screen_height = 650

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Earthbreak Scape')

# Define a pasta que contém as imagens
img_dir = "img/"

# Define as variáveis do jogo
tile_size = 50

# Carrega as imagens
predios = pygame.image.load('background.png').convert()
chao_preto= pygame.image.load('chao_preto.jpg').convert()
chao_branco = pygame.image.load('chão.jpg').convert()

def draw_grid():
    for line in range(0,20):
         pygame.draw.line(screen, (255,255,255), (0,line*tile_size), (screen_width, line*tile_size))
         pygame.draw.line(screen,(255,255,255), (line* tile_size, 0), (line*tile_size, screen_height))

class Player():
    def __init__(self, x, y):
        img = pygame.image.load('timmy.png')
        self.image = pygame.transform.scale(img,(40,80))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.vel_y = 0
        self.jumped = False
    def update(self):
        dx = 0
        dy = 0

        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE] and self.jumped == False:
            self.vel_y = -15
            self.jumped = True
        if key[pygame.K_SPACE] == False:
            self.jumped = False
        if key[pygame.K_LEFT]:
            dx -= 2
        if key[pygame.K_RIGHT]:
            dx += 2

        self.vel_y += 1
        if self.vel_y > 10:
            self.vel_y = 10
        dy += self.vel_y 
 
        for tile in world.tile_list:
            if tile[1].colliderect(self.rect.x + dx, self.rect.y + dy, self.width, self.height):
                dx = 0

            if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                # ve se está no chão quando pula
                if self.vel_y < 0:
                    dy = tile[1].bottom - self.rect.top
                    self.vel_y = 0
                # ve se acima está no chão quando pula
                elif self.vel_y >= 0:
                    dy = tile[1].top - self.rect.bottom
                    self.vel_y = 0

        self.rect.x += dx
        self.rect.y += dy

        if self.rect.bottom > screen_height:
            self.rect.bottom = screen_height
            dy = 0

        screen.blit(self.image, self.rect)
        pygame.draw.rect(screen, (255, 255, 255), self.rect, 2)

class World():
    def __init__(self, data):
        self.tile_list = []
        
        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                if tile == 1:
                    img = pygame.transform.scale(chao_preto, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size            
                    img_rect.y = row_count * tile_size
                    self.tile_list.append((img, img_rect))
                if tile == 2:
                    img = pygame.transform.scale(chao_branco, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size            
                    img_rect.y = row_count * tile_size
                    self.tile_list.append((img, img_rect))
                if tile ==3:
                    inimigo = Enemy(col_count * tile_size, row_count * tile_size + 15)
                    inimigo_grupo.add(inimigo)
                col_count += 1
            row_count += 1

    def  draw(self):
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])
            pygame.draw.rect(screen, (255,255,255), tile[1], 2)

class Enemy(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('inimigo.png').convert()
        self.image = pygame.transform.scale(self.image, (45, 40))  # Reduce the size of the enemy image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_direction = 1
        self.move_counter = 0
    
    def update(self):
        self.rect.x += self.move_direction
        self.move_counter += 1
        if self.move_counter > 50:
            self.move_direction *= -1
            self.move_counter = 0


world_data = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 3, 0, 3, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 1],
    [1, 0, 0, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
]
inimigo_grupo  = pygame.sprite.Group()

player = Player(100, screen_height - 130) 
world = World(world_data)


run = True
while run:
    clock.tick(fps)
    screen.blit(predios, (0, 0))

    world.draw()

    inimigo_grupo.update()
    inimigo_grupo.draw(screen)
    
    player.update()

    draw_grid()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
    

pygame.quit()
