import random
import pygame
import sys

score = 0

pygame.init()
Running = True

Screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

ammus_color = (255, 0, 0)

player_img = pygame.image.load('pelaaja.png')
player_updated = pygame.transform.scale(player_img, (200, 200))

enemy_list = []
otokka_img = pygame.image.load('otokka.png')
otokka_updated = pygame.transform.scale(otokka_img, (200, 200))
SPAWNENEMY = pygame.USEREVENT
pygame.time.set_timer(SPAWNENEMY, 1000)

# Määritellään pelaajan elämäpisteiden fontti
font = pygame.font.Font(None, 36)

class Player:
    def __init__(self):
        self.ypos = 540
        self.xpos = 325
        self.height = 60
        self.width = 60
        self.playerUpdated = player_updated
        self.health = 100

    def create_player(self):
        self.Playerss = pygame.Rect(self.xpos, self.ypos, self.height, self.width)
        pygame.draw.ellipse(Screen, (0, 0, 0), self.Playerss)
        Screen.blit(player_updated, (self.Playerss.x, self.Playerss.y))

    def draw(self):
        Screen.blit(player_updated, (self.xpos, self.ypos))

    def ammus(self):
            bullet = Bullet(self.xpos + self.width / 2, self.ypos)
            bullets.append(bullet)

class Bullet:
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.speed = 5
        self.radius = 10
        # Luo hitbox ammukselle
        self.hitbox = pygame.Rect(self.xpos - self.radius, self.ypos - self.radius, self.radius * 2, self.radius * 2)

    def move(self):
        self.ypos -= self.speed
        # Päivitä hitboxin sijainti
        self.hitbox = pygame.Rect(self.xpos - self.radius, self.ypos - self.radius, self.radius * 2, self.radius * 2)

    def draw(self):
        pygame.draw.circle(Screen, ammus_color, (int(self.xpos), int(self.ypos)), self.radius)

class Enemy:
    def __init__(self):
        self.size = 1
        self.ypos = 0

    def create_enemy(self):
        Enemy = pygame.Rect(random.randint(100, 700), 0, self.size, self.size)
        enemy_list.append(Enemy)

    def move(self):
        for e in enemy_list:
            self.speed = random.randint(1, 5)
            e.y += self.speed

    def draw(self):
        for e in enemy_list:
            Screen.blit(otokka_updated, (e.x, e.y))

    def check_collision(self, player):
        for e in enemy_list:
            if player.Playerss.colliderect(e):
                player.health -= 20
                enemy_list.remove(e)

player = Player()
enemys = Enemy()
player.create_player()

bullets = []

clock = pygame.time.Clock()

while Running:
    Screen.fill((255, 255, 255))
    tapahtuma = pygame.event.poll()

    if tapahtuma.type == pygame.QUIT:
        Running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_DOWN]:
        player.ypos += 5
    if keys[pygame.K_UP]:
        player.ypos -= 5
    if keys[pygame.K_LEFT]:
        player.xpos -= 5
    if keys[pygame.K_RIGHT]:
        player.xpos += 5
    
    if keys[pygame.K_SPACE]:
        player.ammus()

    if keys[pygame.K_ESCAPE]:
         Running = False

    if tapahtuma.type == SPAWNENEMY:
        enemys.create_enemy()

    enemys.move()

    player.draw()
    enemys.draw()

    for bullet in bullets:
        bullet.move()
        bullet.draw()

        for enemy in enemy_list:
            # Tarkista ammuksen hitboxin ja vihollisen Rectin leikkaus
            if bullet.hitbox.colliderect(enemy):
                bullets.remove(bullet)
                enemy_list.remove(enemy)
                score += 10

    score_text = font.render(f'Pisteet: {score}', True, (0, 0, 0))
    Screen.blit(score_text, (10, 50))

    enemys.check_collision(player)

    if player.health <= 0:
        Running = False

    health_text = font.render(f'Elämäpisteet: {player.health}', True, (0, 0, 0))
    Screen.blit(health_text, (10, 10))

    pygame.display.update()

    clock.tick(60)

pygame.quit()
sys.exit()
