import pygame

pygame.init()

screenWidth = 500
screenHeight = 500
win = pygame.display.set_mode((screenWidth,screenHeight))
pygame.display.set_caption("Managing Keys")
clock = pygame.time.Clock()

x = 50
y = 50
speed = 4
width = 20
height = 40
run = True
fps = 30

# ** Top left corner will always be (0,0) **
# * Bottom right corner will always be (width,height) *

jump = False
jumpCount = 8

while run:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > speed:
        x -= speed
    if keys[pygame.K_RIGHT] and x < screenWidth - width - speed:
        x += speed
    if not(jump):
        if keys[pygame.K_UP] and y > speed:
            y -= speed
        if keys[pygame.K_DOWN] and y < screenHeight - height - speed:
            y += speed
        if keys[pygame.K_SPACE]:
            jump = True
    else:
        if jumpCount >= -8:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) * 0.5 * neg
            jumpCount -= 1
        else:
            jump = False
            jumpCount = 8
    win.fill((34,5,9))
    pygame.draw.rect(win, (255,255,255), (x,y,width,height))
    pygame.display.update()
    
pygame.quit()