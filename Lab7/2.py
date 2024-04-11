import pygame

pygame.init()
pygame.mixer.init()

bp = '/Users/nuraiaitbazar/Desktop/pp2/files/'

sw, sh = 500, 700
sc = pygame.display.set_mode((sw, sh))
pygame.display.set_caption("Apple Music Simulation")

aip = bp + 'applemusic.png'
mip = bp + 'Apple_Music.png'
sip = [bp + f'0{i}.jpg' for i in range(1, 6)]
aips = [bp + f'00{i}.jpg' for i in range(1, 6)]
sl = [bp + f'0{i}.mp3' for i in range(1, 6)]

si = [pygame.transform.scale(pygame.image.load(p), (sw, sh)) for p in sip]
ai = [pygame.transform.scale(pygame.image.load(p), (sw, sh)) for p in aips]
ap = pygame.transform.scale(pygame.image.load(aip), (sw, sh))
mi = pygame.transform.scale(pygame.image.load(mip), (sw, sh))

ci = 2
cs = 2
im = si[ci]
ip = False

r = True
cl = pygame.time.Clock()

while r:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            r = False
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_RETURN:
                pygame.mixer.music.load(sl[cs])
                pygame.mixer.music.play()
                im = mi
                ip = True
            elif e.key == pygame.K_LEFT:
                cs = (cs - 1) % len(sl)
                ci = cs
                pygame.mixer.music.load(sl[cs])
                pygame.mixer.music.play()
                im = si[ci]
                ip = True
            elif e.key == pygame.K_RIGHT:
                cs = (cs + 1) % len(sl)
                ci = cs
                pygame.mixer.music.load(sl[cs])
                pygame.mixer.music.play()
                im = si[ci]
                ip = True
            elif e.key == pygame.K_UP:
                ci = cs
                pygame.mixer.music.pause()
                im = ai[ci]
                ip = False
            elif e.key == pygame.K_DOWN:
                ci = cs
                pygame.mixer.music.unpause()
                im = si[ci]
                ip = True

    sc.fill((255, 255, 255))
    sc.blit(im, (0, 0))
    pygame.display.update()

    cl.tick(30)

pygame.quit()










