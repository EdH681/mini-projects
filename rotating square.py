import pygame
from math import sin, cos, radians

pygame.init()
win = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()

points = [(200, 200), (300, 600),  (400, 200), (400, 400), (200, 400), (100, 100)]


def pygame_to_centred(__points):
    __points = __points[:]
    for p, point in enumerate(__points):
        x = point[0]
        y = point[1]
        x -= 300
        y -= 300
        __points[p] = (x, y)
    return __points


def centred_to_pygame(__points):
    __points = __points[:]
    for p, point in enumerate(__points):
        x = point[0]
        y = point[1]
        x += 300
        y += 300
        __points[p] = (x, y)
    return __points


def rotate_points(__points: list[tuple], angle: float) -> list[tuple]:
    __points = __points[:]
    angle = radians(angle)
    for p, point in enumerate(__points):
        point_x = point[0]
        point_y = point[1]
        x = (point_x * cos(angle)) + (point_y * sin(angle))
        y = (-point_x * sin(angle)) + (point_y * cos(angle))
        __points[p] = (x, y)
    return centred_to_pygame(__points)


theta = 0

running = True
while running:
    win.fill("black")
    draw_points = rotate_points(pygame_to_centred(points), theta)
    pygame.draw.polygon(win, "white", draw_points, 1)
    theta += 1

    pygame.display.update()
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
