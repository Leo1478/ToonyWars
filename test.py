import sys
import pygame as pg


pg.init()

screen = pg.display.set_mode((640, 480))
BLACK = pg.Color('black')
FONT = pg.font.Font(None, 32)


def game():
    clock = pg.time.Clock()
    timer = 0
    dt = 0
    running = True

    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.MOUSEBUTTONDOWN:
                print "gay"





                if event.button == 1:
                    if timer == 0:  # First mouse click.
                        timer = 0.001  # Start the timer.
                    # Click again before 0.5 seconds to double click.
                    elif timer < 0.5:
                        print('double click')
                        timer = 0

        # Increase timer after mouse was pressed the first time.
        if timer != 0:
            timer += dt
            # Reset after 0.5 seconds.
            if timer >= 0.5:
                print('too late')
                timer = 0

        screen.fill(BLACK)
        txt = FONT.render(str(round(timer, 2)), True, (180, 190, 40))
        screen.blit(txt, (40, 40))
        pg.display.flip()
        # dt == time in seconds since last tick.
        # / 1000 to convert milliseconds to seconds.
        dt = clock.tick(30) / 1000


if __name__ == '__main__':
    game()
    pg.quit()
    sys.exit()