import pygame
import datetime
import os

pygame.init()


screen = pygame.display.set_mode((1200, 700))
pygame.display.set_caption("Mickey Clock")

WHITE = (255, 255, 255)

base = r'/Users/hoka7e/Practice2/Practice9/mickeys_clock/images'

clock_img = pygame.image.load(os.path.join(base, 'clock.png')).convert_alpha()
mickey    = pygame.image.load(os.path.join(base, 'mUmrP.png')).convert_alpha()
hand_l    = pygame.image.load(os.path.join(base, 'hand_left.png')).convert_alpha()  
hand_r    = pygame.image.load(os.path.join(base, 'hand_right.png')).convert_alpha() 


clock_img = pygame.transform.scale(clock_img, (800, 600))
mickey    = pygame.transform.scale(mickey, (350, 350))
hand_l    = pygame.transform.scale(hand_l, (80, 80))
hand_r    = pygame.transform.scale(hand_r, (100, 100))


CENTER = (600, 320)

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 60)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    now = datetime.datetime.now()
    m = now.minute
    s = now.second


    seconds_angle = -(s * 6)   
    minutes_angle = -(m * 6)    


    rotated_seconds = pygame.transform.rotate(hand_l, seconds_angle)
    rotated_minutes = pygame.transform.rotate(hand_r, minutes_angle)


    seconds_rect = rotated_seconds.get_rect(center=CENTER)
    minutes_rect = rotated_minutes.get_rect(center=CENTER)


    screen.fill(WHITE)

    clock_rect = clock_img.get_rect(center=CENTER)
    screen.blit(clock_img, clock_rect)

    mickey_rect = mickey.get_rect(center=CENTER)
    screen.blit(mickey, mickey_rect)

    screen.blit(rotated_minutes, minutes_rect)
    screen.blit(rotated_seconds, seconds_rect)

    time_text = font.render(f"{m:02}:{s:02}", True, (0, 0, 0))
    screen.blit(time_text, (50, 50))

    pygame.display.flip()

    clock.tick(1)

pygame.quit()