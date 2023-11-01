import pygame
import sys
import random

pygame.init()

leveys = 1200
korkeus = 1000
ruudun_koko = 60
taustavari = (255, 255, 255)
pelaajan_nopeus = 4
vihollisten_nopeus = 4
ammus_nopeus = 8
pelaajan_elamapisteet = 100
pisteet = 0

pelaaja_kuva = pygame.image.load("pelaaja.png")
pelaaja_kuva = pygame.transform.scale(pelaaja_kuva, (27.5, 57.5))

vihollinen_kuva1 = pygame.image.load("otokka.png")
vihollinen_kuva = pygame.transform.scale(vihollinen_kuva1, (60, 60))

naytto = pygame.display.set_mode((leveys, korkeus))
pygame.display.set_caption("Vihollis peli")

pelaaja_x = leveys // 2 - ruudun_koko // 2
pelaaja_y = korkeus - ruudun_koko * 2

viholliset = []
vihollinen_aika = 0

ammukset = []

ammus_vari = (255, 0, 0)
ammus_koko = 7

fontti = pygame.font.Font(None, 36)
 
kello = pygame.time.Clock()
FPS = 60

# Lisätään debug-tilan muuttuja ja sen alkutila
debug_mode = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            ammukset.append([pelaaja_x + ruudun_koko // 2 + -15, pelaaja_y + 0])
        # Lisätään debug-tila päälle/pois päältä "D" -näppäimellä
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_F8:
            debug_mode = not debug_mode

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and pelaaja_x > 0:
        pelaaja_x -= pelaajan_nopeus
    if keys[pygame.K_RIGHT] and pelaaja_x < leveys - ruudun_koko:
        pelaaja_x += pelaajan_nopeus
    if keys[pygame.K_UP] and pelaaja_y > 0:
        pelaaja_y -= pelaajan_nopeus
    if keys[pygame.K_DOWN] and pelaaja_y < korkeus - ruudun_koko:
        pelaaja_y += pelaajan_nopeus
    if keys[pygame.K_ESCAPE]:
        pygame.quit()
        sys.exit()

    if vihollinen_aika == 0:
        vihollinen_x = random.randint(0, leveys - ruudun_koko)
        viholliset.append([vihollinen_x, 0])
        vihollinen_aika = 100

    for vihollinen in viholliset:
        vihollinen[1] += vihollisten_nopeus

    for ammus in ammukset:
        ammus[1] -= ammus_nopeus

    for ammus in ammukset:
        for vihollinen in viholliset:
            if vihollinen[0] < ammus[0] + ammus_koko // 2 < vihollinen[0] + 60 and vihollinen[1] < ammus[1] + ammus_koko // 2 < vihollinen[1] + 60:
                ammukset.remove(ammus)
                viholliset.remove(vihollinen)
                pisteet += 5

    for vihollinen in viholliset:
        if vihollinen[0] < pelaaja_x < vihollinen[0] + 60 and vihollinen[1] + 60 > pelaaja_y:
            pelaajan_elamapisteet -= 10
            if pelaajan_elamapisteet == 0:
                pygame.quit()
                sys.exit()
            viholliset.remove(vihollinen)

    viholliset = [vihollinen for vihollinen in viholliset if vihollinen[1] < korkeus]

    if vihollinen_aika > 0:
        vihollinen_aika -= 1

    naytto.fill(taustavari)  


    if debug_mode:
        pygame.draw.rect(naytto, (0, 0, 255), (pelaaja_x, pelaaja_y, 27.5, 57.5), 2)
    else:
        naytto.blit(pelaaja_kuva, (pelaaja_x, pelaaja_y))

    for vihollinen in viholliset:
        if debug_mode:
            pygame.draw.rect(naytto, (255, 0, 0), (vihollinen[0], vihollinen[1], 60, 60), 2)
        else:
            naytto.blit(vihollinen_kuva, (vihollinen[0], vihollinen[1]))

    for ammus in ammukset:
        if debug_mode:
            pygame.draw.rect(naytto, (0, 255, 0), (ammus[0], ammus[1], ammus_koko, ammus_koko), 2)
        else:
            pygame.draw.circle(naytto, ammus_vari, (ammus[0], ammus[1]), ammus_koko)

    elamapiste_teksti = fontti.render(f"Elämäpisteet: {pelaajan_elamapisteet}", True, (0, 0, 0))
    pisteet_teksti = fontti.render(f"Pisteet: {pisteet}", True, (0, 0, 0))
    naytto.blit(elamapiste_teksti, (10, 10))
    naytto.blit(pisteet_teksti, (10, 50))

    pygame.display.update()

    kello.tick(FPS)
