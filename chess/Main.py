from Pieces import Piece, Pawn, Knight, Rook, Queen, Bishop, King;
import pygame, os, sys;

grid = [
    [Rook(0, 0), Knight(0, 1), Bishop(0, 2), King(0, 3), Queen(0, 4), Bishop(0, 5), Knight(0, 6), Rook(0, 7)],
    [Pawn(1, 0), Pawn(1, 1), Pawn(1, 2), Pawn(1, 3), Pawn(1, 4), Pawn(1, 5), Pawn(1, 6), Pawn(1, 7)],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [Pawn(6, 0), Pawn(6, 1), Pawn(6, 2), Pawn(6, 3), Pawn(6, 4), Pawn(6, 5), Pawn(6, 6), Pawn(6, 7)],
    [Rook(7, 0), Knight(7, 1), Bishop(7, 2), Queen(7, 3), King(7, 4), Bishop(7, 5), Knight(7, 6), Rook(7, 7)]
];

pygame.init();

WIDTH = 800;
HEIGHT = 800;

segHeight = HEIGHT / len(grid);
segWidth = WIDTH / len(grid[0]);

RED = (255, 0, 0);
BLUE = (0, 0, 255);

screen = pygame.display.set_mode((WIDTH, HEIGHT));
pygame.display.set_caption("Chess");

while True:

    screen.fill((0, 0, 0));
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit();

    # Draws pieces & background
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            # Draws background
            pygame.draw.rect(screen, (255, 255, 255), (j * (segWidth), i * (segHeight), segWidth - 1, segHeight - 1));
            piece = grid[i][j];
            # Draws piece if there's a piece there
            if (piece != None):
                piece.draw(screen);

    pygame.display.update();
