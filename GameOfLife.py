import time
import random
import pygame
import numpy as np

color_bg = (0, 0, 0)
color_grid = (40,40,40)
color_die_next = (100,100,100)
color_live_next = (255,255,255)

def update(screen, cells, size, progress=False):
    updated_cells = np.zeros((cells.shape[0], cells.shape[1]))

    for row, col in np.ndindex(cells.shape):
        alive = np.sum(cells[row-1:row+2, col-1:col+2]) - cells[row, col]
        color = color_live_next if alive == 3 else color_die_next if alive != 2 else color_bg

        if cells[row, col] == 1:
            if alive < 2 or alive > 3:
                if progress:
                    color = color_die_next
            elif 2 <= alive <= 3:
                updated_cells[row, col] = 1
                if progress:
                    color = color_live_next

        else:
            if alive == 3:
                updated_cells[row, col] = 1
                if progress:
                    color = color_live_next

        pygame.draw.rect(screen, color, (col*size, row*size, size - 1, size - 1))

    return updated_cells


def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    cells = np.zeros((60, 80))
    screen.fill(color_bg)
    update(screen, cells, 10)

    pygame.display.flip()
    pygame.display.update()

    running = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = not running
                    update(screen, cells, 10)
                    pygame.display.update()
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                cells[pos[1]//10, pos[0]//10] = 1
                update(screen, cells, 10)
                pygame.display.update()

        screen.fill(color_grid)

        if running:
            cells = update(screen, cells, 10, True)
            pygame.display.update()

        time.sleep(0.01)

if __name__ == '__main__':
    main()
