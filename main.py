# File: main.py

import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Quantum Quest: Particle Physics Adventure")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Main game loop
def main():
    clock = pygame.time.Clock()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Fill the screen with black
        screen.fill(BLACK)

        # Draw a white rectangle in the center
        pygame.draw.rect(screen, WHITE, (width/2 - 50, height/2 - 50, 100, 100))

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(60)

if __name__ == "__main__":
    main()