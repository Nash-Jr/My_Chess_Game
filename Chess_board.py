import pygame
import sys

pygame.init()

size = (850, 850)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Chess Remix")


square_size = size[0] // 8
board = pygame.Surface((size[0], size[1]))
board.fill((255, 206, 158))

for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0:
            pygame.draw.rect(board, (210, 180, 140),
                             (i * square_size, j * square_size, square_size, square_size))
        else:
            pygame.draw.rect(board, (139, 69, 19), (i * square_size,
                             j * square_size, square_size, square_size))

screen.blit(board, (0, 0))
pygame.display.flip()

# Main event loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Quit Pygame
pygame.quit()
sys.exit()
