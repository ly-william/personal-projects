import pygame;
import sys;
import random;
import os; 

os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init();

WIDTH = 800;
HEIGHT = 800;

NUMCOLUMNS = 20;
NUMROWS = 20;

RED = (255, 0, 0);
BLUE = (0, 0, 255);

screen = pygame.display.set_mode((WIDTH, HEIGHT));
pygame.display.set_caption("Snake");

clock = pygame.time.Clock();

gameOver = False;

# Setup code

# Randomly selects a tile to be head

headPos = [random.randint(0, NUMROWS - 1), random.randint(0, NUMCOLUMNS - 1)];
food = [[random.randint(0, NUMROWS - 1), random.randint(0, NUMCOLUMNS - 1)]];
# print(food);
snake = [headPos];

segHeight = HEIGHT / NUMROWS;
segWidth = WIDTH / NUMCOLUMNS;

direction = ""

# Returns a coordinate that is not already used by a snake
def randomViableCoord():
    potentialCoord = [random.randint(0, NUMROWS - 1), random.randint(0, NUMCOLUMNS - 1)];
    for coord in snake:
        if coord[0] == potentialCoord[0] and coord[1] == potentialCoord[1]:
            return randomViableCoord();

    return potentialCoord;

myFont = pygame.font.SysFont("monospace", 40);
text = myFont.render("Snake", True, (255, 255, 0), (0, 0, 0));
textRect = text.get_rect();
textRect.center = (WIDTH // 2, HEIGHT // 2);

while not gameOver:
    
    screen.fill((0, 0, 0));
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit();
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and direction != "east":
                direction = "west";
            if event.key == pygame.K_RIGHT and direction != "west":
                direction = "east";
            if event.key == pygame.K_UP and direction != "south":
                direction = "north";
            if event.key == pygame.K_DOWN and direction != "north":
                direction = "south";

    # Draws background
    for i in range(NUMROWS):
        for j in range(NUMCOLUMNS):
            pygame.draw.rect(screen, (255, 255, 255), (j * (segWidth), i * (segHeight), segWidth - 2, segHeight - 2));

    # Draws food
    for coord in food:
        pygame.draw.rect(screen, BLUE, (coord[0] * (segWidth), coord[1] * (segHeight), segWidth - 2, segHeight - 2));

    # Draws snake
    for coord in snake:
        pygame.draw.rect(screen, RED, (coord[0] * (segWidth), coord[1] * (segHeight), segWidth - 2, segHeight - 2));

    if (direction == ""):
        screen.blit(text, textRect);

    # Moves position of snake
    newHead = [snake[0][0], snake[0][1]];
    if direction == "west":
        newHead[0] -= 1;
    if direction == "east":
        newHead[0] += 1;
    if direction == "north":
        newHead[1] -= 1;
    if direction == "south":
        newHead[1] += 1;
    snake.insert(0, newHead);
    del snake[-1];

    # Hit detection for food
    for i in range(len(food)):
        coord = food[i];
        if coord[0] == snake[0][0] and coord[1] == snake[0][1]:
            del food[i];
            food.append(randomViableCoord());
            # Offscreen so the user doesn't see it while it's updating
            snake.append([-1, -1]);
    
    # Hit detection for itself
    if (len(snake) != 1):
        for i in range(1, len(snake)):
            if (snake[0][0] == snake[i][0] and snake[0][1] == snake[i][1]):
                gameOver = True;
                break;

    # Hit detection against walls
    if (snake[0][0] < 0 or snake[0][0] > NUMCOLUMNS - 1 or snake[0][1] < 0 or snake[0][1] > NUMROWS - 1):
        gameOver = True;

    clock.tick(30);
    pygame.display.update();