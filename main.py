from pygame import *

window = display.set_mode((700, 500))
display.set_caption("Доганялки")
clock = time.Clock()

background = transform.scale(image.load("background.png"), (700, 500))
sprite1 = transform.scale(
    image.load('sprite1.png'),
    (100, 100)
)
sprite2 = transform.scale(
    image.load('sprite2.png'),
    (100, 100)
)

x1 = 100
x2 = 0
y1 = 100
y2 = 0

game = True
while game:
    window.blit(background, (0, 0))
    window.blit(sprite1, (x1, y1))
    window.blit(sprite2, (x2, y2))

    for e in event.get():
        if e.type == QUIT:
            game = False

        keys_pressed = key.get_pressed()
        if keys_pressed[K_LEFT] and x1 > 5:
            x1 -= 10
        if keys_pressed[K_RIGHT] and x1 < 595:
            x1 += 10
        if keys_pressed[K_DOWN] and y1 < 395:
            y1 += 10
        if keys_pressed[K_UP] and y1 > 5:
            y1 -= 10

    clock.tick(60)
    display.update()
