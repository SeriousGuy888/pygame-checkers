import sys
import __main__ as main
sys.path.append("..")

def override(f):
    return f

class KingPiece(main.piece.Piece):
    @override
    def move_piece(self):
        pass