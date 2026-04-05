import pygame
import datetime
import os

pygame.init()

# окно
screen = pygame.display.set_mode((1200, 700))
pygame.display.set_caption("Mickey Clock")

WHITE = (255, 255, 255)

# путь к картинкам
base = r'/Users/hoka7e/Practice2/Practice9/mickeys_clock/images'

# загрузка
clock_img = pygame.image.load(os.path.join(base, 'clock.png')).convert_alpha()
mickey    = pygame.image.load(os.path.join(base, 'mUmrP.png')).convert_alpha()
hand_l    = pygame.image.load(os.path.join(base, 'hand_left.png')).convert_alpha()   # seconds
hand_r    = pygame.image.load(os.path.join(base, 'hand_right.png')).convert_alpha()  # minutes

# масштаб
clock_img = pygame.transform.scale(clock_img, (800, 600))
mickey    = pygame.transform.scale(mickey, (350, 350))
hand_l    = pygame.transform.scale(hand_l, (80, 80))
hand_r    = pygame.transform.scale(hand_r, (100, 100))

# центр часов
CENTER = (600, 320)

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 60)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # текущее время
    now = datetime.datetime.now()
    m = now.minute
    s = now.second

    # углы
    seconds_angle = -(s * 6)     # левая рука (секунды)
    minutes_angle = -(m * 6)     # правая рука (минуты)

    # вращение
    rotated_seconds = pygame.transform.rotate(hand_l, seconds_angle)
    rotated_minutes = pygame.transform.rotate(hand_r, minutes_angle)

    # центрируем
    seconds_rect = rotated_seconds.get_rect(center=CENTER)
    minutes_rect = rotated_minutes.get_rect(center=CENTER)

    # отрисовка
    screen.fill(WHITE)

    clock_rect = clock_img.get_rect(center=CENTER)
    screen.blit(clock_img, clock_rect)

    mickey_rect = mickey.get_rect(center=CENTER)
    screen.blit(mickey, mickey_rect)

    screen.blit(rotated_minutes, minutes_rect)
    screen.blit(rotated_seconds, seconds_rect)

    # текст времени
    time_text = font.render(f"{m:02}:{s:02}", True, (0, 0, 0))
    screen.blit(time_text, (50, 50))

    pygame.display.flip()

    # обновление раз в секунду
    clock.tick(1)

pygame.quit()