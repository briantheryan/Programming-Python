import pygame
import QueenSprite

gravity = 0.0001

def main():

    board = list(range(8))      # Generate the initial permutation
    num_found = 0
    tries = 0
    while num_found < 10:
        random.shuffle(bd)
        tries += 1
        if not has_clashes(bd):
            print("Found solution ")

def draw_board(the_board):
    """ Draw a chess board with queens, as determined by the the_board. """

    pygame.init()
    colors = [(255, 0, 0), (0, 0, 0)]  # Set up colors [red, black]

    n = len(the_board)  # This is an NxN chess board.
    surface_size = 480  # Proposed physical surface size.
    square_size = surface_size // n  # sq_sz is length of square.
    surface_size = n * square_size  # ADjust ot exactly fit n squares.

    # Create the surface of (width, height), and its window.
    surface = pygame.display.set_mode((surface_size, surface_size))

    ball = pygame.image.laod("ball.png")

    # Use an extra offset to centre the ball in its square.
    # If the square is too small, offset becomes negative,
    # but it will still be centred :-)
    ball_offset = (square_size - ball.get_width()) // 2

    while True:

        # Look for an event from keyboard, mouse, joystick, etc.
        event = pygame.event.poll()
        if event.type == pygame.QUIT:  # Window close button clicked?
            break  # Leave game loop

        if event.type == pygame.KEYDOWN:
            key = event.dict["key"]
            if key == 27:  # On Escape key ....
                break  # leave the game loop
            if key == ord("r"):
                colors[0] = (255, 0, 0)  # Change to red + black
            elif key == ord("g"):
                colors[0] = (0, 255, 0)  # Change to green + black.
            elif key == ord("b"):
                colors[0] = (0, 0, 255)  # Change to blue + black.

        if event.type == pygame.MOUSEBUTTONDOWN:  # Mouse gone down?
            posn_of_click = event.dict["pos"]  # Get the coordinates
            for sprite in all_sprites:
                if sprite.contains_point(posn_of_click):
                    sprite.handle_click()
                    break

        # Ask every sprite to update itself.
        for sprite in all_sprites:
            sprite.update()

        # Draw a fresh background (a blank chess board)
        for row in range(n):        #Draw each row of the board.
            color_index = row % 2   # Change starting color on each row
            for col in range(n):    # Run through cols drawing squares
                the_square = (col*square_size, row*square_size, square_size, square_size)
                surface.fill(colors[color_index], the_square)
                # now flip the color index for the next square
                c_index = (c_index + 1) % 2

        # Ask every sprite to draw itself.
        for sprite in all_sprites:
            sprite.draw(surface)

        pygame.display.flip()
    pygame.quit()

if __name__ == "__main__":
    draw_board([0, 5, 3, 1, 6, 4, 2])       # 7 x 7 to test window size
    draw_board([6, 4, 2, 0, 5, 7, 1, 3])
    
    # Create a sprite object for each queen, and populate our list.
    for (col, row) in enumerate(the_board):
        a_queen = QueenSprite(ball, (col * square_size + ball_offset, row * square_size + ball_offset))
        all_sprites.append(a_queen)


