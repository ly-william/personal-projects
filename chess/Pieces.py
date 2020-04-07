import pygame;
import os;
pygame.init();

WIDTH = 800;
HEIGHT = 800;

segHeight = HEIGHT / 8;
segWidth = WIDTH / 8;

class Piece(object):
    def __init__(self, row, column):
        self.row = row;
        self.column = column;
    
    def draw(self):
        print("piece");

    def move(self):
        pass;
    
    def get_row(self):
        return self.row;

    def get_column(self):
        return self.column;

class Pawn(Piece):
    def __init__(self, row, column):
        super().__init__(row, column);

    def draw(self, surface):
        font = pygame.font.SysFont('monospace', 24) 
  
        # create a text suface object, 
        # on which text is drawn on it. 
        text = font.render('Pawn', True, (0, 0, 0), (255, 255, 255)); 
        # create a rectangular object for the 
        # text surface object 
        textRect = text.get_rect();  
        
        # set the center of the rectangular object. 
        textRect.center = (super().get_column() * (segWidth) + segWidth // 2, super().get_row() * (segHeight) + segHeight // 2);
        surface.blit(text, textRect);
    
    def move(self):
        pass;

class Rook(Piece):
    def __init__(self, row, column):
        super().__init__(row, column);

    def draw(self, surface):
        font = pygame.font.SysFont('monospace', 24) 
  
        # create a text suface object, 
        # on which text is drawn on it. 
        text = font.render('Rook', True, (0, 0, 0), (255, 255, 255)); 
        # create a rectangular object for the 
        # text surface object 
        textRect = text.get_rect();  
        
        # set the center of the rectangular object. 
        textRect.center = (super().get_column() * (segWidth) + segWidth // 2, super().get_row() * (segHeight) + segHeight // 2);
        surface.blit(text, textRect);
    
    def move(self):
        pass;

class Knight(Piece):

    def __init__(self, row, column):
        super().__init__(row, column);

    def draw(self, surface):
        font = pygame.font.SysFont('monospace', 24) 
  
        # create a text suface object, 
        # on which text is drawn on it. 
        text = font.render('Knight', True, (0, 0, 0), (255, 255, 255)); 
        # create a rectangular object for the 
        # text surface object 
        textRect = text.get_rect();  
        
        # set the center of the rectangular object. 
        textRect.center = (super().get_column() * (segWidth) + segWidth // 2, super().get_row() * (segHeight) + segHeight // 2);
        surface.blit(text, textRect);
    
    def move(self):
        pass;

class Bishop(Piece):
    def __init__(self, row, column):
        super().__init__(row, column);

    def draw(self, surface):
        font = pygame.font.SysFont('monospace', 24) 
  
        # create a text suface object, 
        # on which text is drawn on it. 
        text = font.render('Bishop', True, (0, 0, 0), (255, 255, 255)); 
        # create a rectangular object for the 
        # text surface object 
        textRect = text.get_rect();  
        
        # set the center of the rectangular object. 
        textRect.center = (super().get_column() * (segWidth) + segWidth // 2, super().get_row() * (segHeight) + segHeight // 2);
        surface.blit(text, textRect);
    
    def move(self):
        pass;

class Queen(Piece):
    def __init__(self, row, column):
        super().__init__(row, column);

    def draw(self, surface):
        font = pygame.font.SysFont('monospace', 24) 
  
        # create a text suface object, 
        # on which text is drawn on it. 
        text = font.render('Queen', True, (0, 0, 0), (255, 255, 255)); 
        # create a rectangular object for the 
        # text surface object 
        textRect = text.get_rect();  
        
        # set the center of the rectangular object. 
        textRect.center = (super().get_column() * (segWidth) + segWidth // 2, super().get_row() * (segHeight) + segHeight // 2);
        surface.blit(text, textRect);
    
    def move(self):
        pass;

class King(Piece):
    def __init__(self, row, column):
        super().__init__(row, column);

    def draw(self, surface):
        font = pygame.font.SysFont('monospace', 24) 
  
        # create a text suface object, 
        # on which text is drawn on it. 
        text = font.render('King', True, (0, 0, 0), (255, 255, 255)); 
        # create a rectangular object for the 
        # text surface object 
        textRect = text.get_rect();  
        
        # set the center of the rectangular object. 
        textRect.center = (super().get_column() * (segWidth) + segWidth // 2, super().get_row() * (segHeight) + segHeight // 2);
        surface.blit(text, textRect);
    
    def move(self):
        pass;