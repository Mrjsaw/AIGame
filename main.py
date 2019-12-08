import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("AI Shooter - Imanuel Vancauteren & Seppe Coninx")

#Spawn position
x = 10
y = 10

#Character size
width = 30
height = 30

#Move pixels
move = 5

walkRight = pygame.image.load('rightsprite.png')
walkLeft = pygame.image.load('leftsprite.png')
walkTop = pygame.image.load('topsprite.png')
walkBottom = pygame.image.load('bottomsprite.png')

right = False
left = False
bottom = False
top = False
walkCount = 0

def gameWindow():
    global walkCount
    if left:
        screen.blit(walkLeft, (x,y))
    elif right:
        screen.blit(walkRight, (x,y))
    elif top:
        screen.blit(walkTop, (x,y))
    elif bottom:
        screen.blit(walkBottom, (x,y))
    else:
        screen.blit(walkBottom, (x, y))
    pygame.display.update()

run = True
clock = pygame.time.Clock()

#Game loop
while run:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > move:
        x -= move
        left = True
        right = False
        top = False
        bottom = False
    elif keys[pygame.K_RIGHT] and x < 800 - move - width:
        x += move
        left = False
        right = True
        top = False
        bottom = False
    elif keys[pygame.K_UP] and y > move:
        y -= move
        left = False
        right = False
        top = True
        bottom = False
    elif keys[pygame.K_DOWN] and y < 600 - height - move:
        y += move
        left = False
        right = False
        top = False
        bottom = True

    screen.fill((0,0,0))
    pygame.draw.rect(screen, (255,0,0), (x,y, width, height))
    gameWindow()

pygame.quit()