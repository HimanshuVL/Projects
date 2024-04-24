import pygame
import sys
screen_width, screen_height = 800, 800
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
bg = pygame.image.load("black bg.jpg")
bg = pygame.transform.scale(bg, (screen_width, screen_height))

path = [((0, 50), (90, 40)), ((50, 75), (40, 100)), ((50, 150), (100, 40)), ((120, 150), (40, 110)), ((150, 220),
        (100, 40)), ((250, 220), (40, 200)), ((100, 400), (190, 40)), ((100, 400), (40, 100)), ((100, 500), (100, 40)),
        ((200, 500), (40, 100)), ((200, 600), (240, 40)), ((400, 500), (40, 100)), ((440, 500), (75, 40)), ((480, 50),
        (40, 490)), ((500, 50), (150, 40)), ((610, 75), (40, 150)), ((610, 200), (130, 40))]
run = True
pygame.mouse.set_pos((25, 65))
clock = pygame.time.Clock()
font = pygame.font.Font(None, 60)
while run:
    clock.tick(15)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if any(b[0][0] < pygame.mouse.get_pos()[0] < b[1][0]+b[0][0] and
           b[0][1] < pygame.mouse.get_pos()[1] < b[1][1]+b[0][1] for b in path):
        pass
    else:
        run = False

    screen.blit(bg, (0, 0))
    if((pygame.mouse.get_pos()[0]-800)**2+(pygame.mouse.get_pos()[1]-215)**2) <= 100**2:
        msg = font.render("YOU WON", True, (255, 255, 0))
        screen.blit(msg, (250, 100))
    for x in path:
        pygame.draw.rect(screen, (255, 255, 255), x)

    pygame.draw.circle(screen, (255, 0, 0), (715, 220), 10)
    pygame.display.update()
