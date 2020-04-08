import pygame;
import os;
WIDTH = 800;
HEIGHT = 800;

segHeight = HEIGHT / 8;
segWidth = WIDTH / 8;

class Piece(object):
    def __init__(self, row, column, color):
        self.row = row;
        self.column = column;
        self.color = color;

    def get_color(self):
        return self.color;

    def draw(self):
        print("piece");

    def move(self, grid):
        pass;
    
    def get_row(self):
        return self.row;

    def get_column(self):
        return self.column;

    def set_row(self, row):
        self.row = row;

    def set_column(self, column):
        self.column = column;


# Notes: There is an issue when black pieces reach the bottom of the screen, but at that point it should become a piece other than a pawn anyways
class Pawn(Piece):
    def __init__(self, row, column, color):
        super().__init__(row, column, color);
        self.moved = False;

    def draw(self, surface):
        image = None;

        if (self.get_color() == "white"):
            image = pygame.image.load(r'.\images\pawn_white.png');
        else:
            image = pygame.image.load(r'.\images\pawn_black.png');
            
        surface.blit(image, (self.get_column() * segWidth + 18, self.get_row() * segHeight + 18));
    
    def move(self, grid):
        moves = [];
        if (self.color == "white"):
            # Moving just one up
            if (grid[self.get_row() - 1][self.get_column()] == None):
                moves.append([self.get_row() - 1, self.get_column()]);
                # If you can move one, try to move two
                if (self.moved == False):
                    if (grid[self.get_row() - 2][self.get_column()] == None):
                        moves.append([self.get_row() - 2, self.get_column()]);

            # Also check if there is a piece diagonal, since it could move there if there is
            # Checks the top right
            if (self.get_column() + 1 <= 7):
                if (grid[self.get_row() - 1][self.get_column() + 1] != None):
                    # check if the piece is the same color
                    if (self.get_color() != grid[self.get_row() - 1][self.get_column() + 1].get_color()):
                        moves.append([self.get_row() - 1, self.get_column() + 1]);
            
            # Checks the top left
            if (grid[super().get_row() - 1][super().get_column() - 1] != None):
                if (super().get_color() != grid[super().get_row() - 1][super().get_column() - 1].get_color()):
                    moves.append([super().get_row() - 1, super().get_column() - 1]);
        else:
            # Black pieces
            # Moving just one down
            if (grid[super().get_row() + 1][super().get_column()] == None):
                moves.append([super().get_row() + 1, super().get_column()]);
                # If you can move one, try to move two
                if (self.moved == False):
                    if (grid[super().get_row() + 2][super().get_column()] == None):
                        moves.append([super().get_row() + 2, super().get_column()]);

            # Also check if there is a piece diagonal, since it could move there if there is
            # Checks the bottom right
            # Also test case where it's out of bounds
            if (super().get_column() + 1 <= 7):
                if (grid[super().get_row() + 1][super().get_column() + 1] != None):
                    # check if the piece is the same color
                    if (super().get_color() != grid[super().get_row() + 1][super().get_column() + 1].get_color()):
                        moves.append([super().get_row() + 1, super().get_column() + 1]);
            
            # Checks the bottom left
            if (grid[super().get_row() + 1][super().get_column() - 1] != None):
                if (super().get_color() != grid[super().get_row() + 1][super().get_column() - 1].get_color()):
                    moves.append([super().get_row() + 1, super().get_column() - 1]);
        return moves;

class Rook(Piece):
    def __init__(self, row, column, color):
        super().__init__(row, column, color);

    def draw(self, surface):
        image = None;

        if (self.get_color() == "white"):
            image = pygame.image.load(r'.\images\rook_white.png');
        else:
            image = pygame.image.load(r'.\images\rook_black.png');
            
        surface.blit(image, (self.get_column() * segWidth + 18, self.get_row() * segHeight + 18));
    
    def move(self, grid):
        moves = [];
        counter = 0;
        # Looks to the north
        while (self.get_row() - counter > 0):
            counter += 1;
            if (grid[self.get_row() - counter][self.get_column()] == None):
                moves.append([self.get_row() - counter, self.get_column()]);
            else:
                # Check if this is a different color or not
                if (grid[self.get_row() - counter][self.get_column()].get_color() != self.get_color()):
                    moves.append([self.get_row() - counter, self.get_column()]);
                break;
        # Looks to the east
        counter = 0;
        while (self.get_column() + counter < 7):
            counter += 1;
            if (grid[self.get_row()][self.get_column() + counter] == None):
                moves.append([self.get_row(), self.get_column() + counter]);
            else:
                # Check if this is a different color or not
                if (grid[self.get_row()][self.get_column() + counter].get_color() != self.get_color()):
                    moves.append([self.get_row(), self.get_column() + counter]);
                break;

        # Looks to the south
        counter = 0;
        while (self.get_row() + counter < 7):
            counter += 1;
            if (grid[self.get_row() + counter][self.get_column()] == None):
                moves.append([self.get_row() + counter, self.get_column()]);
            else:
                # Check if this is a different color or not
                if (grid[self.get_row() + counter][self.get_column()].get_color() != self.get_color()):
                    moves.append([self.get_row() + counter, self.get_column()]);
                break;

        # Looks to the west
        counter = 0;
        while (self.get_column() - counter > 0):
            counter += 1;
            if (grid[self.get_row()][self.get_column() - counter] == None):
                moves.append([self.get_row(), self.get_column() - counter]);
            else:
                # Check if this is a different color or not
                if (grid[self.get_row()][self.get_column() - counter].get_color() != self.get_color()):
                    moves.append([self.get_row(), self.get_column() - counter]);
                break;
        return moves;

class Knight(Piece):

    def __init__(self, row, column, color):
        super().__init__(row, column, color);

    def draw(self, surface):
        image = None;

        if (self.get_color() == "white"):
            image = pygame.image.load(r'.\images\knight_white.png');
        else:
            image = pygame.image.load(r'.\images\knight_black.png');
            
        surface.blit(image, (self.get_column() * segWidth + 18, self.get_row() * segHeight + 18));
    
    def move(self, grid):
        moves = [];
        row = self.get_row();
        column = self.get_column();

        # Northeast1
        newRow = row - 2;
        newColumn = column + 1;
        # Makes sure its in the grid
        if (newRow >= 0 and newRow <= 7 and newColumn >= 0 and newColumn <= 7):
            if (grid[newRow][newColumn] == None):
                moves.append([newRow, newColumn]);
            elif (grid[newRow][newColumn].get_color() != self.get_color()):
                moves.append([newRow, newColumn]);

        # Northeast2
        newRow = row - 1;
        newColumn = column + 2;
        # Makes sure its in the grid
        if (newRow >= 0 and newRow <= 7 and newColumn >= 0 and newColumn <= 7):
            if (grid[newRow][newColumn] == None):
                moves.append([newRow, newColumn]);
            elif (grid[newRow][newColumn].get_color() != self.get_color()):
                moves.append([newRow, newColumn]);
        
        # Southeast1
        newRow = row + 1;
        newColumn = column + 2;
        # Makes sure its in the grid
        if (newRow >= 0 and newRow <= 7 and newColumn >= 0 and newColumn <= 7):
            if (grid[newRow][newColumn] == None):
                moves.append([newRow, newColumn]);
            elif (grid[newRow][newColumn].get_color() != self.get_color()):
                moves.append([newRow, newColumn]);

        # Southeast2
        newRow = row + 2;
        newColumn = column + 1;
        # Makes sure its in the grid
        if (newRow >= 0 and newRow <= 7 and newColumn >= 0 and newColumn <= 7):
            if (grid[newRow][newColumn] == None):
                moves.append([newRow, newColumn]);
            elif (grid[newRow][newColumn].get_color() != self.get_color()):
                moves.append([newRow, newColumn]);

        # Southwest1
        newRow = row + 2;
        newColumn = column - 1;
        # Makes sure its in the grid
        if (newRow >= 0 and newRow <= 7 and newColumn >= 0 and newColumn <= 7):
            if (grid[newRow][newColumn] == None):
                moves.append([newRow, newColumn]);
            elif (grid[newRow][newColumn].get_color() != self.get_color()):
                moves.append([newRow, newColumn]);

        # Southwest2
        newRow = row + 1;
        newColumn = column - 2;
        # Makes sure its in the grid
        if (newRow >= 0 and newRow <= 7 and newColumn >= 0 and newColumn <= 7):
            if (grid[newRow][newColumn] == None):
                moves.append([newRow, newColumn]);
            elif (grid[newRow][newColumn].get_color() != self.get_color()):
                moves.append([newRow, newColumn]);

        # Northwest1
        newRow = row - 1;
        newColumn = column - 2;
        # Makes sure its in the grid
        if (newRow >= 0 and newRow <= 7 and newColumn >= 0 and newColumn <= 7):
            if (grid[newRow][newColumn] == None):
                moves.append([newRow, newColumn]);
            elif (grid[newRow][newColumn].get_color() != self.get_color()):
                moves.append([newRow, newColumn]);

        # Northwest2
        newRow = row - 2;
        newColumn = column - 1;
        # Makes sure its in the grid
        if (newRow >= 0 and newRow <= 7 and newColumn >= 0 and newColumn <= 7):
            if (grid[newRow][newColumn] == None):
                moves.append([newRow, newColumn]);
            elif (grid[newRow][newColumn].get_color() != self.get_color()):
                moves.append([newRow, newColumn]);

        return moves;

class Bishop(Piece):
    def __init__(self, row, column, color):
        super().__init__(row, column, color);

    def draw(self, surface):
        image = None;

        if (self.get_color() == "white"):
            image = pygame.image.load(r'.\images\bishop_white.png');
        else:
            image = pygame.image.load(r'.\images\bishop_black.png');
            
        surface.blit(image, (self.get_column() * segWidth + 18, self.get_row() * segHeight + 18));

        # # create a text suface object, 
        # # on which text is drawn on it. 
        # text = font.render('Bishop', True, (0, 0, 0), (255, 255, 255)); 
        # # create a rectangular object for the 
        # # text surface object 
        # textRect = text.get_rect();  
        
        # # set the center of the rectangular object. 
        # textRect.center = (super().get_column() * (segWidth) + segWidth // 2, super().get_row() * (segHeight) + segHeight // 2);
        # surface.blit(text, textRect);
    
    def move(self, grid):
        moves = [];
        # Checks northeast
        counter = 1;
        while (self.get_row() - counter >= 0 and self.get_column() + counter <= 7):
            row = self.get_row() - counter;
            column = self.get_column() + counter;
            if (grid[row][column] == None):
                moves.append([row, column]);
            else:
                # Check if this is a different color or not
                if (grid[row][column].get_color() != self.get_color()):
                    moves.append([row, column]);
                break;
            counter += 1;
        # Checks southeast
        counter = 1;
        while (self.get_row() + counter <= 7 and self.get_column() + counter <= 7):
            row = self.get_row() + counter;
            column = self.get_column() + counter;
            if (grid[row][column] == None):
                moves.append([row, column]);
            else:
                # Check if this is a different color or not
                if (grid[row][column].get_color() != self.get_color()):
                    moves.append([row, column]);
                break;
            counter += 1;

        # Checks southwest
        counter = 1;
        while (self.get_row() + counter <= 7 and self.get_column() - counter >= 0):
            row = self.get_row() + counter;
            column = self.get_column() - counter;
            if (grid[row][column] == None):
                moves.append([row, column]);
            else:
                # Check if this is a different color or not
                if (grid[row][column].get_color() != self.get_color()):
                    moves.append([row, column]);
                break;
            counter += 1;


        # Checks northwest
        counter = 1;
        while (self.get_row() - counter >= 0 and self.get_column() - counter >= 0):
            row = self.get_row() - counter;
            column = self.get_column() - counter;
            if (grid[row][column] == None):
                moves.append([row, column]);
            else:
                # Check if this is a different color or not
                if (grid[row][column].get_color() != self.get_color()):
                    moves.append([row, column]);
                break;
            counter += 1;
        
        return moves;

class Queen(Piece):
    def __init__(self, row, column, color):
        super().__init__(row, column, color);

    def draw(self, surface):
        image = None;

        if (self.get_color() == "white"):
            image = pygame.image.load(r'.\images\queen_white.png');
        else:
            image = pygame.image.load(r'.\images\queen_black.png');
            
        surface.blit(image, (self.get_column() * segWidth + 18, self.get_row() * segHeight + 18));
    
    # I just copy pasted the code from the rook and the bishop
    def move(self, grid):
        moves = [];
        # Checks northeast
        counter = 1;
        while (self.get_row() - counter >= 0 and self.get_column() + counter <= 7):
            row = self.get_row() - counter;
            column = self.get_column() + counter;
            if (grid[row][column] == None):
                moves.append([row, column]);
            else:
                # Check if this is a different color or not
                if (grid[row][column].get_color() != self.get_color()):
                    moves.append([row, column]);
                break;
            counter += 1;
        # Checks southeast
        counter = 1;
        while (self.get_row() + counter <= 7 and self.get_column() + counter <= 7):
            row = self.get_row() + counter;
            column = self.get_column() + counter;
            if (grid[row][column] == None):
                moves.append([row, column]);
            else:
                # Check if this is a different color or not
                if (grid[row][column].get_color() != self.get_color()):
                    moves.append([row, column]);
                break;
            counter += 1;

        # Checks southwest
        counter = 1;
        while (self.get_row() + counter <= 7 and self.get_column() - counter >= 0):
            row = self.get_row() + counter;
            column = self.get_column() - counter;
            if (grid[row][column] == None):
                moves.append([row, column]);
            else:
                # Check if this is a different color or not
                if (grid[row][column].get_color() != self.get_color()):
                    moves.append([row, column]);
                break;
            counter += 1;

        # Checks northwest
        counter = 1;
        while (self.get_row() - counter >= 0 and self.get_column() - counter >= 0):
            row = self.get_row() - counter;
            column = self.get_column() - counter;
            if (grid[row][column] == None):
                moves.append([row, column]);
            else:
                # Check if this is a different color or not
                if (grid[row][column].get_color() != self.get_color()):
                    moves.append([row, column]);
                break;
            counter += 1;

        counter = 0;
        # Looks to the north
        while (self.get_row() - counter > 0):
            counter += 1;
            if (grid[self.get_row() - counter][self.get_column()] == None):
                moves.append([self.get_row() - counter, self.get_column()]);
            else:
                # Check if this is a different color or not
                if (grid[self.get_row() - counter][self.get_column()].get_color() != self.get_color()):
                    moves.append([self.get_row() - counter, self.get_column()]);
                break;
        # Looks to the east
        counter = 0;
        while (self.get_column() + counter < 7):
            counter += 1;
            if (grid[self.get_row()][self.get_column() + counter] == None):
                moves.append([self.get_row(), self.get_column() + counter]);
            else:
                # Check if this is a different color or not
                if (grid[self.get_row()][self.get_column() + counter].get_color() != self.get_color()):
                    moves.append([self.get_row(), self.get_column() + counter]);
                break;

        # Looks to the south
        counter = 0;
        while (self.get_row() + counter < 7):
            counter += 1;
            if (grid[self.get_row() + counter][self.get_column()] == None):
                moves.append([self.get_row() + counter, self.get_column()]);
            else:
                # Check if this is a different color or not
                if (grid[self.get_row() + counter][self.get_column()].get_color() != self.get_color()):
                    moves.append([self.get_row() + counter, self.get_column()]);
                break;

        # Looks to the west
        counter = 0;
        while (self.get_column() - counter > 0):
            counter += 1;
            if (grid[self.get_row()][self.get_column() - counter] == None):
                moves.append([self.get_row(), self.get_column() - counter]);
            else:
                # Check if this is a different color or not
                if (grid[self.get_row()][self.get_column() - counter].get_color() != self.get_color()):
                    moves.append([self.get_row(), self.get_column() - counter]);
                break;
        
        return moves;

class King(Piece):
    def __init__(self, row, column, color):
        super().__init__(row, column, color);

    def draw(self, surface):
        image = None;

        if (self.get_color() == "white"):
            image = pygame.image.load(r'.\images\king_white.png');
        else:
            image = pygame.image.load(r'.\images\king_black.png');
            
        surface.blit(image, (self.get_column() * segWidth + 18, self.get_row() * segHeight + 18));
    
    def move(self, grid):
        moves = [];
        row = self.get_row();
        column = self.get_column();
        
        # North
        newRow = row - 1;
        newColumn = column;
        # Makes sure its in the grid
        if (newRow >= 0 and newRow <= 7 and newColumn >= 0 and newColumn <= 7):
            if (grid[newRow][newColumn] == None):
                moves.append([newRow, newColumn]);
            elif (grid[newRow][newColumn].get_color() != self.get_color()):
                moves.append([newRow, newColumn]);
        
        # Northeast
        newRow = row - 1;
        newColumn = column + 1;
        # Makes sure its in the grid
        if (newRow >= 0 and newRow <= 7 and newColumn >= 0 and newColumn <= 7):
            if (grid[newRow][newColumn] == None):
                moves.append([newRow, newColumn]);
            elif (grid[newRow][newColumn].get_color() != self.get_color()):
                moves.append([newRow, newColumn]);

        # East
        newRow = row ;
        newColumn = column + 1;
        # Makes sure its in the grid
        if (newRow >= 0 and newRow <= 7 and newColumn >= 0 and newColumn <= 7):
            if (grid[newRow][newColumn] == None):
                moves.append([newRow, newColumn]);
            elif (grid[newRow][newColumn].get_color() != self.get_color()):
                moves.append([newRow, newColumn]);

        # East
        newRow = row ;
        newColumn = column + 1;
        # Makes sure its in the grid
        if (newRow >= 0 and newRow <= 7 and newColumn >= 0 and newColumn <= 7):
            if (grid[newRow][newColumn] == None):
                moves.append([newRow, newColumn]);
            elif (grid[newRow][newColumn].get_color() != self.get_color()):
                moves.append([newRow, newColumn]);

        # Southeast
        newRow = row + 1;
        newColumn = column + 1;
        # Makes sure its in the grid
        if (newRow >= 0 and newRow <= 7 and newColumn >= 0 and newColumn <= 7):
            if (grid[newRow][newColumn] == None):
                moves.append([newRow, newColumn]);
            elif (grid[newRow][newColumn].get_color() != self.get_color()):
                moves.append([newRow, newColumn]);

        # South
        newRow = row + 1;
        newColumn = column;
        # Makes sure its in the grid
        if (newRow >= 0 and newRow <= 7 and newColumn >= 0 and newColumn <= 7):
            if (grid[newRow][newColumn] == None):
                moves.append([newRow, newColumn]);
            elif (grid[newRow][newColumn].get_color() != self.get_color()):
                moves.append([newRow, newColumn]);
    
        # Southwest
        newRow = row + 1;
        newColumn = column - 1;
        # Makes sure its in the grid
        if (newRow >= 0 and newRow <= 7 and newColumn >= 0 and newColumn <= 7):
            if (grid[newRow][newColumn] == None):
                moves.append([newRow, newColumn]);
            elif (grid[newRow][newColumn].get_color() != self.get_color()):
                moves.append([newRow, newColumn]);

        # West
        newRow = row;
        newColumn = column - 1;
        # Makes sure its in the grid
        if (newRow >= 0 and newRow <= 7 and newColumn >= 0 and newColumn <= 7):
            if (grid[newRow][newColumn] == None):
                moves.append([newRow, newColumn]);
            elif (grid[newRow][newColumn].get_color() != self.get_color()):
                moves.append([newRow, newColumn]);

        # Northwest
        newRow = row - 1;
        newColumn = column - 1;
        # Makes sure its in the grid
        if (newRow >= 0 and newRow <= 7 and newColumn >= 0 and newColumn <= 7):
            if (grid[newRow][newColumn] == None):
                moves.append([newRow, newColumn]);
            elif (grid[newRow][newColumn].get_color() != self.get_color()):
                moves.append([newRow, newColumn]);

        return moves;
