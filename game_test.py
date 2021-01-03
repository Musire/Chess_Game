import pygame
import players
import moves
import pieces
import board
from pygame.locals import *
import math

GREY = (128, 128, 128)
SILVER = (192, 192, 192)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
TEAL = (0, 153, 153)
LIGHT = (194, 214, 214)
DARK_TEAL = (20, 31, 31)


#class models

class Square(pygame.sprite.Sprite):
    def __init__(self, length, width, color):
        super(Square, self).__init__()

        self.width = width
        self.length = length
        self.color = color
        self.surf = pygame.Surface((self.length, self.width))
        self.surf.fill(self.color)
        self.rect = self.surf.get_rect()


class representation():
    def __init__(self, rep, surf):
        self.rep = rep
        self.surf = surf

    @property
    def pos(self):
        crude = self.rep.current
        return matrix_to_coordinate(crude, 80, 30)



def create_spots(size, color_1, color_2):
    answer = []

    for i in range(1, 9):
        for j in range(1, 9):
            if (j+i) % 2 == 0:
                result = Square(size, size, color_1)
            else:
                result = Square(size, size, color_2)
            
            answer.append(result)

    return answer


def create_squares(space, offset):
    arr = []
    for i in range(8):
        for j in range(8):
            column = (j*space)+offset
            row = (i*space)+offset

            arr.append((row, column))
    return arr


def plane_coordinates(starting):
    arr = [starting]
    for i in range(1, 8):
        new_value = [starting[0]+(80*i), starting[1]]
        arr.append(new_value)

    for j in range(8):
        new_value = [starting[0]+(80*j), starting[1]+80]
        arr.append(new_value)

    return arr


def center_coordinate(pos, size, background_size):
    arr = []
    for p in pos:
        reduced = p * size
        answer = reduced + background_size + (size * .5)
        arr.append(answer)

    return arr[::-1]


def coordinate_to_matrix(pos, size, background_size):
    arr = []
    for p in pos:
        reduced = p - background_size
        answer = math.floor(reduced / size)
        arr.append(answer)

    return arr[::-1]


def matrix_to_coordinate(pos, size, background_size):
    arr = []
    for p in pos:
        reduced = p * size
        answer = reduced + background_size
        arr.append(answer)

    return arr
    

def Enlist(entry, coordinate):
    if len(SELECTED) == 0:
        if entry == 0:
            pass
        elif entry != 0:
            SELECTED.append(entry)
    elif len(SELECTED) != 0:
        if entry in SELECTED:
            del SELECTED[0]
        elif entry not in SELECTED:
            for each in SELECTED:
                each.check_surrounding(chess_board)
                moves = each.moves
                if coordinate in moves:
                    DESTINATION.append(coordinate)
                elif entry != 0 and coordinate not in moves:
                    SELECTED[0] = entry
 

def kill_piece(piece, arr_1, arr_2):
    for i in arr_1:
        if i == piece:
            arr_1.remove(i)
            arr_2.append(piece)


#create and set up the board matrix

chess_board = board.board()
ALL_PIECES = pieces.all_pieces
chess_board.fill_board(ALL_PIECES)


# represent each pieace with an image
bl_rook_1 = representation(pieces.black_rook_1, pygame.image.load('black_rook.png'))
bl_rook_2 = representation(pieces.black_rook_2, pygame.image.load('black_rook.png'))
bl_knight_1 = representation(pieces.black_knight_1, pygame.image.load('black_knight.png'))
bl_knight_2 = representation(pieces.black_knight_2, pygame.image.load('black_knight.png'))
bl_bishop_1 = representation(pieces.black_bishop_1, pygame.image.load('black_bishop.png'))
bl_bishop_2 = representation(pieces.black_bishop_2, pygame.image.load('black_bishop.png'))
bl_queen = representation(pieces.black_queen, pygame.image.load('black_queen.png'))
bl_king = representation(pieces.black_king, pygame.image.load('black_king.png'))

bl_pawn_1 = representation(pieces.black_pawn_1, pygame.image.load('black_pawn.png'))
bl_pawn_2 = representation(pieces.black_pawn_2, pygame.image.load('black_pawn.png'))
bl_pawn_3 = representation(pieces.black_pawn_3, pygame.image.load('black_pawn.png'))
bl_pawn_4 = representation(pieces.black_pawn_4, pygame.image.load('black_pawn.png'))
bl_pawn_5 = representation(pieces.black_pawn_5, pygame.image.load('black_pawn.png'))
bl_pawn_6 = representation(pieces.black_pawn_6, pygame.image.load('black_pawn.png'))
bl_pawn_7 = representation(pieces.black_pawn_7, pygame.image.load('black_pawn.png'))
bl_pawn_8 = representation(pieces.black_pawn_8, pygame.image.load('black_pawn.png'))

wh_rook_1 = representation(pieces.white_rook_1, pygame.image.load('white_rook.png'))
wh_rook_2 = representation(pieces.white_rook_2, pygame.image.load('white_rook.png'))
wh_knight_1 = representation(pieces.white_knight_1, pygame.image.load('white_knight.png'))
wh_knight_2 = representation(pieces.white_knight_2, pygame.image.load('white_knight.png'))
wh_bishop_1 = representation(pieces.white_bishop_1, pygame.image.load('white_bishop.png'))
wh_bishop_2 = representation(pieces.white_bishop_2, pygame.image.load('white_bishop.png'))
wh_queen = representation(pieces.white_queen, pygame.image.load('white_queen.png'))
wh_king = representation(pieces.white_king, pygame.image.load('white_king.png'))

wh_pawn_1 = representation(pieces.white_pawn_1, pygame.image.load('white_pawn.png'))
wh_pawn_2 = representation(pieces.white_pawn_2, pygame.image.load('white_pawn.png'))
wh_pawn_3 = representation(pieces.white_pawn_3, pygame.image.load('white_pawn.png'))
wh_pawn_4 = representation(pieces.white_pawn_4, pygame.image.load('white_pawn.png'))
wh_pawn_5 = representation(pieces.white_pawn_5, pygame.image.load('white_pawn.png'))
wh_pawn_6 = representation(pieces.white_pawn_6, pygame.image.load('white_pawn.png'))
wh_pawn_7 = representation(pieces.white_pawn_7, pygame.image.load('white_pawn.png'))
wh_pawn_8 = representation(pieces.white_pawn_8, pygame.image.load('white_pawn.png'))


# last needed settings
outer_spots = create_spots(80, LIGHT, TEAL)
outer_squares = create_squares(80, 20)

pygame.init()
gameOn = True
x, y = 1200, 680

screen = pygame.display.set_mode((x, y))

Background_1 = Square(1190, 670, GREY)
Background_2 = Square(660, 660, SILVER)
background_3 = Square(650, 650, DARK_TEAL)


ALIVE = [wh_pawn_1, wh_pawn_2, wh_pawn_3, wh_pawn_4, wh_pawn_5, wh_pawn_6, wh_pawn_7, wh_pawn_8,
wh_rook_1, wh_knight_1, wh_bishop_1, wh_queen, wh_king, wh_bishop_2, wh_knight_2, wh_rook_2,
bl_pawn_1, bl_pawn_2, bl_pawn_3, bl_pawn_4, bl_pawn_5, bl_pawn_6, bl_pawn_7, bl_pawn_8,
bl_rook_1, bl_knight_1, bl_bishop_1, bl_queen, bl_king, bl_bishop_2, bl_knight_2, bl_rook_2]

KILLED = []
SELECTED = []
DESTINATION = []

#dictionary bind of rep and physical
PIECE_BOND = {ALL_PIECES[i]: ALIVE[i] for i in range(len(ALL_PIECES))}




#final code

def main(gameOn):
    TURN = moves.move()

    while gameOn:
        # for loop through the event queue
        for event in pygame.event.get():

            if event.type == KEYDOWN:

               if event.key == K_BACKSPACE:

                   gameOn = False

            elif event.type == QUIT:
                gameOn = False

            elif event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                n_pos = [pos[0], pos[1]]
                coordinate = coordinate_to_matrix(n_pos, 80, 30)
                selected = chess_board.board[coordinate[0]][coordinate[1]]

                if selected == 0:
                    if len(SELECTED)>0:
                        Enlist(selected, coordinate)
                elif selected != 0 and len(SELECTED) == 0:
                    if selected.color == TURN.current_turn:
                        Enlist(selected, coordinate)
                elif selected != 0 and len(SELECTED) > 0:
                    Enlist(selected, coordinate)


        screen.blit(Background_1.surf, (5,  5))
        screen.blit(Background_2.surf, (10, 10))
        screen.blit(background_3.surf, (15, 15))
        
        for (spot, square) in zip(outer_spots, outer_squares):
            screen.blit(spot.surf, square)

        for piece in ALIVE:
            screen.blit(piece.surf, (piece.pos[1],piece.pos[0]))




        DOTS = []

        if len(SELECTED) != 0:
            for each in SELECTED:
                each.check_surrounding(chess_board)

                dots = each.moves
                DOTS = dots

        if len(DOTS) != 0:
            for dot in DOTS:
                red_dot = pygame.draw.circle(screen, RED, center_coordinate(dot, 80, 20), 10)

        if len(SELECTED)>0 and len(DESTINATION)>0:
            for (piece, destination) in zip(SELECTED, DESTINATION):
                oppo = chess_board.board[destination[0]][destination[1]]
                if oppo != 0:
                    kill_piece(PIECE_BOND.get(oppo), ALIVE, KILLED)
                    piece.move(chess_board, destination)
                    TURN.turn_queue.append(piece.color)
                    del SELECTED[0]
                    del DESTINATION[0]

                elif oppo == 0:
                    piece.move(chess_board, destination)
                    TURN.turn_queue.append(piece.color)
                    del SELECTED[0]
                    del DESTINATION[0]

                

                

        pygame.display.flip()
        

if __name__ == '__main__':
    main(gameOn)

    

