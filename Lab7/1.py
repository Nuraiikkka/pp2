import pygame 
from datetime import datetime 
pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((1400, 1050))
pygame.display.set_caption('Mickey Clock')

bg_sound = pygame.mixer.Sound('/Users/nuraiaitbazar/Desktop/pp2/files/clocksound.mp3')
bg_sound.play()

bg = pygame.image.load('/Users/nuraiaitbazar/Desktop/pp2/files/mickey.png')
minute_hand = pygame.image.load('//Users/nuraiaitbazar/Desktop/pp2/files/right.png')
second_hand = pygame.image.load('/Users/nuraiaitbazar/Desktop/pp2/files/left.png') 
rect = bg.get_rect(center=(700, 525))

myfont = pygame.font.Font(None, 36)
text_surface = myfont.render('/Users/nuraiaitbazar/Desktop/pp2/files/Mickey Mouse Clock', True, (0, 0, 0))

running = True

while running:
    
    screen.blit(bg, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
            pygame.quit()
            exit()

    time = datetime.now().time()
    second_angle = -(time.second * 6)
    new_second = pygame.transform.rotate(second_hand, second_angle)
    sec_rect = new_second.get_rect(center=rect.center)
    screen.blit(new_second, sec_rect.topleft)

    minute_angle = -(time.minute * 6 + time.second * 0.1)
    new_minute = pygame.transform.rotate(minute_hand, minute_angle)
    min_rect = new_minute.get_rect(center=rect.center)
    
    screen.blit(new_minute, min_rect.topleft)
    screen.blit(text_surface, (1000, 860))
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
