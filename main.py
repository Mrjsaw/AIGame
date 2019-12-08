import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("AI Shooter - Imanuel Vancauteren & Seppe Coninx")

walkRight = pygame.image.load('rightsprite.png')
walkLeft = pygame.image.load('leftsprite.png')
walkTop = pygame.image.load('topsprite.png')
walkBottom = pygame.image.load('bottomsprite.png')

clock = pygame.time.Clock()

class player(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = 5
        self.left = False
        self.right = False
        self.top = False
        self.bottom = False

    def draw(self, screen):
        if self.left:
            screen.blit(walkLeft, (self.x, self.y))
        elif self.right:
            screen.blit(walkRight, (self.x, self.y))
        elif self.top:
            screen.blit(walkTop, (self.x, self.y))
        elif self.bottom:
            screen.blit(walkBottom, (self.x, self.y))
        else:
            screen.blit(walkBottom, (self.x, self.y))

class projectile(object):
    def __init__(self,x,y,radius,color,facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.speed = 8 * facing

    def draw(self,screen):
        pygame.draw.circle(screen, self.color, (self.x,self.y), self.radius)

def gameWindow():
    screen.fill((0, 0, 0))
    player.draw(screen)
    pygame.display.update()


#Game loop
player = player(10, 10, 30, 30)
run = True
while run:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and player.x > player.speed:
        player.x -= player.speed
        player.left = True
        player.right = False
        player.top = False
        player.bottom = False
    elif keys[pygame.K_RIGHT] and player.x < 800 - player.speed - player.width:
        player.x += player.speed
        player.left = False
        player.right = True
        player.top = False
        player.bottom = False
    elif keys[pygame.K_UP] and player.y > player.speed:
        player.y -= player.speed
        player.left = False
        player.right = False
        player.top = True
        player.bottom = False
    elif keys[pygame.K_DOWN] and player.y < 600 - player.height - player.speed:
        player.y += player.speed
        player.left = False
        player.right = False
        player.top = False
        player. bottom = True

    gameWindow()

pygame.quit()