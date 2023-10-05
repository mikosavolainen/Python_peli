import random
import pygame

pygame.init()
Running = True

Screen = pygame.display.set_mode((400, 300), pygame.FULLSCREEN)

player_img = pygame.image.load('pelaaja.png')
player_updated = pygame.transform.scale(player_img, (200, 200))

ammus_img = pygame.image.load('ammus.png')
ammus_updated = pygame.transform.scale(ammus_img, (200, 200))

enemy_list = []
otokka_img = pygame.image.load('otokka.png')  # Käytä otokka.png-kuvaa
otokka_updated = pygame.transform.scale(otokka_img, (200, 200))  # Muuta kuvan kokoa tarvittaessa
SPAWNENEMY = pygame.USEREVENT
pygame.time.set_timer(SPAWNENEMY, 1000)

class Player:
    def __init__(self):
        self.ypos = 540
        self.xpos = 325
        self.height = 60
        self.width = 60
        self.playerUpdated = player_updated
        self.can_shoot = True

    def create_player(self):
        self.Playerss = pygame.Rect(self.xpos, self.ypos, self.height, self.width)
        pygame.draw.ellipse(Screen, (0, 0, 0), self.Playerss)
        Screen.blit(player_updated, (self.Playerss.x, self.Playerss.y))

    def draw(self):
        Screen.blit(player_updated, (self.xpos, self.ypos))

    def ammus(self):
        if self.can_shoot:
            bullet = Bullet(self.xpos + self.width / 2, self.ypos)
            bullets.append(bullet)
            self.can_shoot = False

class Bullet:
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.speed = 5
        self.bulletUpdated = ammus_updated

    def move(self):
        self.ypos -= self.speed

    def draw(self):
        Screen.blit(ammus_updated, (self.xpos, self.ypos))

class Enemy:
    def __init__(self):
        self.size = random.randint(10, 40)

    def create_enemy(self):
        Enemy = pygame.Rect(random.randint(100, 700), 0, self.size, self.size)
        enemy_list.append(Enemy)

    def draw(self):
        for e in enemy_list:
            Screen.blit(otokka_updated, (e.x, e.y))  # Piirrä otokka.png vihollisten tilalle

player = Player()
enemys = Enemy()
player.create_player()

bullets = []

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

    player.draw()
    enemys.draw()

    for bullet in bullets:
        bullet.move()
        bullet.draw()

    bullets = [bullet for bullet in bullets if bullet.ypos > 0]

    if len(bullets) == 0:
        player.can_shoot = True

    pygame.display.update()
