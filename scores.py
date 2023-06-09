import pygame
import os

pygame.init()

# Set the window size and caption
WINDOW_SIZE = (800, 600)
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("High Scores")

# Set the font and text for the high scores
font = pygame.font.Font(None, 36)
text_color = (155, 155, 155)
high_scores_text = "High Scores:"
high_scores = []

# Set the position of the high scores text
high_scores_x = 50
high_scores_y = 50

# Load the high scores from a text file
if os.path.exists("high_scores.txt"):
    with open("high_scores.txt", "r") as f:
        for line in f:
            name, score = line.strip().split(",")
            high_scores.append((name, int(score)))

# Create the high scores as text objects
high_scores_objects = [font.render(f"{name} - {score}", True, text_color) for name, score in high_scores]

# Set the position of the high scores
high_scores_x = 50
high_scores_y = 100
high_scores_spacing = 50

# Loop until the user clicks the close button
done = False

while not done:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    # Clear the screen
    screen.fill((0, 0, 0))
    
    # Draw the high scores
    screen.blit(font.render(high_scores_text, True, text_color), (high_scores_x, high_scores_y))
    for i in range(len(high_scores_objects)):
        score_pos = (high_scores_x, high_scores_y + (i+1) * high_scores_spacing)
        screen.blit(high_scores_objects[i], score_pos)
    
    # Update the display
    pygame.display.flip()
    
# Quit pygame
pygame.quit()
