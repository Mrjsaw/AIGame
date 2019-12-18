"""
 Example program to show using an array to back a grid on-screen.

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/mdTeqiWyFnc
"""
import pygame
import time
import levels




# Create a player
class player():
    def __init__(self, x, y, lives, mines):
        self.x = x
        self.y = y
        self.lives = lives
        self.mines = mines
        self.isAlive = True

class agent():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.isAlive = True

class Node():
    """A node class for A* Pathfinding"""

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position


def astar(maze, start, end):
    """Returns a list of tuples as a path from the given start to the given end in the given maze"""

    # Create start and end node
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    # Initialize both open and closed list
    open_list = []
    closed_list = []

    # Add the start node
    open_list.append(start_node)

    # Loop until you find the end
    while len(open_list) > 0:

        # Get the current node
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        # Pop current off open list, add to closed list
        open_list.pop(current_index)
        closed_list.append(current_node)

        # Found the goal
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1] # Return reversed path

        # Generate children
        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]: # Adjacent squares

            # Get node position
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Make sure within range
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) -1) or node_position[1] < 0:
                continue

            # Make sure walkable terrain
            if maze[node_position[0]][node_position[1]] != 0 and maze[node_position[0]][node_position[1]] != 1 and maze[node_position[0]][node_position[1]] != 4 :
                continue

            # Create new node
            new_node = Node(current_node, node_position)

            # Append
            children.append(new_node)

        # Loop through children
        for child in children:

            # Child is on the closed list
            for closed_child in closed_list:
                if child == closed_child:
                    continue

            # Create the f, g, and h values
            child.g = current_node.g + 1
            #Manhattan distance (geen diagonalen meer)
            #child.h = (abs(child.position[0] - end_node.position[0])) + (abs(child.position[1] - end_node.position[1]) )
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h

            # Child is already in the open list
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            # Add the child to the open list
            open_list.append(child)

# Define some colors
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PINK = (255,153,255)

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 40
HEIGHT = 40

# This sets the margin between each cell
MARGIN = 5

# Create a 2 dimensional array. A two dimensional
# array is simply a list of lists.
grid = []
for row in range(10):
    # Add an empty array that will hold each cell
    # in this row
    grid.append([])
    for column in range(10):
        grid[row].append(0)  # Append a cell
player = player(0, 0, 3, 3)
agent = agent(9,9)
grid = levels.levelOne

start = (agent.x, agent.y)
end = (player.x, player.y)

path = astar(grid, start, end)
print(path)
# Initialize pygame
pygame.init()

startTime = time.time()
lives = 3
pygame.font.init()
myfont = pygame.font.SysFont('Trebuchet MS', 30)
levelText = myfont.render('Level: 1', True, (0, 255, 0))
livesText = myfont.render('Lives: ' + str(player.lives), True, (0, 255, 0))
minesText = myfont.render('Mines: ' + str(player.mines), True, (0, 255, 0))
levelTextRect = levelText.get_rect()
livesTextRect = livesText.get_rect()
minesTextRect = minesText.get_rect()
levelTextRect.center = (552.5, 55)
livesTextRect.center = (552.5, 95)
minesTextRect.center = (552.5, 135)
timeText = myfont.render("Time: " + str(0), True, (0, 255, 0))
timeTextRect = timeText.get_rect()
timeTextRect.center = (552.5, 15)


def algo():
    maze = astar(grid, (agent.x, agent.y), (player.x, player.y))
    print(maze)
    grid[agent.x][agent.y] = 0
    if maze[1][0] == player.x and maze[1][1] == player.y:
        agent.isAlive = False
        player.lives = player.lives - 1
    elif grid[maze[1][0]][maze[1][1]] == 4:
        agent.isAlive = False
        grid[maze[1][0]][maze[1][1]] = 0
    else:
        agent.x = maze[1][0]
        agent.y = maze[1][1]
        grid[agent.x][agent.y] = 2


def drawUI():
    endTime = time.time()
    timeText = myfont.render("Time: " + str(int(endTime - startTime) - 3), True, (0, 255, 0))
    livesText = myfont.render('Lives: ' + str(player.lives), True, (0, 255, 0))
    minesText = myfont.render('Mines: ' + str(player.mines), True, (0, 255, 0))
    screen.blit(timeText, timeTextRect)
    screen.blit(levelText, levelTextRect)
    screen.blit(minesText, minesTextRect)
    screen.blit(livesText, livesTextRect)

# Set the HEIGHT and WIDTH of the screen
WINDOW_SIZE = [650, 455]
screen = pygame.display.set_mode(WINDOW_SIZE)

# Set title of screen
pygame.display.set_caption("AI Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():  # User did something
        keys = pygame.key.get_pressed()
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        elif event.type == pygame.MOUSEBUTTONDOWN and player.mines > 0:
            # User clicks the mouse. Get the position
            pos = pygame.mouse.get_pos()
            # Change the x/y screen coordinates to grid coordinates
            column = pos[0] // (WIDTH + MARGIN)
            row = pos[1] // (HEIGHT + MARGIN)
            # Set that location to one
            if grid[row][column] != 3:
                grid[row][column] = 4
                player.mines = player.mines - 1
                print("Mine planted: ", pos, "Grid coordinates: ", row, column)
        elif keys[pygame.K_LEFT] and player.y > 0 and grid[player.x][player.y - 1] != 3:
            grid[player.x][player.y] = 0
            player.y = player.y - 1
            grid[player.x][player.y] = 1
            if agent.isAlive:
                algo()
        elif keys[pygame.K_RIGHT] and player.y < 9 and grid[player.x][player.y + 1] != 3:
            grid[player.x][player.y] = 0
            player.y = player.y + 1
            grid[player.x][player.y] = 1
            if agent.isAlive:
                algo()
        elif keys[pygame.K_UP] and player.x > 0 and grid[player.x - 1][player.y] != 3:
            grid[player.x][player.y] = 0
            player.x = player.x - 1
            grid[player.x][player.y] = 1
            if agent.isAlive:
                algo()
        elif keys[pygame.K_DOWN] and player.x < 9 and grid[player.x + 1][player.y] != 3:
            grid[player.x][player.y] = 0
            player.x = player.x + 1
            grid[player.x][player.y] = 1
            if agent.isAlive:
                algo()
    # Set the screen background
    screen.fill(BLACK)

    # Draw the grid
    for row in range(10):
        for column in range(10):
            color = WHITE
            if grid[row][column] == 1:
                color = GREEN
            elif grid[row][column] == 2:
               color = RED
            elif grid[row][column] == 3:
                color = PINK
            elif grid[row][column] == 4:
                color = YELLOW
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])


    drawUI()


    # Limit to 30 frames per secon
    clock.tick(30)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()