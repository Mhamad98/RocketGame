import pygame
import os
import sys
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Rocket Game')

# Set up the clock for a decent frame rate
clock = pygame.time.Clock()
fps = 60

# Load images
rocket_img = pygame.image.load('rocket.png')
background_img = pygame.image.load('space.jpg')
asteroid_img = pygame.image.load('asteroid.png')
bullet_img = pygame.image.load('bullet.png')


 
class Rocket(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(rocket_img, (50, 70))
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 50)
        self.speed = 5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.x += self.speed
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.bottom < SCREEN_HEIGHT:
            self.rect.y += self.speed

 
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.transform.scale(bullet_img, (10, 20))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 10

    def update(self):
        self.rect.y -= self.speed
        if self.rect.bottom < 0:
            self.kill()

 
class Asteroid(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(asteroid_img, (40, 40))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randint(-100, -40)
        self.speed = random.randint(1, 5)

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()

 
rocket = Rocket()

 
all_sprites = pygame.sprite.Group()
all_sprites.add(rocket)

 
bullets = pygame.sprite.Group()

 
asteroids = pygame.sprite.Group()

 
score = 0
font = pygame.font.SysFont("arial", 25)

def show_score():
    score_text = font.render("Score: " + str(score), True, WHITE)
    screen.blit(score_text, (10, 10))

 
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet = Bullet(rocket.rect.centerx, rocket.rect.top)
                all_sprites.add(bullet)
                bullets.add(bullet)

    
    all_sprites.update()

  
    if random.random() < 0.02:
        asteroid = Asteroid()
        all_sprites.add(asteroid)
        asteroids.add(asteroid)

   
    hits = pygame.sprite.groupcollide(asteroids, bullets, True, True)
    if hits:
         
        score += 1

 
    screen.blit(background_img, (0, 0))
    all_sprites.draw(screen)
    show_score()
    pygame.display.flip()

 
    clock.tick(fps)

pygame.quit()
sys.exit()
     