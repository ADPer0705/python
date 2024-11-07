'''
These are the methods that the game will use 
'''

def create_board() :
    '''
    These are the methods that will create a board,
    Once the board is created then the methods that will govern the games will
    be executed on the board that is created
    The "bit-board" concept is used here
    This includes representing the board itseld and the pieces positions with a 64 bit 
    integer where each bit representing the square no, 
    square no being rank * 8 + file
    ranks and file ranges from 0 to 7
    '''

    def print_bitboard(bitboard):
        for rank in range(7, -1, -1):
            for file in range(8):
                square = rank * 8 + file
                if bitboard & (1 << square):
                    print('1', end=' ')
                else:
                    print('0', end=' ')
            print()
        print()

# Print initial positions
# print("White Pawns:")
# print_bitboard(0x000000000000FF00)

# print("White Rooks:")
# print_bitboard(0x0000000000000081)

# print("White Knights:")
# print_bitboard(0x0000000000000042)

# print("White Bishops:")
# print_bitboard(0x0000000000000024)

# print("White Queen:")
# print_bitboard(0x0000000000000008)

# print("White King:")
# print_bitboard(0x0000000000000010)

# print("Black Pawns:")
# print_bitboard(0x00FF000000000000)

# print("Black Rooks:")
# print_bitboard(0x8100000000000000)

# print("Black Knights:")
# print_bitboard(0x4200000000000000)

# print("Black Bishops:")
# print_bitboard(0x2400000000000000)

# print("Black Queen:")
# print_bitboard(0x0800000000000000)

# print("Black King:")
# print_bitboard(0x1000000000000000)
