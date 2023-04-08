import pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((640, 480))

# Set up the font
font = pygame.font.SysFont(None, 50)

# Set up the options
options = ['New game', 'High scores', 'Sound effects', 'Quit game']
option_items = ["Sound: On"]
option_selected = 0
sound_on = True

text_color = (255, 255, 255)
option_objects = [font.render(item, True, text_color) for item in option_items]

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                option_selected = (option_selected - 1) % len(options)
            elif event.key == pygame.K_DOWN:
                option_selected = (option_selected + 1) % len(options)
            elif event.key == pygame.K_RETURN:
                # Perform action based on selected option
                if option_selected == 0:
                    print('Option 1 selected')
                elif option_selected == 1:
                    print('Option 2 selected')
                    # Toggle sound on/off
                elif option_selected == 2:
                    sound_on = not sound_on
                    option_items[0] = "sound:" + ("On" if sound_on else "Off")
                    option_objects[0] = font.render(option_items[0], True, text_color)
                    print("Sound is now", "On" if sound_on else "Off")
                    
                elif option_selected == 3:
                    pygame.quit()
                    sys.exit()
                    print('Option 4 selected')
    
    # Draw the menu options
    screen.fill((255, 255, 255))
    for i in range(len(options)):
        text = font.render(options[i], True, (0, 0, 0))
        if i == option_selected:
            # Highlight the selected option
            pygame.draw.rect(screen, (255, 0, 0), (200, 200 + i*50, 280, 50))
        screen.blit(text, (220, 210 + i*50))
    
    # Update the display
    pygame.display.flip()
