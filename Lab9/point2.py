import pygame
pygame.init()

painting = []

timer = pygame.time.Clock()

fps = 60 #frames per second

activeColor = (0, 0, 0)
activeShape = 0

w = 800
h = 600

screen = pygame.display.set_mode([w, h])

#title
pygame.display.set_caption("Paint")

def drawDisplay():
    pygame.draw.rect(screen, 'gray', [0, 0, w, 100]) # Draw Display
    pygame.draw.line(screen, 'black', [0, 100], [w, 100]) # Draw Line separator
    rect = [pygame.draw.rect(screen, 'black', [10, 10, 80, 80]), 0]
    pygame.draw.rect(screen, 'white', [20, 20, 60, 60])
    circ = [pygame.draw.rect(screen, 'black', [100, 10, 80, 80]), 1]
    pygame.draw.circle(screen, 'white', [140, 50], 30)
    # rhombus
    rhomb = [pygame.draw.rect(screen, 'black', [190, 10, 80, 80]), 2]
    pygame.draw.polygon(screen, 'white', [(230, 20), (260, 50), (230, 80), (200, 50)])
    # equilateral triangle
    tri = [pygame.draw.rect(screen, 'black', [280, 10, 80, 80]), 3]
    pygame.draw.polygon(screen, 'white', [(320, 20), (290, 80), (350, 80)])
    

#draw colors
    blue = [pygame.draw.rect(screen, (0, 0, 255), [w - 35, 10, 25, 25]), (0, 0, 255)] 
    red = [pygame.draw.rect(screen, (255, 0, 0), [w - 35, 35, 25, 25]), (255, 0, 0)]
    green = [pygame.draw.rect(screen, (0, 255, 0), [w - 60, 10, 25, 25]), (0, 255, 0)] 
    yellow = [pygame.draw.rect(screen, (255, 255, 0), [w - 60, 35, 25, 25]), (255, 255, 0)] 
    black = [pygame.draw.rect(screen, (0, 0, 0), [w - 85, 10, 25, 25]), (0, 0, 0)] 
    purple = [pygame.draw.rect(screen, (255, 0, 255), [w - 85, 35, 25, 25]), (255, 0, 255)] 

# Draw Eraser
    eraser = [pygame.draw.rect(screen, (255, 255, 255), [w - 150, 20, 25, 25]), (255, 255, 255)]
    return [blue, red, green, yellow, black, purple, eraser], [rect, circ, rhomb, tri]

def drawPaint(paints):
    for paint in paints:
        color, pos, shape = paint
        if shape == 3:
            pygame.draw.polygon(screen, color, [(pos[0], pos[1] - 20), (pos[0] - 17, pos[1] + 10), (pos[0] + 17, pos[1] + 10)])
        elif shape == 2:
            pygame.draw.polygon(screen, color, [(pos[0], pos[1] - 15), (pos[0] + 15, pos[1]), (pos[0], pos[1] + 15), (pos[0] - 15, pos[1])])
        elif shape == 1:  # Circle
            pygame.draw.circle(screen, color, pos, 15)
        elif shape == 0:  # Rectangle
            pygame.draw.rect(screen, color, [pos[0]-15, pos[1]-15, 30, 30])
        
        
def draw():
    global activeColor, activeShape, mouse
    if mouse[1] > 100:
        if activeShape == 0:
            pygame.draw.rect(screen, activeColor, [mouse[0]-15, mouse[1]-15, 30, 30])
        if activeShape == 1:
            pygame.draw.circle(screen, activeColor, mouse, 15)
        if activeShape == 2:
            pygame.draw.polygon(screen, activeColor, [(mouse[0], mouse[1] - 15), (mouse[0] + 15, mouse[1]), (mouse[0], mouse[1] + 15), (mouse[0] - 15, mouse[1])])
        if activeShape == 3:
            pygame.draw.polygon(screen, activeColor, [(mouse[0], mouse[1] - 15), (mouse[0] - 15, mouse[1] + 15), (mouse[0] + 15, mouse[1] + 15)])
run = True
while run:
    timer.tick(fps) #set FPS
    screen.fill('white')
    colors, shape = drawDisplay() 

    mouse = pygame.mouse.get_pos() #get Mouse Position
    draw()
    
    click = pygame.mouse.get_pressed()[0] #get Mouse Button Pressed
    if click and mouse[1] > 100:
        painting.append((activeColor, mouse, activeShape)) #add mouse position to List
    drawPaint(painting)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_ESCAPE:
                run = False

        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_SPACE:
                painting = []

        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in colors:
                if i[0].collidepoint(event.pos):
                    activeColor = i[1]
            for i in shape:
                if i[0].collidepoint(event.pos):
                    activeShape = i[1]
    

    pygame.display.flip()