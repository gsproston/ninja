import sys, pygame, math

width = 640
height = 400

screen = pygame.display.set_mode([width, height])
pygame.display.set_caption("Ninja")
pygame.display.flip()

class Ninja:
    def __init__(self):
        self.xpos = width/9
        self.ypos = height/5*3
        self.changex = 0.0
        self.speed = 7
        self.moving = False
        self.jumping = False
        self.attacking = False
        self.jumpx = 0
        self.jumpHeight = 60
        self.direction = 1 #1-right 0-left
        self.animationFrame = 0
        self.animationCount = 0
    def move(self):
        if self.moving:
            if self.direction == 1: #going right
                self.changex = 1
            else:
                self.changex = -1
            self.xpos += self.changex
        if self.attacking:
            self.animationCount += 1
            if self.animationCount > 3:
                self.animationCount = 0
                if self.animationFrame < 7:
                    self.animationFrame += 1
                else: #animation over
                    self.animationFrame = 0
                    self.attacking = False
                

class Background:
    def __init__(self):
        self.xpos = 0
        self.ypos = 0
        self.xpos0 = 0
        self.ypos0 = 0
        self.xposFloor = 0
        self.yposFloor = 0

#load in images
backgroundImage = pygame.image.load("./images/background.png")
backgroundImage0 = pygame.image.load("./images/background0.png")
floorImage = pygame.image.load("./images/backgroundFloor.png")
#end loading images

#other variables
ninja = Ninja()
background = Background()

quit = False
while not quit:
    ninjaImage = pygame.image.load("./images/ninja"+str(ninja.animationFrame)+".png")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit = True
        #keypressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                ninja.moving = True
                ninja.direction = 1
            if event.key == pygame.K_a:
                ninja.direction = 0
                ninja.moving = True
            if event.key == pygame.K_SPACE:
                ninja.attacking = True
        #keyreleased
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d and ninja.direction == 1:
                ninja.moving = False
                ninja.changex = 0
                background.changex = 0
            if event.key == pygame.K_a and ninja.direction == 0:
                ninja.moving = False
                ninja.changex = 0
                background.changex = 0

    #other actions
    ninja.move()
    if ninja.changex == 1:
        background.xpos0 += -1
        background.xposFloor += -2
    elif ninja.changex == -1:
        background.xpos0 += 1
        background.xposFloor += 2

    #debugging

    #draw images
    screen.blit(backgroundImage, (background.xpos, background.ypos))
    screen.blit(backgroundImage0, (background.xpos0, background.ypos0))
    screen.blit(floorImage, (background.xposFloor, background.yposFloor))
    screen.blit(ninjaImage, (ninja.xpos, ninja.ypos))
    #end draw images

    pygame.display.update()
    pygame.time.delay(10)

#exit game
pygame.quit()
sys.exit()
