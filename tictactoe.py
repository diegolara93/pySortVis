import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Set screen dimensions
WIDTH, HEIGHT = 800, 400
BACKGROUND_COLOR = (0,0,0)
BAR_COLOR = (169,169,169) # Grey color
ACTIVE_BAR_COLOR = (255,0,0) # Red color for the active bar
BAR_WIDTH = 4

# Create screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bubble Sort Visualization")

# Generate random heights
num_bars = WIDTH // BAR_WIDTH
bars = [random.randint(1, HEIGHT) for _ in range(num_bars)]

def draw_bars(bars, active_index=None):
    screen.fill(BACKGROUND_COLOR)
    for i, h in enumerate(bars):
        color = BAR_COLOR if i != active_index else ACTIVE_BAR_COLOR
        pygame.draw.rect(screen, color, (i * BAR_WIDTH, HEIGHT - h, BAR_WIDTH, h))
    pygame.display.update()

def bubble_sort(bars):
    n = len(bars)
    for i in range(n):
        for j in range(0, n-i-1):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            draw_bars(bars, j)
            pygame.time.delay(1)  # Decrease delay to make it faster
            if bars[j] > bars[j+1] :
                bars[j], bars[j+1] = bars[j+1], bars[j]

# Visualize the sorting process
bubble_sort(bars)

# Keep the window open until closed by the user
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
