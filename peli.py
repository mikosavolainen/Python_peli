import random, pygame

pygame.init()
Running = True
Screen = pygame.display.set_mode((900, 1000))

player_img = pygame.image.load('pelaaja.png')
player_updated = pygame.transform.scale(player_img,(200,200))

ammus_img = pygame.image.load('ammus.png')
ammus_updated = pygame.transform.scale(ammus_img,(200,200))

enemy_list = []
enemy_img = pygame.image.load('otokka.png')
enemy_updated = pygame.transform.scale(enemy_img,(200,200))
SPAWNENEMY = pygame.USEREVENT
pygame.time.set_timer(SPAWNENEMY,1000)

class Player:
    def __init__(self):
        self.ypos = 540
        self.xpos = 325
        self.height = 60
        self.width = 60
        self.playerUpdated = player_updated
    def create_player(self):
        self.Playerss = pygame.Rect(self.xpos,self.ypos,self.height,self.width)
        pygame.draw.ellipse(Screen, (0, 0, 0), self.Playerss)
        Screen.blit(player_updated, (self.Playerss.x, self.Playerss.y))
        
    def draw(self):  
        Screen.blit(player_updated, (self.xpos,self.ypos))

    def ammus(self):
          Screen.blit(ammus_updated, (self.xpos,self.ypos))
          while True:
            for bullet in bullets:
                if bullet.x < 500 and bullet.x > 0:
                    bullet.x += bullet.vel



sizee = random.randint(10,40)
randomX = random.randint(0,700)
wut is this
class Enemys:
    def __init__(self):

            self.size = random.randint(10,40)
    def create_enemy(self):
        Enemy = pygame.Rect(random.randint(100,700), 0, self.size,self.size)
        
        enemy_list.append(Enemy)
       
    def draw(self):  
        for e in enemy_list:
            pygame.draw.ellipse(Screen,(255,255,0),e)
            


Player = Player()  
Enemys = Enemys()  
Player.create_player()


bullets = []
while Running:
    Screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False

       

        keys = pygame.key.get_pressed()

        if keys[pygame.K_DOWN]: 
                Player.ypos += 20
        if keys[pygame.K_UP]: 
                Player.ypos -= 20
        if keys[pygame.K_LEFT]:    
                Player.xpos -= 20
        if keys[pygame.K_RIGHT]:
                Player.xpos += 20
        if keys[pygame.K_SPACE]:
                Player.ammus()

        if event.type == SPAWNENEMY:
            Enemys.create_enemy()

    Player.draw()  
    Enemys.draw()  
    pygame.display.update()