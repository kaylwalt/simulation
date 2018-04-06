import heapq
import pygame

from graph import Node, Graph
from grid import GridWorld
from utils import stateNameToCoords
from d_star_lite import initDStarLite, moveAndRescan

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GRAY1 = (145, 145, 102)
GRAY2 = (77, 77, 51)
BLUE = (0, 0, 80)

colors = {
    0: WHITE,
    1: GREEN,
    -1: GRAY1,
    -2: GRAY2
}

# Create a 2 dimensional array. A two dimensional
# array is simply a list of lists.
grid = []
for row in range(10):
    # Add an empty array that will hold each cell
    # in this row
    grid.append([])
    for column in range(10):
        grid[row].append(0)  # Append a cell

# Set row 1, cell 5 to one. (Remember rows and
# column numbers start at zero.)
grid[1][5] = 1

# Initialize pygame
pygame.init()

X_DIM = 10
Y_DIM = 10
VIEWING_RANGE = 3


# distance between node centers

#radius of nodes
RADIUS = 30
GAP = RADIUS * 4
WINDOW_SIZE = (X_DIM* GAP + 4 * RADIUS, Y_DIM * GAP + 4 * RADIUS)

# Set the HEIGHT and WIDTH of the screen
#WINDOW_SIZE = [(WIDTH + MARGIN) * X_DIM + MARGIN,
#               (HEIGHT + MARGIN) * Y_DIM + MARGIN]
screen = pygame.display.set_mode(WINDOW_SIZE)

# Set title of screen
pygame.display.set_caption("D* Lite Path Planning")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

if __name__ == "__main__":
    GRID = GridWorld(X_DIM, Y_DIM, GAP, RADIUS)
    s_start = (1, 0)
    s_goal = (1, 1)
    goal_coords = s_goal
    #goal_coords = stateNameToCoords(s_goal)

    GRID.graph.setStart(s_start)
    GRID.graph.setGoal(s_goal)
    # k_m = 0
    # s_last = s_start
    # queue = []
    #
    # graph, queue, k_m = initDStarLite(graph, queue, s_start, s_goal, k_m)
    #
    # s_current = s_start
    # pos_coords = stateNameToCoords(s_current)
    #
    # basicfont = pygame.font.SysFont('Comic Sans MS', 36)

    redraw_rects = []
    # Set the screen background
    redraw_rects += [screen.fill((153, 204, 255))]
    while not done:
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True  # Flag that we are done so we exit this loop
            # elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            #     # print('space bar! call next action')
            #     s_new, k_m = moveAndRescan(
            #         graph, queue, s_current, VIEWING_RANGE, k_m)
            #     if s_new == 'goal':
            #         print('Goal Reached!')
            #         done = True
            #     else:
            #         # print('setting s_current to ', s_new)
            #         s_current = s_new
            #         pos_coords = stateNameToCoords(s_current)
            #         # print('got pos coords: ', pos_coords)
            #
            # elif event.type == pygame.MOUSEBUTTONDOWN:
            #     # User clicks the mouse. Get the position
            #     pos = pygame.mouse.get_pos()
            #     # Change the x/y screen coordinates to grid coordinates
            #     column = pos[0] // (WIDTH + MARGIN)
            #     row = pos[1] // (HEIGHT + MARGIN)
            #     # Set that location to one
            #     if(graph.cells[row][column] == 0):
            #         graph.cells[row][column] = -1

        # Draw the grid
        redraw_rects += GRID.draw(screen)

        # print('drawing robot pos_coords: ', pos_coords)
        # draw moving robot, based on pos_coords
        # robot_center = [int(pos_coords[0] * (WIDTH + MARGIN) + WIDTH / 2) +
        #                 MARGIN, int(pos_coords[1] * (HEIGHT + MARGIN) + HEIGHT / 2) + MARGIN]
        # pygame.draw.circle(screen, RED, robot_center, int(WIDTH / 2) - 2)
        #
        # # draw robot viewing range
        # pygame.draw.rect(
        #     screen, BLUE, [robot_center[0] - VIEWING_RANGE * (WIDTH + MARGIN), robot_center[1] - VIEWING_RANGE * (HEIGHT + MARGIN), 2 * VIEWING_RANGE * (WIDTH + MARGIN), 2 * VIEWING_RANGE * (HEIGHT + MARGIN)], 2)

        # Limit to 60 frames per second
        clock.tick(60)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.update(redraw_rects)
        redraw_rects = []
    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.
    pygame.quit()
