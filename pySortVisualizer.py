import pygame
import random
import sys
import numpy as np
from scipy.io.wavfile import write

# Initialize pygame
pygame.init()
pygame.mixer.init()

# Create a short noise and save as a .wav file
samplerate = 44100
duration = 0.1
frequency = 440
t = np.linspace(0., duration, int(samplerate * duration), endpoint=False)
noise = 0.1 * np.sin(1. * np.pi * frequency * t)
write('noise.wav', samplerate, noise.astype(np.float32))

# Load the sound
noise_sound = pygame.mixer.Sound('noise.wav')
# Set screen dimensions
WIDTH, HEIGHT = 600,400
BACKGROUND_COLOR = (0,0,0)
BAR_COLOR = (169,169,169) # Grey color
ACTIVE_BAR_COLOR = (255,0,0) # Red color for the active bar
BAR_WIDTH = 4
TEXT_COLOR = (255,255,255)
BUTTON_COLOR = (0,0,255)

# Create screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bubble Sort Visualization")

# Generate random heights
num_bars = WIDTH // BAR_WIDTH
bars = [random.randint(1, HEIGHT) for _ in range(num_bars)]

def draw_button():
    font = pygame.font.Font(None, 36)
    text_surf = font.render('Start', True, TEXT_COLOR)
    text_rect = text_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    button_rect = pygame.Rect(WIDTH // 4, HEIGHT // 4, WIDTH // 2, HEIGHT // 2)
    pygame.draw.rect(screen, BUTTON_COLOR, button_rect)
    screen.blit(text_surf, text_rect)
    pygame.display.flip()
    

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
            noise_sound.play()
            pygame.time.delay(1)  # Decrease delay to make it faster
            if bars[j] > bars[j+1] :
                bars[j], bars[j+1] = bars[j+1], bars[j]

start_sorting = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and not start_sorting:
            mouse_pos = event.pos
            if WIDTH // 4 < mouse_pos[0] < 3 * WIDTH // 4 and HEIGHT // 4 < mouse_pos[1] < 3 * HEIGHT // 4:
                start_sorting = True
                bubble_sort(bars)

    if not start_sorting:
        draw_button()
