import random
import pygame
from card import FunctionCard
from drop_point import DropPoint

# Init game
pygame.init()

width = 1366
height = 768

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Mushroom Forest")

bg_color = (255, 255, 255)
base_color = [0, 0, 0]
transparent_color = [150, 150, 150]

cards_amount = 4
cards = []

is_moving = False

run = True


# Start game
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    # set background
    screen.fill(bg_color)


    # set variables
    mouse_pos = pygame.mouse.get_pos()
    mouse_pos_x = mouse_pos[0]
    mouse_pos_y = mouse_pos[1]
    l_mouse = pygame.mouse.get_pressed(num_buttons=3)[0]

    for i in range(cards_amount):
        cards.append(FunctionCard(name=f"Test{i}", surface=screen))
        print(cards[i].name + " created!")



    # Game logic

    for card in cards:
        if card.location[0] < mouse_pos_x < card.x_max and card.location[1] < mouse_pos_y < card.y_max:
            if l_mouse and not is_moving:
                is_moving = True

            if not l_mouse:
                is_moving = False

        if is_moving:
            card.set_location(mouse_pos_x - card.width / 2, mouse_pos_y - card.height / 2)
            card.set_color(transparent_color)
        else:
            card.set_color(base_color)


    dp1 = DropPoint(name="Test DropPoint1", surface=screen)


    # Refresh screen every frame.
    pygame.display.update()


pygame.quit()

