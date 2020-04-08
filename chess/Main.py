from Pieces import Piece, Pawn, Knight, Rook, Queen, Bishop, King;
import pygame, os, sys, copy;
os.environ['SDL_VIDEO_CENTERED'] = '1'

grid = [
    [Rook(0, 0, "black"), Knight(0, 1, "black"), Bishop(0, 2, "black"), King(0, 3, "black"), Queen(0, 4, "black"), Bishop(0, 5, "black"), Knight(0, 6, "black"), Rook(0, 7, "black")],
    [Pawn(1, 0, "black"), Pawn(1, 1, "black"), Pawn(1, 2, "black"), Pawn(1, 3, "black"), Pawn(1, 4, "black"), Pawn(1, 5, "black"), Pawn(1, 6, "black"), Pawn(1, 7, "black")],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [Pawn(6, 0, "white"), Pawn(6, 1, "white"), Pawn(6, 2, "white"), Pawn(6, 3, "white"), Pawn(6, 4, "white"), Pawn(6, 5, "white"), Pawn(6, 6, "white"), Pawn(6, 7, "white")],
    [Rook(7, 0, "white"), Knight(7, 1, "white"), Bishop(7, 2, "white"), Queen(7, 3, "white"), King(7, 4, "white"), Bishop(7, 5, "white"), Knight(7, 6, "white"), Rook(7, 7, "white")]
];

# Piece that was clicked on
clickedCoords = None;

# Piece that is currently selected to move
selectedCoords = None;

# Holds the positions of where the selected piece can move
possibleMoves = [];

pygame.init();

WIDTH = 800;
HEIGHT = 800;

segHeight = HEIGHT / len(grid);
segWidth = WIDTH / len(grid[0]);

RED = (255, 105, 97);
BLUE = (65,105,225);
black = (255, 255, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT));
pygame.display.set_caption("Chess");

def get_clicked_coord(x, y):
    for i in range(len(grid)):
        row = grid[i];
        for j in range(len(row)):
            # Determines which coordinate was selected
            if (j * segWidth < x and x < j * segWidth + segWidth and i * segHeight < y and y < i * segHeight + segHeight):
                return [i, j];

turn = "white";

while True:

    screen.fill((0, 0, 0));
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit();
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If they left click
            if event.button == 1:
                x, y = pygame.mouse.get_pos();
                # Figures out which piece was clicked and makes it clicked
                clickedCoords = get_clicked_coord(x, y);
                # print(clickedCoords);
                                
    # Draws DEFAULT background
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pygame.draw.rect(screen, black, (j * (segWidth), i * (segHeight), segWidth - 1, segHeight - 1));

    # Draws anything additional
    if (clickedCoords != None):
        # If the user clicked somewhere that is not a possible move, not a piece, and not the right color
        # print(grid[clickedCoords[0]]);
        # print(selectedCoords);
        # print(clickedCoords);
        if ((clickedCoords not in possibleMoves and grid[clickedCoords[0]][clickedCoords[1]] == None) or (grid[clickedCoords[0]][clickedCoords[1]] != None and grid[clickedCoords[0]][clickedCoords[1]].get_color() != turn and clickedCoords not in possibleMoves)):
            del possibleMoves[:];
            # Case for where the first thing the user clicks on is nothing
            if (selectedCoords != None):
                del selectedCoords[:];
        else:
            # If there are possible moves currently
            if (len(possibleMoves) != 0):
                # Draws the possible moves
                for move in possibleMoves:
                    pygame.draw.rect(screen, BLUE, (move[1] * (segWidth), move[0] * (segHeight), segWidth - 1, segHeight - 1));
                # If where they clicked is a possible move
                if (clickedCoords in possibleMoves):
                    # Saves the piece
                    tempPiece = copy.copy(grid[selectedCoords[0]][selectedCoords[1]]);
                    grid[selectedCoords[0]][selectedCoords[1]] = None;
                    grid [clickedCoords[0]][clickedCoords[1]] = tempPiece;
                    tempPiece.set_row(clickedCoords[0]);
                    tempPiece.set_column(clickedCoords[1]);
                    if (type(tempPiece) is Pawn):
                        tempPiece.moved = True;
                    # Sets the next turn
                    if (turn == "white"):
                        turn = "black";
                    else:
                        turn = "white";
                    
                    del possibleMoves[:];
                    clickedCoords = None;
                else:
                    # This means the user is selected a new piece to view
                    selectedCoords = [clickedCoords[0], clickedCoords[1]];
                    clickedPiece = grid[clickedCoords[0]][clickedCoords[1]];
                    pygame.draw.rect(screen, RED, (clickedPiece.get_column() * (segWidth), clickedPiece.get_row() * (segHeight), segWidth - 1, segHeight - 1));
                    del [possibleMoves[:]];
                    # Add possible moves to possibleMoves list
                    possibleMoves = clickedPiece.move(grid);
                    # print(possibleMoves);
            else:
                # This means the user is selected a new piece to view
                selectedCoords = [clickedCoords[0], clickedCoords[1]];
                clickedPiece = grid[clickedCoords[0]][clickedCoords[1]];
                pygame.draw.rect(screen, RED, (clickedPiece.get_column() * (segWidth), clickedPiece.get_row() * (segHeight), segWidth - 1, segHeight - 1));
                del [possibleMoves[:]];
                # Add possible moves to possibleMoves list
                possibleMoves = clickedPiece.move(grid);
                # print(possibleMoves);

    # Draws pieces
    for row in grid:
        for piece in row:
            if (piece != None):
                piece.draw(screen);

    pygame.display.update();
