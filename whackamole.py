import pygame
import random


def draw_grid(screen):
    GRID_COLOR = (0, 100, 0)
    SQUARE_SIZE = 32

    # vertical lines
    for x in range(0, 640 + 1, SQUARE_SIZE):
        pygame.draw.line(screen, GRID_COLOR, (x, 0), (x, 512))

    # horizontal lines
    for y in range(0, 512 + 1, SQUARE_SIZE):
        pygame.draw.line(screen, GRID_COLOR, (0, y), (640, y))


def get_random_position():
    # Get random grid coordinates (20x16 grid)
    x = random.randrange(0, 20) * 32  # 20 columns
    y = random.randrange(0, 16) * 32  # 16 rows
    return (x, y)


def main():
    try:
        pygame.init()
        mole_image = pygame.image.load("mole.png")
        mole_image = pygame.transform.scale(mole_image, (30, 30))

        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()

        # Start mole in top-left
        mole_pos = (0, 0)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:

                    mouse_x, mouse_y = event.pos

                    mole_rect = mole_image.get_rect(topleft=mole_pos)
                    if mole_rect.collidepoint(mouse_x, mouse_y):

                        mole_pos = get_random_position()


            screen.fill("light green")


            draw_grid(screen)


            screen.blit(mole_image, mole_image.get_rect(topleft=mole_pos))

            pygame.display.flip()
            clock.tick(60)

    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
