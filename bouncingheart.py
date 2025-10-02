import pygame
import sys

pygame.init()

display_info = pygame.display.Info()
screen_width = display_info.current_w
screen_height = display_info.current_h

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Bouncing Heart")

heart_image = pygame.image.load('heart.png').convert_alpha()  # Load image with transparency support
heart_rect = heart_image.get_rect()
heart_speed = [1, 1]


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    heart_rect = heart_rect.move(heart_speed)

    if heart_rect.left < 0 or heart_rect.right > screen_width:
        heart_speed[0] = -heart_speed[0]

    if heart_rect.top < 0 or heart_rect.bottom > screen_height:
        heart_speed[1] = -heart_speed[1]

    screen.fill((255, 255, 255))

    screen.blit(heart_image, heart_rect)

    pygame.display.flip()

    pygame.time.delay(10)

